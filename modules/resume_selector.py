import os
from config.resume_map import RESUME_MAP, DEFAULT_RESUME

def select_resume(job_title: str) -> str:
    job_title = job_title.lower()

    sorted_keywords = sorted(RESUME_MAP.keys(), key=len, reverse=True)

    for keyword in sorted_keywords:
        if keyword in job_title:
            resume_path = RESUME_MAP[keyword]

            # Fix folder name just in case
            resume_path = resume_path.replace("all resumes", "all_resumes")

            # Convert to absolute path
            resume_path = os.path.abspath(resume_path)

            # ✅ If resume exists → use it
            if os.path.exists(resume_path):
                print(f"[Resume Selector] Using role-based resume → {resume_path}")
                return resume_path

            # ❌ If not → fallback
            else:
                print(f"[Resume Selector] {resume_path} NOT FOUND → switching to default")
                break  # important: don't keep looping

    # ✅ ALWAYS fallback safely
    default_path = DEFAULT_RESUME.replace("all resumes", "all_resumes")
    default_path = os.path.abspath(default_path)

    print(f"[Resume Selector] Using default resume → {default_path}")
    return default_path