from pathlib import Path
import shutil
import re

pages = [
    "semester-preparation.html",
    "cds-preparation.html",
    "afcat-preparation.html",
    "placement-preparation.html"
]

backup = Path("backup_exam_navigation")
backup.mkdir(exist_ok=True)

for name in pages:
    page = Path("pages/exams") / name
    html = page.read_text(encoding="utf-8")

    if 'class="exam-back-link"' in html:
        print(f"{name}: already has back button")
        continue

    shutil.copy2(page, backup / name)

    updated, count = re.subn(
        r'(<body\b[^>]*>)',
        r'\1\n<a class="exam-back-link" href="../exam-preparation.html">← Back to Exam Preparation</a>',
        html,
        count=1,
        flags=re.IGNORECASE
    )

    if count:
        page.write_text(updated, encoding="utf-8")
        print(f"{name}: back button added")
    else:
        print(f"{name}: body tag not found; skipped")

print("Navigation update finished.")
