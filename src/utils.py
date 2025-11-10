# src/utils.py
import re
from typing import List

def clean_text(t: str) -> str:
    if not t:
        return ""
    # Normalize whitespace, remove non-ascii weirdness
    t = t.replace('\r\n', '\n')
    t = re.sub(r'\n{2,}', '\n\n', t)
    t = re.sub(r'[ \t]+', ' ', t)
    return t.strip()

def simple_skill_extractor(text: str, skills_vocab: List[str]) -> List[str]:
    text_low = text.lower()
    found = []
    for skill in skills_vocab:
        if skill.lower() in text_low:
            found.append(skill)
    return sorted(set(found))
