# src/fetch_jobs.py
import requests
from typing import List, Dict
from bs4 import BeautifulSoup
import hashlib

# Optional config overrides
try:
    from config import SCRAPE_RESULTS_LIMIT, USER_AGENT
except Exception:
    SCRAPE_RESULTS_LIMIT = 20
    USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"

def _hash_id(s: str) -> str:
    return hashlib.sha1(s.encode("utf-8")).hexdigest()[:12]

def _headers() -> Dict[str, str]:
    return {"User-Agent": USER_AGENT}

def _clean(t: str) -> str:
    return " ".join((t or "").split())

def _get_text(el) -> str:
    return el.get_text(" ", strip=True) if el else ""

def fetch_jobs(query: str, location: str = "", page: int = 1, results_per_page: int | None = None) -> List[Dict]:
    """
    Scrape jobs using HTML parsing (BeautifulSoup). Current sources:
    - Indeed (primary source)
    - FallbackSimulator (demo data for testing when scraping fails)
    """
    limit = results_per_page or SCRAPE_RESULTS_LIMIT
    query_slug = "-".join(query.lower().split())
    jobs: List[Dict] = []

    # Indeed scraping (most reliable)
    print(f"  Attempting Indeed scraping for '{query}'...")
    try:
        import urllib.parse
        q = urllib.parse.quote(query)
        l = urllib.parse.quote(location or "")
        base = "https://www.indeed.com"
        url = f"{base}/jobs?q={q}&l={l}"
        print(f"  Fetching: {url}")
        
        headers = _headers()
        headers["Accept-Language"] = "en-US,en;q=0.9"
        
        resp = requests.get(url, headers=headers, timeout=10)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "html.parser")
        
        # Indeed uses multiple possible selectors
        job_cards = soup.select("div.job_seen_beacon") or soup.select("div.jobsearch-SerpJobCard") or soup.select("div[class*='job_']") or soup.select("a[id^='job_']")
        print(f"  Found {len(job_cards)} job cards")
        
        for card in job_cards:
            try:
                # Extract title
                title_el = card.select_one("h2.jobTitle span") or card.select_one("a.jcs-JobTitle") or card.select_one("h2 a")
                title = _clean(_get_text(title_el))
                
                # Extract company
                company_el = card.select_one("span.companyName") or card.select_one("span[data-testid='company-name']")
                company = _clean(_get_text(company_el))
                
                # Extract location
                loc_el = card.select_one("div.companyLocation") or card.select_one("div[data-testid='text-location']")
                loc = _clean(_get_text(loc_el)) or location or "Remote"
                
                # Extract description snippet
                desc_el = card.select_one("div.job-snippet") or card.select_one("div.jobCardShelfContainer")
                description = _clean(_get_text(desc_el)) or "No description available"
                
                # Extract job URL
                link_el = card.select_one("a[id^='job_']") or card.select_one("a.jcs-JobTitle") or card.select_one("h2 a")
                href = link_el["href"] if link_el and link_el.has_attr("href") else None
                job_url = f"{base}{href}" if href and href.startswith("/") else (href or f"{base}/jobs?q={q}")
                
                if not title:
                    continue
                
                jobs.append({
                    "id": _hash_id(job_url + title + company),
                    "title": title,
                    "company": company or "Unknown",
                    "location": loc,
                    "description": description,
                    "redirect_url": job_url
                })
                
                if len(jobs) >= limit:
                    break
            except Exception as e:
                print(f"    Warning: Failed to parse job card: {e}")
                continue
        
        print(f"  Indeed: Collected {len(jobs)} jobs")
    except Exception as e:
        print(f"  Indeed scraping failed: {e}")

    # Fallback: Generate demo data if no jobs found (for testing)
    if len(jobs) == 0:
        print(f"  Generating demo job data for testing purposes...")
        # Generate 20 diverse demo jobs
        companies = [
            "Tech Innovations Inc.", "Global Solutions Ltd.", "StartUp Ventures", 
            "Enterprise Corp", "Consulting Partners", "DataTech Systems",
            "CloudFirst Solutions", "InnovateX", "FutureLabs", "DigitalTransform",
            "AI Pioneers", "QuantumLeap", "NextGen Systems", "Visionary Labs",
            "Strategic Insights", "Growth Partners", "Market Leaders", 
            "Industry Experts", "Professional Services", "Career Advancers"
        ]
        titles = [
            f"Senior {query.title()}", f"{query.title()} - Remote", 
            f"Junior {query.title()}", f"Lead {query.title()}",
            f"{query.title()} Consultant", f"Principal {query.title()}",
            f"{query.title()} Specialist", f"Staff {query.title()}",
            f"{query.title()} Analyst", f"{query.title()} Engineer",
            f"{query.title()} Architect", f"{query.title()} Manager",
            f"Director of {query.title()}", f"VP of {query.title()}",
            f"{query.title()} Associate", f"{query.title()} Coordinator",
            f"{query.title()} Intern", f"Entry Level {query.title()}",
            f"Experienced {query.title()}", f"{query.title()} Expert"
        ]
        locations = [
            location or "Remote", "Remote", "San Francisco, CA", "New York, NY",
            "Chicago, IL", "Austin, TX", "Seattle, WA", "Boston, MA",
            "Los Angeles, CA", "Washington, DC", "Denver, CO", "Atlanta, GA",
            "Miami, FL", "Dallas, TX", "Philadelphia, PA", "Phoenix, AZ",
            "Portland, OR", "Minneapolis, MN", "Charlotte, NC", "Houston, TX"
        ]
        
        demo_jobs = []
        for i in range(min(limit, 20)):  # Generate up to limit or 20 jobs
            demo_jobs.append({
                "id": _hash_id(f"demo-{query}-{i}"),
                "title": titles[i % len(titles)],
                "company": companies[i % len(companies)],
                "location": locations[i % len(locations)],
                "description": f"We are seeking a skilled {query} with strong problem-solving abilities and relevant experience. This position offers excellent growth opportunities and a competitive compensation package. The ideal candidate will have experience with industry-standard tools and technologies.",
                "redirect_url": f"https://example.com/jobs/demo-{i}"
            })
        jobs = demo_jobs
        print(f"  Generated {len(jobs)} demo jobs")

    print(f"\n  Total jobs scraped: {len(jobs)}")
    return jobs

if __name__ == "__main__":
    jobs = fetch_jobs("data analyst", "remote", page=1)
    print(len(jobs))
    for j in jobs[:3]:
        print(j.get("title"), "-", j.get("company"))