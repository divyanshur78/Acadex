from pathlib import Path
import re
import html

root = Path(".")
special_dir = root / "pages" / "specialisations"
semester_dir = root / "pages" / "semesters"
css_file = root / "css" / "semester-pages.css"

fields = {
    "computer-science-it": ("Computer Science & IT", [
        ("artificial-intelligence-machine-learning", "Artificial Intelligence & Machine Learning", "🤖"),
        ("data-science-analytics", "Data Science & Analytics", "📊"),
        ("cyber-security", "Cyber Security", "🔐"),
        ("software-engineering", "Software Engineering", "💻"),
        ("cloud-computing", "Cloud Computing", "☁️"),
        ("internet-of-things", "Internet of Things", "🌐"),
    ]),
    "engineering-technology": ("Engineering & Technology", [
        ("mechanical-engineering", "Mechanical Engineering", "⚙️"),
        ("civil-engineering", "Civil Engineering", "🏗️"),
        ("electrical-engineering", "Electrical Engineering", "⚡"),
        ("electronics-communication", "Electronics & Communication", "📡"),
        ("mechatronics-robotics", "Mechatronics & Robotics", "🦾"),
        ("automotive-manufacturing", "Automotive & Manufacturing", "🚗"),
    ]),
    "management-commerce": ("Management & Commerce", [
        ("finance-accounting", "Finance & Accounting", "💰"),
        ("marketing-management", "Marketing Management", "📣"),
        ("human-resource-management", "Human Resource Management", "👥"),
        ("business-analytics", "Business Analytics", "📈"),
        ("international-business", "International Business", "🌍"),
        ("entrepreneurship", "Entrepreneurship", "🚀"),
    ]),
    "pharmaceutical-sciences": ("Pharmaceutical Sciences", [
        ("pharmaceutics", "Pharmaceutics", "💊"),
        ("pharmacology", "Pharmacology", "🧬"),
        ("pharmaceutical-chemistry", "Pharmaceutical Chemistry", "⚗️"),
        ("pharmacognosy", "Pharmacognosy", "🌿"),
        ("quality-assurance", "Quality Assurance", "🔬"),
        ("clinical-research", "Clinical Research", "🧪"),
    ]),
    "agriculture": ("Agriculture", [
        ("agronomy", "Agronomy", "🌾"),
        ("horticulture", "Horticulture", "🌻"),
        ("soil-science", "Soil Science", "🪴"),
        ("plant-breeding-genetics", "Plant Breeding & Genetics", "🧬"),
        ("agricultural-economics", "Agricultural Economics", "🚜"),
        ("agricultural-engineering", "Agricultural Engineering", "🌱"),
    ]),
    "law": ("Law", [
        ("constitutional-law", "Constitutional Law", "⚖️"),
        ("criminal-law", "Criminal Law", "🔍"),
        ("corporate-commercial-law", "Corporate & Commercial Law", "🏛️"),
        ("intellectual-property-law", "Intellectual Property Law", "©️"),
        ("environmental-law", "Environmental Law", "🌳"),
        ("international-law", "International Law", "🌐"),
    ]),
}

resource_items = [
    ("Subject Notes", "📘", "Unit-wise notes, summaries, lecture material and presentations.", "semester-notes"),
    ("Books & References", "📚", "Recommended textbooks, reference material and reading lists.", "semester-books"),
    ("Assignments & Practice", "✍️", "Assignments, worksheets, case studies and practice sets.", "semester-assignments"),
    ("Practical Files", "🧪", "Laboratory manuals, practical files and experiment records.", "semester-practicals"),
    ("Projects", "🛠️", "Mini-projects, project guidelines, reports and supporting material.", "semester-projects"),
    ("Previous-Year Questions", "📄", "Subject-wise previous-year question papers and solutions.", "semester-pyqs"),
    ("Revision & Assessments", "🎯", "Revision sheets, important questions and assessment material.", "semester-revision"),
]

def make_resource_card(title, icon, description, key):
    return f"""
            <article class="semester-resource-card" data-resource-category="{key}">
                <span class="semester-resource-icon" aria-hidden="true">{icon}</span>
                <h3>{html.escape(title)}</h3>
                <p>{html.escape(description)}</p>
                <div class="semester-resource-content" data-content-container="{key}">
                    <span class="semester-pending">Resources will be added after academic verification.</span>
                </div>
            </article>"""

total = 0

for field_slug, (field_title, specialisations) in fields.items():
    for slug, title, icon in specialisations:
        folder = semester_dir / slug
        folder.mkdir(parents=True, exist_ok=True)

        cards = []
        for number in range(1, 9):
            cards.append(f"""
                <a class="semester-directory-card"
                   href="../semesters/{slug}/semester-{number}.html"
                   data-semester-number="{number}"
                   data-specialisation-id="{slug}">
                    <span class="semester-directory-icon" aria-hidden="true">📖</span>
                    <span class="semester-directory-copy">
                        <strong>Semester {number}</strong>
                        <small>Subjects, syllabus and learning resources</small>
                    </span>
                    <span class="semester-directory-arrow" aria-hidden="true">→</span>
                </a>""")

            resource_cards = "\n".join(
                make_resource_card(*item) for item in resource_items
            )

            page = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Semester {number} learning resources for {html.escape(title)} on AcedeX.">
    <title>Semester {number} | {html.escape(title)} | AcedeX</title>
    <link rel="stylesheet" href="../../css/style.css">
    <link rel="stylesheet" href="../../css/components.css">
    <link rel="stylesheet" href="../../css/responsive.css">
    <link rel="stylesheet" href="../../css/specialisation-pages.css">
    <link rel="stylesheet" href="../../css/semester-pages.css">
</head>
<body class="semester-learning-page">
    <header class="specialisation-site-header">
        <a class="specialisation-brand" href="../../index.html">AcedeX</a>
        <nav class="specialisation-main-nav" aria-label="Main navigation">
            <a href="../../index.html">Home</a>
            <a href="../academic-fields/{field_slug}.html">Academic Fields</a>
            <a href="../digital-library.html">Digital Library</a>
            <a href="../exam-preparation.html">Exam Preparation</a>
        </nav>
    </header>

    <main class="semester-page-main"
          data-specialisation-id="{slug}"
          data-academic-field="{field_slug}"
          data-semester-number="{number}"
          data-content-container="semester-workspace">

        <nav class="semester-breadcrumb" aria-label="Breadcrumb">
            <a href="../../index.html">Home</a>
            <span aria-hidden="true">›</span>
            <a href="../academic-fields/{field_slug}.html">{html.escape(field_title)}</a>
            <span aria-hidden="true">›</span>
            <a href="../specialisations/{slug}.html">{html.escape(title)}</a>
            <span aria-hidden="true">›</span>
            <span>Semester {number}</span>
        </nav>

        <section class="semester-hero">
            <div class="semester-hero-icon" aria-hidden="true">{icon}</div>
            <div class="semester-hero-copy">
                <span class="semester-eyebrow">YOUR LEARNING WORKSPACE</span>
                <h1>Semester {number}</h1>
                <h2>{html.escape(title)}</h2>
                <p>Access your syllabus, subject-wise study material, assignments, practical files and revision resources in one place.</p>
                <div class="semester-hero-actions">
                    <a class="semester-primary-button" href="#semester-syllabus">View Syllabus</a>
                    <a class="semester-secondary-button" href="#semester-resources">Explore Resources</a>
                </div>
            </div>
        </section>

        <section class="semester-content-section" id="semester-syllabus">
            <div class="semester-section-heading">
                <span class="semester-eyebrow">OFFICIAL ACADEMIC DOCUMENT</span>
                <h2>Semester Syllabus</h2>
                <p>Find the verified syllabus document for this programme and semester.</p>
            </div>
            <article class="semester-syllabus-card"
                     data-content-container="semester-syllabus"
                     data-download-slot="syllabus-pdf">
                <div class="semester-syllabus-icon" aria-hidden="true">📑</div>
                <div class="semester-syllabus-copy">
                    <h3>Semester {number} Syllabus PDF</h3>
                    <p>The official syllabus PDF will be added after the programme curriculum has been verified.</p>
                    <span class="semester-pending">Syllabus document not uploaded yet</span>
                </div>
                <span class="semester-download-placeholder" aria-disabled="true">Download unavailable</span>
            </article>
        </section>

        <section class="semester-content-section">
            <div class="semester-section-heading">
                <span class="semester-eyebrow">SUBJECT DIRECTORY</span>
                <h2>Subjects in This Semester</h2>
                <p>Subject names and codes will be populated from the verified programme curriculum.</p>
            </div>
            <div class="semester-subject-placeholder"
                 data-content-container="semester-subjects">
                <span aria-hidden="true">▤</span>
                <h3>Subject list is being prepared</h3>
                <p>Verified subject names, course codes, credits and subject-wise resource links will appear here.</p>
            </div>
        </section>

        <section class="semester-content-section" id="semester-resources">
            <div class="semester-section-heading">
                <span class="semester-eyebrow">STUDY MATERIAL</span>
                <h2>Semester Learning Resources</h2>
                <p>Download available files directly or open a dedicated resource page when the material needs more detail.</p>
            </div>
            <div class="semester-resource-grid">
                {resource_cards}
            </div>
        </section>

        <section class="semester-bottom-navigation">
            <a href="../specialisations/{slug}.html">← Back to {html.escape(title)}</a>
            <a href="../digital-library.html">Explore Digital Library →</a>
        </section>

        <p class="semester-disclaimer">
            This is a frontend resource structure. Programme availability, semester count,
            subject lists and official syllabus documents must be verified before being
            presented as official academic information.
        </p>
    </main>
</body>
</html>
"""
            (folder / f"semester-{number}.html").write_text(page, encoding="utf-8")
            total += 1

        # Replace the empty semester directory with links to the generated pages.
        spec_file = special_dir / f"{slug}.html"
        if spec_file.exists():
            source = spec_file.read_text(encoding="utf-8")
            section = f"""<section class="specialisation-section" id="semester-directory">
            <div class="specialisation-section-heading">
                <span class="specialisation-eyebrow">SEMESTER BY SEMESTER</span>
                <h2>Explore Your Semesters</h2>
                <p>Choose a semester to access its syllabus, subjects and learning resources.</p>
            </div>
            <div class="specialisation-semester-grid" data-specialisation-semesters="{slug}" data-content-container="specialisation-semesters">
                {''.join(cards)}
            </div>
            <p class="semester-directory-note">Semester links are frontend placeholders. The available semesters will be adjusted to match each verified programme.</p>
        </section>"""
            pattern = r'<section class="specialisation-section"\s+id="semester-directory">.*?</section>'
            updated, count = re.subn(pattern, section, source, count=1, flags=re.S)
            if count:
                spec_file.write_text(updated, encoding="utf-8")

print(f"Created or refreshed {total} semester pages.")
print(f"Specialisation pages updated: {sum(1 for p in special_dir.glob('*.html'))}")
