from pathlib import Path
import shutil
import re

page = Path("pages/exams/quick-revision.html")
css = Path("css/quick-revision.css")
dashboard = Path("pages/exam-preparation.html")

page.parent.mkdir(parents=True, exist_ok=True)

html = r'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Quick Revision | AcedeX</title>
<link rel="stylesheet" href="../../css/style.css">
<link rel="stylesheet" href="../../css/components.css">
<link rel="stylesheet" href="../../css/library-pages.css">
<link rel="stylesheet" href="../../css/responsive.css">
<link rel="stylesheet" href="../../css/exam-preparation.css">
<link rel="stylesheet" href="../../css/exam-track-pages.css">
<link rel="stylesheet" href="../../css/quick-revision.css">
</head>
<body class="library-page exam-track-page revision-page">
<a class="exam-back-link" href="../exam-preparation.html">← Back to Exam Preparation</a>
<a class="page-back-button" href="../exam-preparation.html" aria-label="Back to exam preparation"><span class="page-back-icon">←</span><span>Back</span></a>

<header class="library-header">
<a class="library-brand" href="../../index.html">Acede<span>X</span></a>
<nav class="library-nav">
<a href="../../index.html">Dashboard</a>
<a href="../courses.html">Courses</a>
<a href="../digital-library.html">Digital Library</a>
<a href="../book-locator.html">Book Locator</a>
<a class="active" href="../exam-preparation.html">Exam Prep</a>
</nav>
</header>

<main class="library-container track-container">
<section class="track-hero revision-hero">
<div class="track-hero-content">
<span class="track-eyebrow">FAST RECALL · SMART PRACTICE</span>
<div class="track-hero-icon">⚡</div>
<h1>Quick Revision Centre</h1>
<p>Refresh important concepts, formulas, definitions and problem-solving methods through focused subject-wise revision modules.</p>
<div class="track-hero-actions">
<a href="#revision-subjects" class="track-primary-button">Start Revising ↓</a>
<a href="#revision-checklist" class="track-secondary-button">Revision Checklist</a>
</div>
</div>
<div class="track-hero-side">
<span class="hero-side-icon">📚</span>
<span class="hero-side-label">RECALL · PRACTISE<br>REINFORCE</span>
</div>
</section>

<section class="revision-intro">
<div><span class="track-section-kicker">YOUR QUICK STUDY SPACE</span>
<h2>Revise one concept at a time.</h2>
<p>Choose a subject to open its revision notes. Attempt the questions before revealing their explanations.</p></div>
<div class="revision-tags"><span>Concepts</span><span>Formulas</span><span>Examples</span><span>Practice</span></div>
</section>

<section class="track-content-section" id="revision-subjects">
<div class="track-section-heading"><div><span>01 · SUBJECT-WISE RECALL</span><h2>Revision Modules</h2><p>Open any subject to explore its quick notes and practice questions.</p></div><span class="track-heading-icon">⚡</span></div>

<details class="revision-subject" open>
<summary><span class="revision-number">01</span><span class="revision-subject-name">Engineering Mathematics</span><span class="revision-subject-meta">Functions · Calculus · Matrices</span><span class="revision-plus">＋</span></summary>
<div class="revision-body">
<h3>Functions and Limits</h3>
<ul><li>A function assigns exactly one output to each permitted input.</li><li>Domain: permitted input values; range: resulting output values.</li><li>A limit describes the value approached by a function near a point.</li><li>For polynomials, direct substitution evaluates the limit.</li></ul>
<h3>Differentiation</h3>
<ul><li>Power rule: \(\frac{d}{dx}x^n=nx^{n-1}\).</li><li>Product rule: \((uv)'=u'v+uv'\).</li><li>Quotient rule: \((u/v)'=(vu'-uv')/v^2\).</li><li>A derivative represents instantaneous rate of change.</li></ul>
<h3>Matrices</h3>
<ul><li>Matrix order is rows × columns.</li><li>Matrix addition requires equal dimensions.</li><li>For an invertible square matrix, determinant is non-zero.</li><li>Rank is the maximum number of linearly independent rows or columns.</li></ul>
<div class="revision-example"><strong>Worked example</strong><p>If \(f(x)=x^2+3x\), then \(f'(x)=2x+3\). At \(x=2\), the derivative is 7.</p></div>
<div class="revision-question"><strong>Easy · Question 1</strong><p>What is the derivative of \(x^4\)?</p><details><summary>Reveal answer</summary><p><strong>Answer: \(4x^3\).</strong> Apply the power rule.</p></details></div>
<div class="revision-question"><strong>Moderate · Question 2</strong><p>What is the determinant of an identity matrix of order 3?</p><details><summary>Reveal answer</summary><p><strong>Answer: 1.</strong> The determinant of every identity matrix is 1.</p></details></div>
</div>
</details>

<details class="revision-subject">
<summary><span class="revision-number">02</span><span class="revision-subject-name">Programming Fundamentals</span><span class="revision-subject-meta">Python · Logic · OOP</span><span class="revision-plus">＋</span></summary>
<div class="revision-body">
<h3>Core Programming Concepts</h3>
<ul><li>A variable stores a reference to a value.</li><li>Common Python types include int, float, str, bool and list.</li><li>Conditional statements control execution based on Boolean expressions.</li><li>Loops repeat a block of instructions.</li><li>A function groups reusable instructions and may return a value.</li></ul>
<h3>Object-Oriented Programming</h3>
<ul><li>Class: a blueprint for creating objects.</li><li>Object: an instance of a class.</li><li>Encapsulation groups data and methods while controlling access.</li><li>Inheritance allows a class to reuse and extend another class.</li><li>Polymorphism allows a common interface to support different implementations.</li></ul>
<div class="revision-example"><strong>Worked example</strong><p>A loop running from 1 through 5 executes five iterations. A counter can track the number of iterations.</p></div>
<div class="revision-question"><strong>Easy · Question 1</strong><p>Which Python keyword defines a function?</p><details><summary>Reveal answer</summary><p><strong>Answer: def.</strong> It introduces a function definition.</p></details></div>
<div class="revision-question"><strong>Moderate · Question 2</strong><p>Which OOP principle allows a child class to reuse parent-class features?</p><details><summary>Reveal answer</summary><p><strong>Answer: Inheritance.</strong> A derived class can extend an existing class.</p></details></div>
</div>
</details>

<details class="revision-subject">
<summary><span class="revision-number">03</span><span class="revision-subject-name">Data Structures and Algorithms</span><span class="revision-subject-meta">Arrays · Searching · Stacks</span><span class="revision-plus">＋</span></summary>
<div class="revision-body">
<h3>Complexity and Searching</h3>
<ul><li>O(1): constant time.</li><li>O(log n): logarithmic growth.</li><li>O(n): linear growth.</li><li>O(n log n): common efficient sorting complexity.</li><li>O(n²): often appears in two nested loops.</li><li>Binary search requires sorted input and runs in O(log n) time.</li></ul>
<h3>Linear Data Structures</h3>
<ul><li>Array: indexed collection of elements.</li><li>Stack: follows LIFO (Last In, First Out).</li><li>Queue: follows FIFO (First In, First Out).</li><li>Linked list: nodes connected through references.</li><li>Push inserts into a stack; pop removes its top element.</li></ul>
<div class="revision-example"><strong>Worked example</strong><p>For a stack receiving A, B and C in that order, the first item removed is C because the stack follows LIFO.</p></div>
<div class="revision-question"><strong>Easy · Question 1</strong><p>Which data structure follows FIFO?</p><details><summary>Reveal answer</summary><p><strong>Answer: Queue.</strong> The earliest inserted element is removed first.</p></details></div>
<div class="revision-question"><strong>Moderate · Question 2</strong><p>What is the worst-case time complexity of linear search?</p><details><summary>Reveal answer</summary><p><strong>Answer: O(n).</strong> It may inspect every element.</p></details></div>
</div>
</details>

<details class="revision-subject">
<summary><span class="revision-number">04</span><span class="revision-subject-name">Database Management Systems</span><span class="revision-subject-meta">SQL · Keys · Normalisation</span><span class="revision-plus">＋</span></summary>
<div class="revision-body">
<h3>Database Fundamentals</h3>
<ul><li>A database organises information for storage and retrieval.</li><li>A primary key uniquely identifies each row.</li><li>A foreign key references a key in another table.</li><li>Candidate keys are minimal sets of attributes that uniquely identify rows.</li></ul>
<h3>SQL and Normalisation</h3>
<ul><li>SELECT retrieves data; INSERT adds rows; UPDATE modifies rows; DELETE removes rows.</li><li>WHERE filters rows; ORDER BY sorts results.</li><li>GROUP BY groups rows for aggregate calculations.</li><li>1NF requires atomic values and no repeating groups.</li><li>Normalisation helps reduce redundancy and update anomalies.</li></ul>
<div class="revision-example"><strong>Worked example</strong><p><code>SELECT name FROM Students WHERE marks &gt; 80;</code> retrieves names of students whose marks exceed 80.</p></div>
<div class="revision-question"><strong>Easy · Question 1</strong><p>Which SQL clause filters rows?</p><details><summary>Reveal answer</summary><p><strong>Answer: WHERE.</strong> It applies a condition to selected rows.</p></details></div>
<div class="revision-question"><strong>Moderate · Question 2</strong><p>Which key uniquely identifies a record in a table?</p><details><summary>Reveal answer</summary><p><strong>Answer: Primary key.</strong> Its values must be unique and non-null.</p></details></div>
</div>
</details>

<details class="revision-subject">
<summary><span class="revision-number">05</span><span class="revision-subject-name">Operating Systems</span><span class="revision-subject-meta">Processes · Memory · Scheduling</span><span class="revision-plus">＋</span></summary>
<div class="revision-body">
<h3>Processes and Threads</h3>
<ul><li>A process is a program in execution.</li><li>A thread is a unit of execution within a process.</li><li>Context switching changes the CPU from one execution context to another.</li><li>Scheduling decides which ready process receives CPU time.</li></ul>
<h3>Memory and Deadlocks</h3>
<ul><li>RAM provides working storage for active programs.</li><li>Virtual memory gives processes an abstraction of a larger address space.</li><li>Paging divides memory into fixed-size pages and frames.</li><li>Deadlock involves processes waiting indefinitely for resources.</li><li>The four necessary deadlock conditions are mutual exclusion, hold and wait, no preemption and circular wait.</li></ul>
<div class="revision-example"><strong>Worked example</strong><p>Round Robin scheduling gives each ready process a time slice before moving to the next process.</p></div>
<div class="revision-question"><strong>Easy · Question 1</strong><p>What is a program in execution called?</p><details><summary>Reveal answer</summary><p><strong>Answer: Process.</strong></p></details></div>
<div class="revision-question"><strong>Moderate · Question 2</strong><p>Which scheduling method uses a time quantum?</p><details><summary>Reveal answer</summary><p><strong>Answer: Round Robin.</strong> Each process receives a fixed time slice.</p></details></div>
</div>
</details>

<details class="revision-subject">
<summary><span class="revision-number">06</span><span class="revision-subject-name">Computer Networks</span><span class="revision-subject-meta">OSI · TCP/IP · Protocols</span><span class="revision-plus">＋</span></summary>
<div class="revision-body">
<h3>Network Models</h3>
<ul><li>OSI has seven layers: Physical, Data Link, Network, Transport, Session, Presentation and Application.</li><li>TCP provides reliable, connection-oriented transport.</li><li>UDP provides connectionless transport with lower overhead.</li><li>IP handles logical addressing and packet routing.</li></ul>
<h3>Common Protocols</h3>
<ul><li>HTTP/HTTPS: web communication.</li><li>DNS: translates domain names into IP addresses.</li><li>DHCP: assigns network configuration automatically.</li><li>SMTP: sends email.</li><li>FTP: transfers files.</li></ul>
<div class="revision-example"><strong>Worked example</strong><p>When a user enters a domain name, DNS helps find its corresponding IP address before the device communicates with the destination.</p></div>
<div class="revision-question"><strong>Easy · Question 1</strong><p>How many layers are in the OSI model?</p><details><summary>Reveal answer</summary><p><strong>Answer: Seven.</strong></p></details></div>
<div class="revision-question"><strong>Moderate · Question 2</strong><p>Which protocol translates domain names into IP addresses?</p><details><summary>Reveal answer</summary><p><strong>Answer: DNS.</strong> It provides domain-name resolution.</p></details></div>
</div>
</details>
</section>

<section class="track-content-section" id="revision-checklist">
<div class="track-section-heading"><div><span>02 · BEFORE YOU FINISH</span><h2>Revision Checklist</h2><p>Use this checklist to organise an effective revision session.</p></div><span class="track-heading-icon">✓</span></div>
<div class="revision-checklist">
<label><input type="checkbox"> Review the key definitions and concepts.</label>
<label><input type="checkbox"> Revise important formulas and rules.</label>
<label><input type="checkbox"> Work through at least one solved example.</label>
<label><input type="checkbox"> Attempt practice questions before revealing answers.</label>
<label><input type="checkbox"> Revisit topics that need more practice.</label>
<label><input type="checkbox"> Check the latest official syllabus and exam instructions.</label>
</div>
</section>

<div class="track-notice"><strong>Academic content note:</strong> These are foundational revision examples, not an official syllabus for every LPU programme or competitive examination. Match material to the relevant course, semester and current examination requirements.</div>
</main>
<footer class="library-footer"><p>© AcedeX · Learn, revise and move forward.</p></footer>
</body>
</html>
'''

styles = r'''
/* Quick Revision */
.revision-page { --revision-accent: #b56a16; --revision-soft: #fff4df; }
.revision-hero { background: linear-gradient(120deg, #fff0d5, #fff9ed 58%, #f8e5c4); }
.revision-hero .track-hero-icon, .revision-hero .hero-side-icon { color: #a85d0c; }
.revision-intro { display:flex; justify-content:space-between; align-items:center; gap:24px; margin:30px 0; padding:26px; border:1px solid #ead8b9; border-radius:18px; background:#fffaf1; }
.revision-intro h2 { margin:8px 0; }
.revision-tags { display:flex; flex-wrap:wrap; gap:8px; }
.revision-tags span { padding:8px 12px; border-radius:20px; background:#f8e8cb; color:#805016; font-weight:700; font-size:.85rem; }
.revision-subject { margin:16px 0; border:1px solid #ead7b8; border-radius:16px; background:#fff; overflow:hidden; box-shadow:0 5px 18px rgba(95,65,25,.05); }
.revision-subject > summary { display:flex; align-items:center; gap:16px; padding:20px 22px; cursor:pointer; list-style:none; }
.revision-subject > summary::-webkit-details-marker { display:none; }
.revision-number { display:grid; place-items:center; min-width:42px; height:42px; border-radius:12px; background:#fff0d5; color:#96540c; font-weight:800; }
.revision-subject-name { color:#352b20; font-weight:800; font-size:1.05rem; }
.revision-subject-meta { margin-left:auto; color:#8b7962; font-size:.85rem; }
.revision-plus { color:#a85d0c; font-size:1.4rem; font-weight:700; }
.revision-subject[open] > summary { background:#fff7e9; border-bottom:1px solid #f0dfc4; }
.revision-subject[open] .revision-plus { transform:rotate(45deg); }
.revision-body { padding:24px; color:#51483d; line-height:1.75; }
.revision-body h3 { margin:18px 0 8px; color:#79490f; }
.revision-body ul { padding-left:24px; }
.revision-body li { margin:5px 0; }
.revision-example, .revision-question { margin:18px 0; padding:17px 19px; border-radius:12px; background:#fff8eb; border-left:4px solid #d49a43; }
.revision-example p, .revision-question p { margin:7px 0; }
.revision-question { background:#f7f7fb; border-left-color:#8b83b9; }
.revision-question details { margin-top:10px; }
.revision-question details summary { cursor:pointer; color:#594c91; font-weight:700; }
.revision-question details p { padding:10px; background:#fff; border-radius:8px; }
.revision-checklist { display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:12px; }
.revision-checklist label { display:flex; gap:12px; align-items:flex-start; padding:16px; border:1px solid #eadfcf; border-radius:12px; background:#fffaf3; line-height:1.5; }
.revision-checklist input { margin-top:4px; accent-color:#b56a16; }
@media(max-width:700px) {
 .revision-intro { display:block; }
 .revision-tags { margin-top:18px; }
 .revision-subject > summary { flex-wrap:wrap; gap:10px; padding:16px; }
 .revision-subject-meta { width:100%; margin-left:52px; }
 .revision-plus { margin-left:auto; }
 .revision-body { padding:17px; }
 .revision-checklist { grid-template-columns:1fr; }
}
'''

if page.exists():
    shutil.copy2(page, "quick-revision-before-update.html")
page.write_text(html, encoding="utf-8")
if css.exists():
    shutil.copy2(css, "quick-revision-before-update.css")
css.write_text(styles, encoding="utf-8")

source = dashboard.read_text(encoding="utf-8")
shutil.copy2(dashboard, "exam-preparation-before-revision-link.html")
updated, count = re.subn(
    r'href="exams/semester-preparation\.html"(?=[^>]*data-exam-category="revision")',
    'href="exams/quick-revision.html"',
    source,
    count=1
)
if count != 1:
    raise SystemExit("Could not safely locate the Quick Revision card link. Page created; dashboard unchanged.")
dashboard.write_text(updated, encoding="utf-8")

print("Created pages/exams/quick-revision.html")
print("Created css/quick-revision.css")
print("Connected the Quick Revision dashboard card.")
