# app.py (at project root)

from src.parse_resume import parse_resume
from src.fetch_jobs import fetch_jobs
from src.match_jobs import compute_similarity
from src.generate_cover import generate_cover, save_cover_letter_docx
from src.export_results import export_to_csv

# Import config with defaults for CI/testing
try:
    from config import DEFAULT_RESUME
except ImportError:
    DEFAULT_RESUME = "data/your_resume.pdf"

from typing import Optional, List
from datetime import datetime
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email_alert(watchlist_matches, email_config=None):
    """
    Send email alerts for company watchlist matches.
    
    To enable email alerts, create email_config.py with:
    EMAIL_ENABLED = True
    SMTP_SERVER = "smtp.gmail.com"
    SMTP_PORT = 587
    SENDER_EMAIL = "your_email@gmail.com"
    SENDER_PASSWORD = "your_app_password"
    RECIPIENT_EMAIL = "your_email@gmail.com"
    """
    try:
        if email_config is None:
            try:
                from email_config import EMAIL_ENABLED, SMTP_SERVER, SMTP_PORT, SENDER_EMAIL, SENDER_PASSWORD, RECIPIENT_EMAIL
                if not EMAIL_ENABLED:
                    print("   (Email alerts disabled in config)")
                    return
            except ImportError:
                print("   (Email config not found - create email_config.py to enable alerts)")
                return
        
        # Create email content
        subject = f"🎯 Job Alert: {len(watchlist_matches)} Watchlist Match(es) Found!"
        
        body = "Hello!\n\n"
        body += f"Your AI Job Agent found {len(watchlist_matches)} job(s) from your watchlist companies:\n\n"
        
        for idx, row in watchlist_matches.iterrows():
            body += f"📌 {row['company']}\n"
            body += f"   Position: {row['title']}\n"
            body += f"   Location: {row['location']}\n"
            body += f"   Match Score: {row['similarity']:.2%}\n"
            body += f"   URL: {row['link']}\n\n"
        
        body += "Cover letters have been generated for all matches.\n\n"
        body += "Best regards,\nYour AI Job Agent"
        
        # Send email
        msg = MIMEMultipart()
        msg['From'] = SENDER_EMAIL
        msg['To'] = RECIPIENT_EMAIL
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.send_message(msg)
        
        print(f"   ✓ Email alert sent to {RECIPIENT_EMAIL}")
        
    except Exception as e:
        print(f"   ⚠ Failed to send email alert: {e}")

def run_pipeline(resume_path: Optional[str] = None, query: Optional[str] = None, location: str = "", generate_covers: bool = True, output_csv: Optional[str] = None, company_watchlist: Optional[List[str]] = None):
    resume_path = resume_path or DEFAULT_RESUME
    print("[1/6] Parsing resume:", resume_path)
    resume_summary = parse_resume(resume_path)
    print("Found skills:", resume_summary.get("skills"))
    
    # Auto-detect job role from resume if no query provided
    if query is None:
        detected_role = resume_summary.get("target_role", "data analyst")
        query = str(detected_role) if detected_role else "data analyst"
        print(f"Auto-detected target role: {query}")
    else:
        print(f"Using provided query: {query}")
    
    # Ensure query is a string at this point
    assert query is not None, "Query must be provided or auto-detected"
    
    # Generate unique filename with timestamp if not provided
    if output_csv is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        job_type_clean = query.replace(" ", "_").replace("/", "-")
        output_csv = f"outputs/jobs_{job_type_clean}_{timestamp}.csv"
        os.makedirs("outputs", exist_ok=True)
    
    # Initialize cover letters folder variable
    cover_letters_folder = None
    
    print(f"[2/6] Fetching jobs for query: {query}")
    jobs = fetch_jobs(query, location=location, page=1)
    
    print(f"Got {len(jobs)} jobs — computing similarity...")
    enriched = compute_similarity(resume_summary.get("raw_text", ""), jobs, top_k=len(jobs))
    
    if generate_covers:
        print("[3/6] Generating cover letters for top matches (this may take time if using local LLM)…")
        # Create folder with resume name and today's date
        today_date = datetime.now().strftime("%Y-%m-%d")
        resume_name = resume_summary.get("name") or "Candidate"
        # Clean name for folder (remove special characters)
        clean_name = str(resume_name).replace(" ", "_").replace("/", "-").replace("\\", "-")
        cover_letters_folder = f"cover_letters/{clean_name}_{today_date}"
        os.makedirs(cover_letters_folder, exist_ok=True)
        
        for i, job in enumerate(enriched):
            try:
                print(f"  Generating cover letter {i+1}/{len(enriched)}...")
                # Use GPT4All for cover letter generation
                cover = generate_cover(resume_summary, job, prefer_local_llm=True)
                job["cover_letter"] = cover
                
                # Save as DOCX file in timestamped folder
                try:
                    save_cover_letter_docx(cover, job, resume_summary, output_dir=cover_letters_folder)
                except Exception as docx_error:
                    print(f"  Warning: Failed to save DOCX for {job.get('title', 'Unknown')}: {docx_error}")
                    
            except Exception as e:
                print(f"  Failed to generate cover letter for {job.get('title', 'Unknown')}: {e}")
                job["cover_letter"] = "Failed to generate cover letter."
        
        print(f"  ✓ Cover letters saved to: {cover_letters_folder}")
    else:
        print("[3/6] Skipping cover letter generation (disabled)")

    print("[5/6] Exporting results to CSV")
    df = export_to_csv(enriched, path=output_csv)

    # Check for company watchlist matches and send alerts
    if company_watchlist:
        # Fuzzy matching: check if any watchlist company name is contained in job company name or vice versa
        watchlist_matches = df[df['company'].apply(
            lambda job_company: any(
                watchlist_name.lower() in str(job_company).lower() or 
                str(job_company).lower() in watchlist_name.lower()
                for watchlist_name in company_watchlist
            )
        )]
        if len(watchlist_matches) > 0:
            print(f"\n   🎯 Sending email alerts for {len(watchlist_matches)} watchlist match(es)...")
            send_email_alert(watchlist_matches)

    print(f"[6/6] Done. Saved {df.shape[0]} jobs to CSV.")
    print(f"\n" + "="*70)
    print(f"✓ CSV saved to: {output_csv}")
    if generate_covers:
        print(f"✓ Cover letters saved to: {cover_letters_folder}")
    print("="*70)
    return df, output_csv

def get_resume_files(data_dir="data"):
    """Get all resume files from the data directory"""
    resume_extensions = ['.pdf', '.docx', '.txt']
    resume_files = []
    
    if os.path.exists(data_dir):
        for file in os.listdir(data_dir):
            if any(file.lower().endswith(ext) for ext in resume_extensions):
                resume_files.append(file)
    
    return resume_files

def select_resume(resume_files):
    """Prompt user to select a resume when multiple options are available"""
    if len(resume_files) == 0:
        print("❌ No resume files found in the data directory!")
        print("Please add your resume file to the 'data' folder and try again.")
        return None
    elif len(resume_files) == 1:
        # Automatically select the only resume
        selected_resume = resume_files[0]
        print(f"✅ Found one resume: {selected_resume}")
        return f"data/{selected_resume}"
    else:
        # Multiple resumes - prompt user to select
        print(f"📁 Found {len(resume_files)} resume files in the data directory:")
        for i, resume in enumerate(resume_files, 1):
            print(f"  {i}. {resume}")
        
        while True:
            try:
                choice = input(f"\nPlease select a resume (1-{len(resume_files)}): ")
                choice_idx = int(choice) - 1
                if 0 <= choice_idx < len(resume_files):
                    selected_resume = resume_files[choice_idx]
                    print(f"✅ Selected resume: {selected_resume}")
                    return f"data/{selected_resume}"
                else:
                    print(f"⚠️  Please enter a number between 1 and {len(resume_files)}")
            except ValueError:
                print("⚠️  Please enter a valid number")

if __name__ == "__main__":
    # Check for multiple resumes and let user select if needed
    resume_files = get_resume_files("data")
    if resume_files:
        selected_resume_path = select_resume(resume_files)
        if selected_resume_path:
            print(f"\n📄 Using resume: {selected_resume_path}\n")
            run_pipeline(resume_path=selected_resume_path)
        else:
            print("❌ No resume selected. Exiting.")
    else:
        # Fallback to default resume from config
        print(f"📄 Using default resume from config: {DEFAULT_RESUME}\n")
        run_pipeline()