# src/generate_cover.py
from typing import Dict
import os
import json
from datetime import datetime
from docx import Document
from docx.shared import Pt, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from config import LOCAL_LLM_MODEL_PATH, COVER_LETTERS_DIR

# Try to use GPT4All if available, otherwise use a template fallback
def generate_cover_with_template(resume_summary: Dict, job: Dict) -> str:
    """Generate a formal, personalized cover letter using template - HEAVILY based on resume"""
    title = job.get("title", "Position")
    company = job.get("company", "Company")
    desc = job.get("description", "")[:1000]  # Reduced - focus more on resume
    
    # Handle case where resume_summary might be a string instead of dict
    if isinstance(resume_summary, str):
        skills_str = "various technical skills"
        name = "[Your Name]"
        email = "[Your Email]"
        phone = "[Your Phone]"
        experience_text = "my professional experience"
        all_skills = []
        exp_snippets = []
    else:
        skills_list = resume_summary.get("skills", [])
        all_skills = skills_list
        # Get top 6 most relevant skills for emphasis
        skills_str = ", ".join(skills_list[:6]) if skills_list else "various technical skills"
        name = resume_summary.get("name") or "[Your Name]"
        email = resume_summary.get("email") or "[Your Email]"
        phone = resume_summary.get("phone") or "[Your Phone]"
        
        # Get experience snippets - FOCUS ON RESUME CONTENT
        exp_snippets = resume_summary.get("experience_snippets", [])
        if exp_snippets and len(exp_snippets) > 2:
            # Extract meaningful experience lines (skip headers)
            meaningful_exp = [e for e in exp_snippets if len(e) > 20 and not e.isupper()]
            experience_text = f"my experience including {meaningful_exp[0] if meaningful_exp else 'relevant work'}"
        else:
            experience_text = "my professional background"
    
    # Extract job requirements but keep minimal - RESUME is the focus
    desc_lower = desc.lower()
    job_keywords = []
    if "python" in desc_lower and "Python" in all_skills:
        job_keywords.append("Python")
    if "sql" in desc_lower and "SQL" in all_skills:
        job_keywords.append("SQL")
    if "data" in desc_lower and any("data" in s.lower() for s in all_skills):
        data_skills = [s for s in all_skills if "data" in s.lower()]
        if data_skills:
            job_keywords.extend(data_skills[:2])
    
    # Build resume-focused content
    date_str = datetime.now().strftime("%B %d, %Y")
    
    # INTRO - Focus on YOUR skills and experience
    intro = f"Dear Hiring Manager,\n\nI am writing to express my strong interest in the {title} position at {company}. As a professional with expertise in {skills_str}, I am excited about the opportunity to contribute my skills and experience to your team."
    
    # BODY 1 - YOUR RESUME EXPERIENCE (80% resume, 20% job match)
    if exp_snippets and len(exp_snippets) > 3:
        # Use actual resume content
        relevant_exp = [e.strip() for e in exp_snippets if len(e.strip()) > 15][:3]
        exp_details = ". I have also ".join(relevant_exp[:2]) if len(relevant_exp) >= 2 else relevant_exp[0] if relevant_exp else "gained valuable experience"
        body1 = f"\n\nThroughout my career, {exp_details}. My hands-on experience with {skills_str} has equipped me with the technical proficiency and problem-solving abilities essential for this role."
    else:
        body1 = f"\n\nMy professional background includes substantial experience with {skills_str}. I have consistently demonstrated strong analytical and technical capabilities, which I am eager to apply to the challenges at {company}."
    
    # BODY 2 - YOUR SKILLS AND ACHIEVEMENTS (90% resume)
    skill_highlights = ", ".join(all_skills[:8]) if len(all_skills) > 6 else skills_str
    body2 = f"\n\nMy core competencies include {skill_highlights}. I have developed these skills through rigorous practical application and continuous learning. "
    
    # Add minimal job connection if keywords match
    if job_keywords:
        matched_skills = ", ".join(job_keywords[:3])
        body2 += f"I noticed that your position requires proficiency in {matched_skills}, which aligns perfectly with my skill set. "
    
    body2 += f"I am confident that my technical expertise and dedication to excellence will enable me to make meaningful contributions to {company}."
    
    # CLOSING - Professional and confident
    closing = f"\n\nI am enthusiastic about the possibility of bringing my skills and experience to {company}. I would welcome the opportunity to discuss how my background aligns with your team's needs. Thank you for considering my application, and I look forward to the possibility of speaking with you soon.\n\nSincerely,\n{name}"
    
    if email != "[Your Email]":
        closing += f"\n{email}"
    if phone != "[Your Phone]":
        closing += f"\n{phone}"
    
    return date_str + "\n\n" + intro + body1 + body2 + closing

def generate_cover_gpt4all(resume_summary: Dict, job: Dict, n_tokens: int = 300) -> str:
    # lazy import to avoid making it required
    try:
        from gpt4all import GPT4All
    except Exception as e:
        print("gpt4all not available:", e)
        return generate_cover_with_template(resume_summary, job)

    model_path = LOCAL_LLM_MODEL_PATH
    if not os.path.exists(model_path):
        print("Local LLM model file not found at", model_path)
        return generate_cover_with_template(resume_summary, job)

    try:
        prompt = build_prompt(resume_summary, job)
        gptj = GPT4All(model_path)
        # Using .generate; API depends on model type/version. This is a simple example.
        reply = gptj.generate(prompt, max_tokens=n_tokens)
        if isinstance(reply, (list, tuple)):
            reply = reply[0]
        # Ensure we return a string
        return str(reply) if reply else generate_cover_with_template(resume_summary, job)
    except Exception as e:
        print("LLM generation failed:", e)
        return generate_cover_with_template(resume_summary, job)

def build_prompt(resume_summary: Dict, job: Dict) -> str:
    # Handle case where resume_summary might be a string instead of dict
    if isinstance(resume_summary, str):
        name = "the candidate"
        skills = "various technical skills"
        experience = "Relevant professional experience"
        email = ""
        phone = ""
        education = ""
    else:
        name = resume_summary.get("name") or "the candidate"
        skills = ", ".join(resume_summary.get("skills", [])[:10])  # More skills from resume
        experience = "\n".join(resume_summary.get("experience_snippets", [])[:8])  # More experience details
        email = resume_summary.get("email") or ""
        phone = resume_summary.get("phone") or ""
        education = "\n".join(resume_summary.get("education_snippets", [])[:3])
    
    job_title = job.get("title", "")
    company = job.get("company", "")
    job_desc = job.get("description", "")[:800]  # Reduced job description - focus on resume
    
    contact_info = ""
    if email:
        contact_info += f"\nEmail: {email}"
    if phone:
        contact_info += f"\nPhone: {phone}"
    
    prompt = (
        f"You are a professional career advisor writing a personalized cover letter that SHOWCASES THE CANDIDATE'S RESUME.\n\n"
        f"CANDIDATE'S RESUME (PRIMARY FOCUS - USE THIS EXTENSIVELY):\n"
        f"Name: {name}{contact_info}\n"
        f"Skills: {skills}\n\n"
        f"Professional Experience:\n{experience}\n\n"
        f"Education:\n{education}\n\n"
        f"JOB POSTING (SECONDARY - Use sparingly for context):\n"
        f"Position: {job_title}\n"
        f"Company: {company}\n"
        f"Brief Description: {job_desc[:400]}\n\n"
        f"INSTRUCTIONS FOR WRITING THE COVER LETTER:\n"
        f"1. DATE: Start with today's date ({datetime.now().strftime('%B %d, %Y')})\n"
        f"2. GREETING: 'Dear Hiring Manager,'\n"
        f"3. OPENING (2-3 sentences): Express interest in {job_title} at {company}. " 
        f"Immediately highlight 2-3 KEY SKILLS from the candidate's resume that make them qualified.\n"
        f"4. BODY PARAGRAPH 1 (4-5 sentences): Detail the candidate's ACTUAL EXPERIENCE from their resume. "
        f"Use SPECIFIC examples from their experience section. Talk about what they have accomplished, "
        f"what technologies they've worked with, and what impact they've made. Focus 90% on RESUME CONTENT.\n"
        f"5. BODY PARAGRAPH 2 (3-4 sentences): Showcase MORE of the candidate's SKILLS AND QUALIFICATIONS from their resume. "
        f"Mention their education if relevant. Emphasize their technical competencies and professional strengths. "
        f"Only briefly mention (1 sentence max) how these align with the company's needs.\n"
        f"6. CLOSING (2-3 sentences): Express enthusiasm for the opportunity, thank them, mention availability for interview.\n"
        f"7. SIGNATURE: 'Sincerely,' followed by {name}\n\n"
        f"CRITICAL REQUIREMENTS:\n"
        f"- The cover letter should be 80-90% about the CANDIDATE'S resume content\n"
        f"- Use SPECIFIC details from their experience and skills sections\n"
        f"- Do NOT make up any experience, skills, or achievements\n"
        f"- Only use information explicitly stated in the candidate's resume\n"
        f"- Keep job description references minimal (10-20% of content)\n"
        f"- Make the candidate sound accomplished and qualified based on THEIR OWN resume\n"
        f"- Use the candidate's actual name: {name}\n"
        f"- Professional, confident tone but grounded in actual resume facts\n"
        f"- Length: 350-450 words\n"
    )
    return prompt

def generate_cover(resume_summary: Dict, job: Dict, prefer_local_llm: bool = True) -> str:
    try:
        if prefer_local_llm:
            return generate_cover_gpt4all(resume_summary, job)
        else:
            return generate_cover_with_template(resume_summary, job)
    except Exception as e:
        print(f"Error generating cover letter: {e}")
        # Fallback to template
        try:
            return generate_cover_with_template(resume_summary, job)
        except Exception as e2:
            print(f"Error with fallback template: {e2}")
            return "Failed to generate cover letter due to technical issues."

def save_cover_letter_docx(cover_text: str, job: Dict, resume_summary: Dict, output_dir: str | None = None) -> str:
    """Save cover letter as a formatted DOCX file"""
    if output_dir is None:
        output_dir = COVER_LETTERS_DIR
    
    # Create directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Generate filename
    company = job.get("company", "Company").replace("/", "-").replace("\\", "-")
    title = job.get("title", "Position").replace("/", "-").replace("\\", "-")
    job_id = job.get("id", "unknown")
    filename = f"CoverLetter_{company}_{title}_{job_id}.docx"
    filepath = os.path.join(output_dir, filename)
    
    # Create document
    doc = Document()
    
    # Set up default paragraph formatting
    for paragraph in doc.paragraphs:
        for run in paragraph.runs:
            run.font.name = 'Times New Roman'
            run.font.size = Pt(12)
    
    # Get candidate info
    if isinstance(resume_summary, str):
        name = "[Your Name]"
        email = "[Your Email]"
        phone = "[Your Phone]"
    else:
        name = resume_summary.get("name") or "[Your Name]"
        email = resume_summary.get("email") or "[Your Email]"
        phone = resume_summary.get("phone") or "[Your Phone]"
    
    # Add header with contact info
    header_para = doc.add_paragraph()
    header_para.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    header_run = header_para.add_run(f"{name}\n")
    if email != "[Your Email]":
        header_run.add_text(f"{email}\n")
    if phone != "[Your Phone]":
        header_run.add_text(f"{phone}\n")
    header_run.font.size = Pt(11)
    
    # Add date
    date_para = doc.add_paragraph()
    date_para.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    date_run = date_para.add_run(datetime.now().strftime("%B %d, %Y"))
    date_run.font.size = Pt(11)
    
    # Add space
    doc.add_paragraph()
    
    # Add recipient info
    recipient_para = doc.add_paragraph()
    recipient_run = recipient_para.add_run(f"Hiring Manager\n{job.get('company', 'Company')}")
    recipient_run.font.size = Pt(11)
    
    # Add space
    doc.add_paragraph()
    
    # Parse and add cover letter body
    paragraphs = cover_text.split('\n\n')
    for para_text in paragraphs:
        if para_text.strip():
            # Skip date if already in header
            if datetime.now().strftime("%B %d, %Y") in para_text:
                continue
            
            para = doc.add_paragraph(para_text.strip())
            para.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            para_format = para.paragraph_format
            para_format.space_after = Pt(6)
            para_format.line_spacing = 1.15
    
    # Save document
    doc.save(filepath)
    print(f"  Saved cover letter: {filename}")
    return filepath