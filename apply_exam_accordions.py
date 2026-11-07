from pathlib import Path
import re
import shutil

files = [
    Path("pages/exams/semester-preparation.html"),
    Path("pages/exams/gate-preparation.html"),
    Path("pages/exams/cds-preparation.html"),
    Path("pages/exams/afcat-preparation.html"),
    Path("pages/exams/placement-preparation.html"),
]

backup = Path("backup_exam_accordions")
backup.mkdir(exist_ok=True)

for path in files:
    html = path.read_text(encoding="utf-8")
    shutil.copy2(path, backup / path.name)

    pattern = re.compile(
        r'(<section class="exam-subject-section">)(.*?)(</section>)',
        re.DOTALL
    )

    def convert(match):
        content = match.group(2)

        heading = re.search(r'<h3>(.*?)</h3>', content, re.DOTALL)
        if not heading:
            raise RuntimeError(f"Subject heading missing in {path}")

        title = heading.group(1).strip()
        summary = (
            '<summary class="exam-subject-summary">'
            f'<span class="exam-subject-title">{title}</span>'
            '<span class="exam-subject-hint">VIEW TOPICS</span>'
            '<span class="exam-subject-chevron" aria-hidden="true">＋</span>'
            '</summary>'
        )

        content = content[:heading.start()] + summary + content[heading.end():]
        return (
            '<details class="exam-subject-section exam-subject-accordion">'
            + content +
            '</details>'
        )

    updated, count = pattern.subn(convert, html)

    if count == 0:
        raise RuntimeError(f"No subject sections found in {path}")

    path.write_text(updated, encoding="utf-8")
    print(f"{path}: converted {count} subject sections")

css_path = Path("css/exam-track-pages.css")
css = css_path.read_text(encoding="utf-8")

marker = "/* Subject accordion layout */"

if marker not in css:
    css += """

/* Subject accordion layout */
.exam-subject-accordion {
    display: block;
    overflow: hidden;
    margin: 22px 0;
    border: 1px solid var(--track-border, #e4e7ec);
    border-radius: 16px;
    background: var(--track-card, #fff);
}

.exam-subject-accordion > .exam-subject-summary {
    display: flex;
    align-items: center;
    gap: 14px;
    padding: 20px 22px;
    cursor: pointer;
    list-style: none;
    background: var(--track-surface, #f8fafc);
}

.exam-subject-accordion > .exam-subject-summary::-webkit-details-marker {
    display: none;
}

.exam-subject-title {
    flex: 1;
    font-size: 1.12rem;
    font-weight: 800;
    color: var(--track-heading, #172033);
}

.exam-subject-hint {
    font-size: 0.7rem;
    font-weight: 700;
    letter-spacing: 0.08em;
    color: var(--track-muted, #667085);
}

.exam-subject-chevron {
    display: grid;
    place-items: center;
    width: 30px;
    height: 30px;
    border-radius: 50%;
    background: var(--track-accent-soft, #fff0e5);
    color: var(--track-accent, #e87524);
    font-size: 1.2rem;
    transition: transform 0.2s ease;
}

.exam-subject-accordion[open] > .exam-subject-summary {
    border-bottom: 1px solid var(--track-border, #e4e7ec);
}

.exam-subject-accordion[open] .exam-subject-chevron {
    transform: rotate(45deg);
}

.exam-subject-accordion > :not(summary) {
    margin-left: 22px;
    margin-right: 22px;
}

.exam-subject-accordion > .exam-subject-summary + h4,
.exam-subject-accordion > .exam-subject-summary + details {
    margin-top: 22px;
}

.exam-subject-accordion > .exam-practice-area {
    margin-bottom: 22px;
}

@media (max-width: 600px) {
    .exam-subject-accordion > .exam-subject-summary {
        padding: 16px;
        gap: 9px;
    }

    .exam-subject-title {
        font-size: 1rem;
    }

    .exam-subject-hint {
        font-size: 0.6rem;
    }

    .exam-subject-accordion > :not(summary) {
        margin-left: 14px;
        margin-right: 14px;
    }
}
"""
    css_path.write_text(css, encoding="utf-8")
    print("Accordion CSS added.")
else:
    print("Accordion CSS already exists; left unchanged.")

print("Finished. Original HTML backups are in backup_exam_accordions.")
