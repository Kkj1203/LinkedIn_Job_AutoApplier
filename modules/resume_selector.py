import os
from config.resume_map import RESUME_MAP, DEFAULT_RESUME

def select_resume(job_title: str) -> str:
    job_title = job_title.lower()

    # Sort keywords by length (important)
    sorted_keywords = sorted(RESUME_MAP.keys(), key=len, reverse=True)

    for keyword in sorted_keywords:
        if keyword in job_title:
            resume_path = RESUME_MAP[keyword]

            # ✅ Check if file exists
            if os.path.exists(resume_path):
                print(f"[Resume Selector] Matched '{keyword}' → {resume_path}")
                return resume_path
            else:
                print(f"[Resume Selector] '{resume_path}' NOT FOUND → using default")
                return DEFAULT_RESUME

    print("[Resume Selector] Using default resume")
    return DEFAULT_RESUME