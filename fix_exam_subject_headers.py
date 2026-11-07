from pathlib import Path
import re
import shutil

files = list(Path("pages/exams").glob("*-preparation.html"))
backup = Path("backup_exam_accordion_fix")
backup.mkdir(exist_ok=True)

pattern = re.compile(
    r'(<details class="exam-subject-section\s+exam-subject-accordion">)'
    r'(.*?)'
    r'(<summary class="exam-subject-summary">.*?</summary>)',
    re.DOTALL
)

for path in files:
    original = path.read_text(encoding="utf-8")
    shutil.copy2(path, backup / path.name)

    updated, count = pattern.subn(
        lambda m: m.group(1) + "\n" + m.group(3) + m.group(2),
        original
    )

    path.write_text(updated, encoding="utf-8")
    print(f"{path.name}: fixed {count} subject headers")

print("\nFinished. Backup saved in backup_exam_accordion_fix.")
