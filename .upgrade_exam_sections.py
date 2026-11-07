from pathlib import Path
import re
import html

ROOT = Path(".")
PAGES = {
    "semester-preparation.html": [
        ("Engineering Mathematics", "Illustrative B.Tech CSE practice", "Foundation", 
         "Engineering Mathematics provides the mathematical tools used to model and solve computing and engineering problems. Begin with algebraic manipulation, functions, matrices and basic calculus. A matrix represents values arranged in rows and columns. Matrix operations are useful in solving simultaneous equations and representing transformations. In calculus, a derivative describes the rate at which a quantity changes, while an integral represents accumulated change.",
         "Matrix addition requires equal dimensions. Matrix multiplication is possible when the first matrix's column count equals the second matrix's row count. For a differentiable function f(x), the power rule is d(x^n)/dx = nx^(n-1). Always simplify expressions before substituting values.",
         "For A = [[1, 2], [3, 4]] and B = [[2, 0], [1, 5]], A + B = [[3, 2], [4, 9]]. For f(x) = x^3 + 2x, f'(x) = 3x^2 + 2.",
         [("Foundation", "If A is a 2 × 3 matrix and B is a 3 × 2 matrix, what is the order of AB?", ["2 × 2", "3 × 3", "2 × 3", "3 × 2"], "A", "The inner dimensions (3 and 3) match, so the product is defined. The result has the outer dimensions: 2 × 2."),
          ("Moderate", "What is the derivative of 4x^3 - 5x^2 + 7?", ["12x² - 10x", "12x² - 5x", "4x² - 10x", "12x³ - 10x"], "A", "Apply the power rule term by term. The derivative of the constant 7 is zero.")]),
        ("Programming Fundamentals", "Illustrative B.Tech CSE practice", "Foundation",
         "A program is a sequence of instructions that transforms input into output. Variables store values, data types define the kind of values stored, and operators perform computations. Control structures determine execution flow: sequence executes statements in order, selection chooses a path, and iteration repeats a block. Functions divide a program into reusable units and help reduce repetition.",
         "Use meaningful variable names, initialise values before use, and keep functions focused on one task. A conditional statement evaluates a Boolean expression. A loop should have a clear termination condition to avoid unintended infinite repetition.",
         "A loop that processes five values can use a counter starting at zero and continue while the counter is less than five. A function named calculate_total can accept values and return their sum.",
         [("Foundation", "Which control structure is used to repeat a block of instructions?", ["Selection", "Iteration", "Declaration", "Assignment"], "B", "Iteration includes loops such as for and while, which repeat instructions."),
          ("Moderate", "What is the main benefit of dividing a program into functions?", ["It removes the need for input", "It prevents all errors", "It improves reuse and organisation", "It makes every program shorter"], "C", "Functions support modularity, reuse, testing and easier maintenance.")]),
        ("Digital Logic and Computer Fundamentals", "Illustrative B.Tech CSE practice", "Foundation",
         "Digital systems represent information using binary digits, 0 and 1. A logic gate performs a Boolean operation on one or more binary inputs. AND produces 1 only when all inputs are 1; OR produces 1 when at least one input is 1; NOT reverses its input. These gates form the foundation of arithmetic circuits, memory and processor logic.",
         "Binary place values are powers of two, beginning at 2^0 on the right. Boolean expressions can be simplified using identities such as A AND 1 = A, A OR 0 = A, and NOT(NOT A) = A.",
         "The binary number 1011₂ equals 8 + 0 + 2 + 1 = 11₁₀. For inputs A=1 and B=0, AND gives 0 while OR gives 1.",
         [("Foundation", "What is the decimal value of binary 1101?", ["11", "12", "13", "14"], "C", "1101₂ = 8 + 4 + 0 + 1 = 13."),
          ("Moderate", "An AND gate outputs 1 when:", ["At least one input is 1", "All inputs are 1", "All inputs are 0", "Inputs are different"], "B", "The AND operation requires every input to be HIGH (1).")])
    ],
    "gate-preparation.html": [
        ("Engineering Mathematics", "GATE CSE illustrative practice", "Moderate",
         "Engineering Mathematics for computer science commonly includes discrete mathematics, linear algebra, calculus, probability and statistics. Discrete mathematics studies countable structures such as sets, relations, functions, graphs and logic. A relation on a set may have properties such as reflexivity, symmetry and transitivity. These properties are frequently used to classify relations and equivalence classes.",
         "For a relation to be an equivalence relation, it must be reflexive, symmetric and transitive. For independent events A and B, P(A ∩ B) = P(A)P(B). For a square matrix, a non-zero determinant implies that the matrix is invertible.",
         "On S={1,2,3}, the equality relation is reflexive, symmetric and transitive. If two independent events have probabilities 1/2 and 1/3, their joint probability is 1/6.",
         [("Moderate", "Which property is required for an equivalence relation?", ["Antisymmetry only", "Reflexivity, symmetry and transitivity", "Transitivity only", "Irreflexivity"], "B", "All three properties are required."),
          ("Advanced", "Two independent events have probabilities 0.4 and 0.5. What is the probability that both occur?", ["0.1", "0.2", "0.4", "0.9"], "B", "For independent events, multiply their probabilities: 0.4 × 0.5 = 0.2.")]),
        ("Data Structures and Algorithms", "GATE CSE illustrative practice", "Advanced",
         "An algorithm is a finite sequence of unambiguous steps used to solve a problem. Data structures organise information so operations can be performed efficiently. Arrays provide indexed access, linked lists connect nodes through references, stacks follow LIFO order, and queues follow FIFO order. Trees represent hierarchical data, while graphs represent relationships between vertices.",
         "Time complexity describes how running time grows with input size. O(1) is constant, O(log n) is logarithmic, O(n) is linear and O(n²) is quadratic. Binary search requires sorted data and repeatedly halves the search interval, giving O(log n) time.",
         "In a stack, pushing A then B means B is removed first. In binary search over 16 sorted elements, at most about four halving steps are needed to isolate a position.",
         [("Moderate", "Which data structure follows LIFO?", ["Queue", "Stack", "Tree", "Graph"], "B", "Last In, First Out is the defining behaviour of a stack."),
          ("Advanced", "What is the worst-case time complexity of binary search on a sorted array?", ["O(1)", "O(log n)", "O(n)", "O(n²)"], "B", "Each comparison halves the remaining search space.")]),
        ("Operating Systems", "GATE CSE illustrative practice", "Advanced",
         "An operating system manages hardware resources and provides services to programs. A process is a program in execution, while a thread is a unit of execution within a process. The OS schedules processes, manages memory, controls files and coordinates input/output devices. Process states commonly include new, ready, running, waiting and terminated.",
         "A context switch saves the state of one process or thread and loads another. Deadlock involves processes waiting indefinitely for resources. The four necessary deadlock conditions are mutual exclusion, hold and wait, no preemption and circular wait.",
         "If process P1 holds resource R1 while waiting for R2, and P2 holds R2 while waiting for R1, a circular wait exists and deadlock may occur.",
         [("Moderate", "Which component selects a process from the ready queue for CPU execution?", ["Compiler", "CPU scheduler", "File system", "Loader"], "B", "The short-term CPU scheduler selects the next ready process."),
          ("Advanced", "Which is NOT one of the four necessary conditions for deadlock?", ["Mutual exclusion", "Circular wait", "Preemption allowed", "Hold and wait"], "C", "The necessary condition is no preemption, not preemption allowed.")])
    ],
    "cds-preparation.html": [
        ("English", "CDS written-exam style practice", "Moderate",
         "English preparation tests comprehension, vocabulary, grammar and correct usage. Read a passage for its central idea before examining individual details. In sentence correction, identify the subject and verb first, then check tense, agreement, pronouns and modifiers. Vocabulary questions are best approached through context rather than memorising isolated meanings.",
         "A singular subject generally takes a singular verb in the present tense. Keep parallel items in the same grammatical form. In comprehension, distinguish what the passage states from what a reader merely assumes.",
         "Incorrect: She go to college every day. Correct: She goes to college every day. The singular subject 'She' takes 'goes'.",
         [("Foundation", "Choose the grammatically correct sentence.", ["He do his work.", "He does his work.", "He doing his work.", "He done his work."], "B", "The singular subject 'He' takes 'does' in the simple present tense."),
          ("Moderate", "Choose the closest meaning of 'concise'.", ["Confusing", "Brief and clear", "Uncertain", "Decorative"], "B", "Concise means expressing something clearly in few words.")]),
        ("Elementary Mathematics", "CDS written-exam style practice", "Moderate",
         "Elementary Mathematics requires accuracy in arithmetic, algebra, geometry, trigonometry and mensuration. Percentages express a quantity per hundred. Ratio compares quantities by division, while proportion states that two ratios are equal. Translate word problems into equations before calculating.",
         "Percentage = (part / whole) × 100. If a value increases by r%, multiply it by (1 + r/100). For a simple interest problem, SI = (P × R × T)/100, where P is principal, R is annual rate and T is time in years.",
         "A price of ₹800 increased by 10% becomes ₹800 × 1.10 = ₹880. Simple interest on ₹2,000 at 5% for 2 years is ₹200.",
         [("Foundation", "What is 25% of 240?", ["40", "50", "60", "80"], "C", "25% is one-fourth. 240 ÷ 4 = 60."),
          ("Moderate", "Find the simple interest on ₹1,500 at 4% per annum for 2 years.", ["₹100", "₹120", "₹140", "₹160"], "B", "SI = 1500 × 4 × 2 / 100 = ₹120.")]),
        ("General Knowledge", "CDS written-exam style practice", "Moderate",
         "General Knowledge preparation spans history, geography, polity, economics and general science. Build understanding around causes, institutions, locations and basic principles rather than relying only on isolated facts. For polity, learn the roles of constitutional bodies and the broad structure of government. For science, focus on everyday applications and foundational concepts.",
         "Separate static concepts from current affairs. Verify time-sensitive facts from reliable, recent sources before an examination. When answering a factual question, eliminate options that contradict established definitions or basic chronology.",
         "A constitution establishes the framework of government, defines institutions and distributes powers. A map-based geography question can often be approached by locating the region first and then checking its physical features.",
         [("Foundation", "Which branch of government is primarily responsible for interpreting laws?", ["Legislature", "Executive", "Judiciary", "Election Commission"], "C", "The judiciary interprets laws and adjudicates disputes."),
          ("Moderate", "Which instrument is commonly used to measure atmospheric pressure?", ["Thermometer", "Barometer", "Ammeter", "Hygrometer"], "B", "A barometer measures atmospheric pressure.")])
    ],
    "afcat-preparation.html": [
        ("English", "AFCAT exam-pattern practice", "Moderate",
         "English preparation covers comprehension, vocabulary, sentence completion, error detection and basic grammar. In comprehension, identify the author's main point, tone and supporting evidence. In sentence completion, use grammar and context together instead of selecting a word based only on familiarity.",
         "Check subject–verb agreement, tense consistency, articles, prepositions and pronoun reference. A word's meaning can change with context, so read the complete sentence before choosing a synonym or antonym.",
         "In 'The team ____ ready for the exercise', the expected verb is 'is' when team is treated as one unit. The surrounding sentence determines the correct tense and agreement.",
         [("Foundation", "Choose the correct form: 'Neither of the answers ____ correct.'", ["are", "were", "is", "have"], "C", "'Neither' is treated as singular in this construction, so 'is' is appropriate."),
          ("Moderate", "Choose the closest meaning of 'vigilant'.", ["Careless", "Watchful", "Confused", "Indifferent"], "B", "Vigilant means alert and watchful.")]),
        ("Numerical Ability", "AFCAT exam-pattern practice", "Moderate",
         "Numerical Ability focuses on arithmetic speed and reliable methods. Important areas include percentages, averages, ratios, profit and loss, time and work, speed and distance, and simple interest. Write down the known quantities and units before selecting a formula.",
         "Average = sum of observations / number of observations. Speed = distance / time. If two workers complete a job independently in a and b days, their combined daily work rate is 1/a + 1/b.",
         "A vehicle covers 150 km in 3 hours. Its average speed is 150/3 = 50 km/h. The average of 12, 18 and 24 is 54/3 = 18.",
         [("Foundation", "The average of 10, 20 and 30 is:", ["15", "20", "25", "30"], "B", "Average = (10 + 20 + 30)/3 = 20."),
          ("Moderate", "A person travels 120 km in 2.5 hours. Find the average speed.", ["40 km/h", "45 km/h", "48 km/h", "50 km/h"], "C", "Speed = 120 ÷ 2.5 = 48 km/h.")]),
        ("Reasoning and Military Aptitude", "AFCAT exam-pattern practice", "Moderate",
         "Reasoning evaluates patterns, logical relationships, spatial understanding and decision-making. Common forms include number and letter series, analogy, classification, coding-decoding, directions and figure-based reasoning. Identify the rule governing the sequence before selecting an answer.",
         "For a number series, compare consecutive differences and ratios. For direction problems, draw a simple reference: north is up, east is right, south is down and west is left. In analogy questions, state the relationship between the first pair before applying it to the second.",
         "In 3, 6, 12, 24, each term is multiplied by 2, so the next term is 48. If a person faces north and turns right, they face east.",
         [("Foundation", "Find the next number: 2, 4, 8, 16, __.", ["20", "24", "30", "32"], "D", "Each term doubles, so 16 × 2 = 32."),
          ("Moderate", "A person faces east and turns left. Which direction are they facing now?", ["North", "South", "West", "East"], "A", "A left turn from east points north.")])
    ],
    "placement-preparation.html": [
        ("Quantitative Aptitude", "Placement-test style practice", "Moderate",
         "Placement aptitude tests commonly assess arithmetic, algebra, data interpretation, ratios, percentages, averages, time and work, and speed and distance. Read the question carefully to identify what is being asked. Convert percentages and ratios into comparable quantities before calculating.",
         "For successive percentage changes, apply each change to the updated value rather than adding percentages blindly. If a value changes by +a% and then -b%, the final value is original × (1+a/100) × (1-b/100).",
         "A value of 100 increased by 20% becomes 120. A subsequent decrease of 10% gives 108, not 110.",
         [("Foundation", "A product costing ₹500 is discounted by 10%. What is the sale price?", ["₹400", "₹450", "₹475", "₹490"], "B", "10% of ₹500 is ₹50. Sale price = ₹500 - ₹50 = ₹450."),
          ("Moderate", "The average of five numbers is 18. What is their total?", ["72", "80", "90", "100"], "C", "Total = average × count = 18 × 5 = 90.")]),
        ("Data Structures and Algorithms", "Technical screening practice", "Advanced",
         "Technical screening often tests arrays, strings, linked lists, stacks, queues, trees, sorting, searching and complexity analysis. Choose a data structure based on the operations required. Arrays support direct indexed access; linked lists support flexible node insertion; stacks and queues enforce particular access orders.",
         "Binary search requires sorted input and runs in O(log n) time. Linear search checks elements sequentially and runs in O(n) time. A nested loop over n elements may lead to O(n²) time, but always analyse the actual number of iterations.",
         "To find the maximum in an unsorted array, scan each element once while maintaining the largest value seen. This takes O(n) time and O(1) extra space.",
         [("Moderate", "Which search method requires the input to be sorted?", ["Linear search", "Binary search", "Depth-first search", "Hash lookup"], "B", "Binary search relies on ordering to discard half the search interval."),
          ("Advanced", "A single loop visits each of n elements once. What is its time complexity?", ["O(1)", "O(log n)", "O(n)", "O(n²)"], "C", "The number of operations grows proportionally with n.")]),
        ("OOP, DBMS and SQL", "Technical interview practice", "Moderate",
         "Object-oriented programming organises code around objects that combine data and behaviour. Encapsulation controls access to internal state, inheritance enables specialised classes to reuse behaviour, polymorphism allows a common interface to have different implementations, and abstraction exposes essential features while hiding implementation details.",
         "A database stores structured information. A primary key uniquely identifies a row; a foreign key references a key in another table. SQL SELECT retrieves data, WHERE filters rows, GROUP BY forms groups and ORDER BY sorts results. Use joins when information is distributed across related tables.",
         "A Student table may use student_id as its primary key. An Enrolment table can store student_id as a foreign key. A query such as SELECT name FROM Student WHERE year = 1; retrieves first-year student names.",
         [("Foundation", "Which OOP concept bundles data and methods while controlling access?", ["Inheritance", "Encapsulation", "Compilation", "Iteration"], "B", "Encapsulation groups state and behaviour and controls how internal data is accessed."),
          ("Moderate", "Which SQL clause filters rows before grouping?", ["ORDER BY", "WHERE", "HAVING", "JOIN"], "B", "WHERE filters individual rows; HAVING filters groups after GROUP BY.")])
    ]
}

def build_module(item, index):
    name, label, level, notes, keypoints, example, questions = item
    qhtml = []
    for n, (difficulty, question, options, answer, explanation) in enumerate(questions, 1):
        letters = "ABCD"
        choices = "".join(
            f'<li><span class="exam-option-letter">{letters[i]}</span> {html.escape(option)}</li>'
            for i, option in enumerate(options)
        )
        qhtml.append(f"""
        <article class="exam-practice-question">
          <div class="exam-question-meta"><span>Question {n}</span><span class="exam-difficulty difficulty-{difficulty.lower()}">{difficulty}</span><span>Single correct answer</span></div>
          <h4>{html.escape(question)}</h4>
          <ol class="exam-question-options" type="A">{choices}</ol>
          <details class="exam-answer-reveal">
            <summary>View answer and explanation</summary>
            <div class="exam-answer-content"><strong>Correct answer: {answer}</strong><p>{html.escape(explanation)}</p></div>
          </details>
        </article>""")
    return f"""
    <details class="exam-subject-accordion" data-subject-module="{index}">
      <summary class="exam-subject-summary">
        <span class="exam-subject-number">{index:02d}</span>
        <span class="exam-subject-heading"><strong>{html.escape(name)}</strong><small>{html.escape(label)} · Open to study notes and practice</small></span>
        <span class="exam-subject-level">{html.escape(level)}</span>
        <span class="exam-subject-chevron" aria-hidden="true">＋</span>
      </summary>
      <div class="exam-subject-content">
        <section class="exam-topic-notes">
          <div class="exam-content-label">STUDY NOTES</div>
          <h3>Core concepts and understanding</h3>
          <p>{html.escape(notes)}</p>
          <div class="exam-key-points"><strong>Important rules and concepts</strong><p>{html.escape(keypoints)}</p></div>
          <div class="exam-worked-example"><strong>Worked example</strong><p>{html.escape(example)}</p></div>
        </section>
        <section class="exam-topic-practice">
          <div class="exam-content-label">PRACTICE ZONE</div>
          <h3>Test your understanding</h3>
          <p class="exam-practice-instruction">Attempt each question before opening its answer. These are illustrative exam-pattern questions, not official past-paper questions.</p>
          {''.join(qhtml)}
        </section>
      </div>
    </details>"""

def replace_section(path, modules):
    text = path.read_text(encoding="utf-8-sig")
    marker = "Starter Notes and Practice"
    pos = text.find(marker)
    if pos < 0:
        raise RuntimeError(f"Could not find target heading in {path}")
    starts = list(re.finditer(r"<section\\b[^>]*>", text[:pos], re.I))
    if not starts:
        raise RuntimeError(f"Could not find containing section in {path}")
    start = starts[-1].start()
    depth = 0
    end = None
    for match in re.finditer(r"</?section\\b[^>]*>", text[start:], re.I):
        token = match.group(0)
        if token.startswith("</"):
            depth -= 1
            if depth == 0:
                end = start + match.end()
                break
        else:
            depth += 1
    if end is None:
        raise RuntimeError(f"Could not locate end of target section in {path}")

    content = f"""
<section class="track-content-section exam-subject-learning" id="examSubjectLearning">
  <div class="section-heading">
    <span class="section-eyebrow">06 · LEARN AND TEST YOURSELF</span>
    <h2>Subject-wise Notes and Practice</h2>
    <p>Choose a subject to open its study material. Each subject contains explanatory notes, important concepts, worked examples and difficulty-based practice.</p>
  </div>
  <div class="exam-subject-accordion-list">
    {''.join(build_module(item, i) for i, item in enumerate(modules, 1))}
  </div>
  <p class="exam-content-disclaimer">Learning material and questions on this page are illustrative practice content. They are not represented as official LPU syllabus material or verified previous-year questions. Check the latest official examination notification and syllabus for the applicable course or exam.</p>
</section>"""
    text = text[:start] + content + text[end:]
    path.write_text(text, encoding="utf-8")
    print(f"Updated: {path}")

for filename, modules in PAGES.items():
    replace_section(ROOT / "pages" / "exams" / filename, modules)

css_path = ROOT / "css" / "exam-track-pages.css"
css = r"""

/* Subject-wise expandable learning modules */
.exam-subject-learning { margin-top: 34px; }
.exam-subject-accordion-list { display: grid; gap: 15px; margin-top: 24px; }
.exam-subject-accordion {
    overflow: hidden;
    border: 1px solid rgba(232, 112, 42, .28);
    border-radius: 17px;
    background: var(--card-bg, #fff);
    box-shadow: 0 7px 22px rgba(45, 35, 25, .055);
}
.exam-subject-summary {
    display: flex;
    align-items: center;
    gap: 15px;
    padding: 19px 21px;
    cursor: pointer;
    list-style: none;
    min-height: 82px;
}
.exam-subject-summary::-webkit-details-marker { display: none; }
.exam-subject-number {
    display: grid;
    place-items: center;
    flex: 0 0 43px;
    height: 43px;
    border-radius: 13px;
    background: #fff0e5;
    color: #c65a1b;
    font-weight: 800;
}
.exam-subject-heading { display: grid; gap: 5px; flex: 1; min-width: 0; }
.exam-subject-heading strong { font-size: 1.08rem; color: var(--text-primary, #28231f); }
.exam-subject-heading small { color: var(--text-secondary, #777); font-size: .83rem; }
.exam-subject-level {
    border-radius: 30px;
    padding: 6px 11px;
    background: #f2f3f5;
    color: #555;
    font-size: .75rem;
    font-weight: 700;
}
.exam-subject-chevron { color: #d66b2d; font-size: 1.35rem; font-weight: 700; }
.exam-subject-accordion[open] { border-color: rgba(232, 112, 42, .65); }
.exam-subject-accordion[open] .exam-subject-chevron { transform: rotate(45deg); }
.exam-subject-content {
    border-top: 1px solid rgba(120, 110, 100, .14);
    padding: 25px;
    display: grid;
    gap: 25px;
}
.exam-content-label { color: #d66b2d; font-size: .72rem; font-weight: 800; letter-spacing: .12em; }
.exam-topic-notes h3, .exam-topic-practice h3 { margin: 7px 0 12px; font-size: 1.18rem; }
.exam-topic-notes p, .exam-topic-practice p { line-height: 1.75; color: var(--text-secondary, #5e5a56); }
.exam-key-points, .exam-worked-example {
    margin-top: 15px;
    padding: 16px 18px;
    border-radius: 12px;
    background: #fff8f2;
    border-left: 4px solid #e8894e;
}
.exam-key-points strong, .exam-worked-example strong { color: #9d4d20; }
.exam-key-points p, .exam-worked-example p { margin: 7px 0 0; }
.exam-practice-instruction { margin-bottom: 15px; font-size: .9rem; }
.exam-practice-question {
    padding: 18px;
    margin-top: 13px;
    border: 1px solid rgba(120, 110, 100, .18);
    border-radius: 13px;
    background: var(--card-bg, #fff);
}
.exam-question-meta { display: flex; flex-wrap: wrap; gap: 9px; align-items: center; color: #777; font-size: .75rem; font-weight: 700; }
.exam-difficulty { padding: 4px 9px; border-radius: 20px; background: #f1f1f1; color: #555; }
.difficulty-foundation { background: #e8f5ed; color: #287344; }
.difficulty-moderate { background: #fff2dc; color: #95600d; }
.difficulty-advanced { background: #fce9e8; color: #a43e37; }
.exam-practice-question h4 { margin: 13px 0; font-size: 1rem; line-height: 1.55; }
.exam-question-options { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 9px 18px; padding-left: 0; list-style: none; }
.exam-question-options li { display: flex; align-items: flex-start; gap: 9px; padding: 10px; border-radius: 9px; background: #f8f7f5; color: var(--text-primary, #333); }
.exam-option-letter { display: inline-grid; place-items: center; flex: 0 0 23px; height: 23px; border-radius: 50%; background: #fff0e5; color: #b95720; font-size: .75rem; font-weight: 800; }
.exam-answer-reveal { margin-top: 14px; border-top: 1px solid rgba(120, 110, 100, .15); padding-top: 12px; }
.exam-answer-reveal summary { cursor: pointer; color: #bd5d25; font-weight: 750; font-size: .9rem; }
.exam-answer-content { margin-top: 10px; padding: 13px 15px; border-radius: 10px; background: #edf7ef; color: #285d37; }
.exam-answer-content p { margin: 6px 0 0; color: #365b40; }
.exam-content-disclaimer { margin-top: 20px; font-size: .82rem; line-height: 1.65; color: var(--text-secondary, #777); }
@media (max-width: 650px) {
    .exam-subject-summary { gap: 10px; padding: 15px 13px; }
    .exam-subject-number { flex-basis: 36px; height: 36px; }
    .exam-subject-heading strong { font-size: .96rem; }
    .exam-subject-heading small { font-size: .75rem; }
    .exam-subject-level { display: none; }
    .exam-subject-content { padding: 17px 13px; }
    .exam-question-options { grid-template-columns: 1fr; }
}
"""
existing = css_path.read_text(encoding="utf-8-sig")
if "Subject-wise expandable learning modules" not in existing:
    css_path.write_text(existing + "\n" + css, encoding="utf-8")
    print(f"Added styles: {css_path}")
else:
    print("Styles already present; left unchanged.")
