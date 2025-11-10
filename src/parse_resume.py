# src/parse_resume.py
import os
from typing import Dict, List
from docx import Document
import fitz  # PyMuPDF
from .utils import clean_text, simple_skill_extractor

DEFAULT_SKILLS = [
    "Python", "SQL", "Pandas", "Excel", "Power BI", "Tableau",
    "Machine Learning", "Scikit-learn", "TensorFlow", "PyTorch",
    "Data Analysis", "NLP", "Deep Learning", "Linux", "Git"
]


# -----------------------------
# PDF and DOCX Extractors
# -----------------------------
def extract_text_from_pdf(path: str) -> str:
    """Extract all text from a PDF file."""
    with fitz.open(path) as doc:
        text = [page.get_text() for page in doc]
    return "\n".join(text)


def extract_text_from_docx(path: str) -> str:
    """Extract all text from a DOCX file."""
    doc = Document(path)
    return "\n".join([p.text for p in doc.paragraphs])


# -----------------------------
# Job Role Detection
# -----------------------------
def detect_job_role(text: str, skills: List[str]) -> str:
    """Detect the most likely job role based on resume content and skills"""
    text_lower = text.lower()
    
    # Define job role patterns with keywords
    job_roles = {
        "software engineer": [
            "software engineer", "software developer", "backend developer", 
            "frontend developer", "full stack", "java", "javascript", "react", 
            "node.js", "spring", "django", "flask"
        ],
        "data scientist": [
            "data scientist", "machine learning", "deep learning", "ai", 
            "artificial intelligence", "neural network", "tensorflow", "pytorch", 
            "keras", "nlp", "computer vision", "model"
        ],
        "data analyst": [
            "data analyst", "business analyst", "data analysis", "analytics", 
            "excel", "power bi", "tableau", "sql", "reporting", "dashboard", 
            "visualization", "pandas"
        ],
        "data engineer": [
            "data engineer", "etl", "data pipeline", "airflow", "spark", 
            "hadoop", "kafka", "data warehouse", "bigquery", "snowflake"
        ],
        "ml engineer": [
            "ml engineer", "machine learning engineer", "mlops", "model deployment", 
            "scikit-learn", "model training", "feature engineering"
        ],
        "web developer": [
            "web developer", "frontend", "backend", "html", "css", "javascript", 
            "react", "angular", "vue", "web development"
        ],
        "devops engineer": [
            "devops", "ci/cd", "docker", "kubernetes", "jenkins", "aws", 
            "azure", "cloud", "infrastructure", "deployment"
        ]
    }
    
    # Score each role based on keyword matches
    role_scores = {}
    for role, keywords in job_roles.items():
        score = 0
        for keyword in keywords:
            if keyword.lower() in text_lower:
                score += 1
            # Check if keyword is in skills list
            if skills:
                for skill in skills:
                    if keyword.lower() in skill.lower():
                        score += 2  # Skills match counts more
        role_scores[role] = score
    
    # Get the role with highest score
    if role_scores:
        best_role = max(role_scores, key=role_scores.get)
        if role_scores[best_role] > 0:
            return best_role
    
    # Default fallback based on common skills
    skills_lower = [s.lower() for s in skills] if skills else []
    if any(skill in skills_lower for skill in ["python", "sql", "pandas", "excel", "tableau", "power bi"]):
        return "data analyst"
    elif any(skill in skills_lower for skill in ["tensorflow", "pytorch", "machine learning", "deep learning"]):
        return "data scientist"
    elif any(skill in skills_lower for skill in ["java", "javascript", "react", "node"]):
        return "software engineer"
    
    return "data analyst"  # Final fallback


# -----------------------------
# Resume Parser
# -----------------------------
def parse_resume(path: str) -> Dict:
    """Parse a resume and extract key info like email, phone, and skills."""

    # ✅ Handle relative paths safely
    if not os.path.isabs(path):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        path = os.path.abspath(os.path.join(base_dir, "..", path))

    # ✅ Check file existence
    if not os.path.exists(path):
        raise FileNotFoundError(f"Resume file not found at: {path}")

    # -----------------------------
    # Extract text from resume
    # -----------------------------
    text = ""
    if path.lower().endswith(".pdf"):
        text = extract_text_from_pdf(path)
    elif path.lower().endswith(".docx"):
        text = extract_text_from_docx(path)
    else:
        with open(path, 'r', encoding='utf-8') as f:
            text = f.read()

    text = clean_text(text)

    # -----------------------------
    # Heuristics: email, phone, name
    # -----------------------------
    import re
    email, phone, name = None, None, None

    m = re.search(r'[\w\.-]+@[\w\.-]+\.\w+', text)
    if m:
        email = m.group(0)

    m = re.search(r'(\+?\d{10,15})', text.replace(" ", ""))
    if m:
        phone = m.group(0)
    
    # Extract name - typically the first line or first few words
    lines = text.split('\n')
    for line in lines[:5]:  # Check first 5 lines
        line = line.strip()
        # Skip lines that are too long or too short
        if 2 <= len(line.split()) <= 4 and len(line) < 50:
            # Check if it looks like a name (contains mostly letters)
            if re.match(r'^[A-Z][a-z]+(\s+[A-Z][a-z]+)*$', line.strip()):
                name = line.strip()
                break
    
    # If still no name, try to find a name-like pattern
    if not name:
        name_patterns = [
            r'\b([A-Z][a-z]+\s+[A-Z][a-z]+(?:\s+[A-Z][a-z]+)?)\b',  # Full name
            r'Name[:\s]+([A-Z][a-z]+\s+[A-Z][a-z]+)',  # "Name: John Doe"
        ]
        for pattern in name_patterns:
            m = re.search(pattern, text[:500])  # Search in first 500 chars
            if m:
                name = m.group(1) if 'Name' in pattern else m.group(0)
                break

    # -----------------------------
    # Skills extraction
    # -----------------------------
    skills = simple_skill_extractor(text, DEFAULT_SKILLS)

    # -----------------------------
    # Naive section extraction
    # -----------------------------
    experience, education = [], []
    lower = text.lower()

    # Extract experience section
    if "experience" in lower or "work experience" in lower:
        start = lower.find("experience")
        end = lower.find("education")
        if end == -1:
            end = start + 1000
        extract = text[start:end]
        experience = [line.strip() for line in extract.split("\n") if line.strip()][:20]

    # Extract education section
    if "education" in lower:
        start = lower.find("education")
        extract = text[start:start + 1000]
        education = [line.strip() for line in extract.split("\n") if line.strip()][:20]
    
    # -----------------------------
    # Detect target job role from resume
    # -----------------------------
    target_role = detect_job_role(text, skills)

    # -----------------------------
    # Return structured data
    # -----------------------------
    return {
        "raw_text": text,
        "email": email,
        "phone": phone,
        "name": name,
        "skills": skills,
        "experience_snippets": experience,
        "education_snippets": education,
        "target_role": target_role,
        "file_path": path
    }


# -----------------------------
# Script Entry Point
# -----------------------------
if __name__ == "__main__":
    import sys

    # Default resume path if none given
    p = sys.argv[1] if len(sys.argv) > 1 else "../data/devashish_resume.pdf"

    print(f"[1/6] Parsing resume: {p}")

    try:
        result = parse_resume(p)
        print(result)
    except FileNotFoundError as e:
        print(f"❌ Error: {e}")
    except Exception as e:
        print(f"⚠️ Unexpected error: {e}")
