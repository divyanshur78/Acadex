from pathlib import Path
import shutil
import re

page = Path("pages/exams/gate-preparation.html")
css = Path("css/exam-track-pages.css")

shutil.copy2(page, "gate-preparation-before-backup.html")
shutil.copy2(css, "exam-track-pages-before-backup.css")

html = page.read_text(encoding="utf-8")

if 'class="exam-back-link"' not in html:
    html, count = re.subn(
        r'(<body\b[^>]*>)',
        r'\1\n<a class="exam-back-link" href="../exam-preparation.html">← Back to Exam Preparation</a>',
        html,
        count=1,
        flags=re.IGNORECASE
    )
    if not count:
        raise SystemExit("Could not find the body tag. No changes made.")
    page.write_text(html, encoding="utf-8")

styles = css.read_text(encoding="utf-8")

if "/* Exam page back navigation */" not in styles:
    styles += """

/* Exam page back navigation */
.exam-back-link {
    display: inline-flex;
    align-items: center;
    gap: 9px;
    margin: 22px 5% 10px;
    padding: 11px 18px;
    border: 1px solid #d8c9f5;
    border-radius: 12px;
    background: #f1eaff;
    color: #6541a5;
    font-weight: 700;
    text-decoration: none;
    transition: background 0.2s ease, transform 0.2s ease;
}

.exam-back-link:hover {
    background: #e5d8ff;
    transform: translateX(-3px);
}
"""
    css.write_text(styles, encoding="utf-8")

print("GATE back navigation added.")
