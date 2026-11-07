from pathlib import Path
import re
from html import escape

ROOT = Path(__file__).resolve().parent
PAGES = ROOT / "pages" / "exams"

def topic(title, level, concepts, formulas, example, questions):
    qhtml = ""
    for i, (difficulty, question, options, answer, explanation) in enumerate(questions, 1):
        choices = "".join(
            f"<li><strong>{chr(65+j)}.</strong> {escape(option)}</li>"
            for j, option in enumerate(options)
        )
        qhtml += f"""
        <article class="exam-question-card">
            <span class="exam-level exam-level-{difficulty.lower()}">{difficulty}</span>
            <h4>Question {i}: {escape(question)}</h4>
            <ol class="exam-question-options" type="A">{choices}</ol>
            <details class="exam-answer">
                <summary>Reveal answer and explanation</summary>
                <div><strong>Answer: {escape(answer)}</strong>
                <p>{escape(explanation)}</p></div>
            </details>
        </article>"""

    return f"""
    <article class="exam-topic-card">
        <div class="exam-topic-heading">
            <div><span class="exam-topic-label">{level}</span>
            <h4>{escape(title)}</h4></div>
        </div>
        <details class="exam-notes" open>
            <summary>Detailed concept notes</summary>
            <div class="exam-notes-body">{concepts}</div>
        </details>
        <details class="exam-formula">
            <summary>Important formulas and quick reference</summary>
            <div class="exam-notes-body">{formulas}</div>
        </details>
        <details class="exam-solved">
            <summary>Worked example</summary>
            <div class="exam-notes-body">{example}</div>
        </details>
        <div class="exam-practice-area">
            <h5>Topic-wise practice</h5>
            <p>Attempt the questions before revealing their solutions.</p>
            <div class="exam-question-list">{qhtml}</div>
        </div>
    </article>"""

def subject(name, description, topics):
    return f"""
    <section class="exam-subject-section">
        <div class="exam-subject-heading">
            <span>SUBJECT MODULE</span>
            <h3>{escape(name)}</h3>
            <p>{escape(description)}</p>
        </div>
        {''.join(topics)}
    </section>"""

def make_page(title, intro, subjects, exam_pattern):
    return f"""
<section class="track-content-section exam-learning-hub" id="detailed-learning">
    <div class="track-section-heading">
        <div>
            <span>06 · DETAILED LEARNING CENTRE</span>
            <h2>Subject-wise Notes and Practice</h2>
            <p>{escape(intro)}</p>
        </div>
        <span class="track-heading-icon">📚</span>
    </div>

    <div class="exam-pattern-panel">
        <span>UNDERSTAND THE QUESTION FORMAT</span>
        <h3>Exam Pattern and Practice Approach</h3>
        <p>{exam_pattern}</p>
    </div>

    <div class="exam-learning-guide">
        <h3>How to use these learning modules</h3>
        <p>Study the concept notes first, review the formula sheet, follow the solved example and then attempt the questions without opening the answers. Questions are labelled by difficulty.</p>
        <div class="exam-level-guide">
            <span class="exam-level exam-level-beginner">Beginner</span>
            <span class="exam-level exam-level-intermediate">Intermediate</span>
            <span class="exam-level exam-level-advanced">Advanced</span>
            <span class="exam-level exam-level-exam">Exam level</span>
        </div>
    </div>

    {''.join(subjects)}

    <div class="exam-pyq-panel" id="exam-pyq">
        <span>PREVIOUS-YEAR PRACTICE</span>
        <h3>Previous-Year Question Papers</h3>
        <p>Use verified papers from the relevant examination authority. Add year-wise paper links, official answer keys and solutions here when the documents are available.</p>
        <p><strong>Important:</strong> Questions in the learning modules above are original practice questions, not claimed official PYQs.</p>
    </div>

    <div class="exam-learning-disclaimer">
        Learning material is provided for practice and concept building. Check the latest official examination notification, syllabus, marking scheme and paper pattern before preparing.
    </div>
</section>
"""

def mcq(d, q, opts, ans, exp):
    return (d, q, opts, ans, exp)

B = mcq("Beginner", "What is the value of 2 + 3 × 4?",
        ["20", "14", "24", "11"], "14",
        "Multiplication is performed before addition: 2 + 12 = 14.")
I = mcq("Intermediate", "If x + 5 = 12, what is x?",
        ["5", "6", "7", "8"], "7",
        "Subtract 5 from both sides.")
A = mcq("Advanced", "If f(x) = x² + 3x, what is f'(x)?",
        ["2x + 3", "x + 3", "2x", "x² + 3"], "2x + 3",
        "Differentiate each term using the power rule.")
E = mcq("Exam", "Which property is used when a = b implies a + c = b + c?",
        ["Commutative", "Additive equality", "Associative", "Distributive"],
        "Additive equality",
        "Adding the same quantity to both sides preserves equality.")

# SEMESTER PREPARATION
semester = [
subject("Engineering Mathematics",
"Core mathematical foundations. Match these sample topics with your verified semester syllabus.",
[
topic("Functions, Limits and Continuity", "FOUNDATION",
"""<h5>1. Functions</h5>
<p>A function assigns exactly one output to each permitted input. The set of permitted inputs is the domain, while the set of resulting outputs is the range.</p>
<p>For example, f(x) = x² maps each real number to its square. Its domain is all real numbers and its range is non-negative real numbers.</p>
<h5>2. Limits</h5>
<p>A limit describes the value a function approaches as its input approaches a particular point. The function does not necessarily need to be defined at that point.</p>
<p>For polynomial functions, direct substitution is often sufficient. For indeterminate forms such as 0/0, factorisation or other limit techniques may be needed.</p>
<h5>3. Continuity</h5>
<p>A function is continuous at x = a when its limit exists there and equals its function value. Graphically, there is no break at that point.</p>""",
"""<ul><li>For a polynomial, lim x→a f(x) = f(a).</li>
<li>Continuity at a: lim x→a f(x) = f(a).</li>
<li>For a product: lim(fg) = (lim f)(lim g), when the limits exist.</li></ul>""",
"""<p>Evaluate lim x→2 (x² + 3x).</p><ol><li>Substitute x = 2 because the expression is a polynomial.</li><li>2² + 3(2) = 4 + 6.</li><li>The limit is <strong>10</strong>.</li></ol>""",
[
mcq("Beginner","Evaluate lim x→2 (x + 4)",["4","5","6","8"],"6","Substitution gives 2 + 4 = 6."),
mcq("Intermediate","What is the domain of f(x) = 1/x?",["All real numbers","All real numbers except 0","Only positive numbers","Only integers"],"All real numbers except 0","Division by zero is undefined."),
mcq("Advanced","For continuity at x = a, which equality must hold?",["f(a) = 0","Limit = f(a)","Derivative = 0","Domain is empty"],"Limit = f(a)","The limit must exist and equal the function value."),
mcq("Exam","Evaluate lim x→3 (x² - 9)/(x - 3).",["3","6","9","12"],"6","Factorise: (x - 3)(x + 3)/(x - 3), then substitute 3.")
]),
topic("Differentiation and Applications", "CORE CONCEPT",
"""<h5>1. Meaning of differentiation</h5>
<p>The derivative measures the instantaneous rate of change of a function. Geometrically, it represents the slope of the tangent to the curve at a point.</p>
<h5>2. Power rule</h5>
<p>For x raised to a constant power n, bring the exponent down as a multiplier and reduce the exponent by one.</p>
<h5>3. Product and chain rules</h5>
<p>The product rule is used when two differentiable functions are multiplied. The chain rule is used for composite functions, where one function is inside another.</p>
<h5>4. Applications</h5>
<p>Derivatives are used to determine increasing or decreasing intervals, stationary points, rates of change and optimisation.</p>""",
"""<ul><li>d(xⁿ)/dx = nxⁿ⁻¹</li><li>d(c)/dx = 0</li>
<li>d(u + v)/dx = u' + v'</li>
<li>d(uv)/dx = u'v + uv'</li>
<li>d(f(g(x)))/dx = f'(g(x))g'(x)</li></ul>""",
"""<p>Differentiate y = 3x⁴ - 2x² + 5.</p><ol><li>Differentiate each term separately.</li><li>3 × 4x³ - 2 × 2x.</li><li>Therefore dy/dx = <strong>12x³ - 4x</strong>.</li></ol>""",
[
mcq("Beginner","Derivative of x⁵?",["x⁴","5x⁴","5x","x⁶"],"5x⁴","Apply the power rule."),
mcq("Intermediate","Derivative of 7x - 9?",["7","7x","-9","0"],"7","The derivative of 7x is 7 and the derivative of a constant is zero."),
mcq("Advanced","Derivative of (x² + 1)³?",["3(x² + 1)²","6x(x² + 1)²","2x(x² + 1)","3x²"],"6x(x² + 1)²","Use the chain rule: 3(x² + 1)² × 2x."),
mcq("Exam","At a stationary point, the first derivative is generally:",["1","-1","0","Undefined"],"0","A differentiable function has a stationary point where its first derivative is zero.")
])
]),
subject("Programming Fundamentals",
"Sample computer-science foundation topics. Replace or supplement these according to the selected programme and semester.",
[
topic("Variables, Data Types and Control Flow","FOUNDATION",
"""<h5>Variables</h5><p>A variable is a named reference used to work with a value. In Python, a variable is created by assignment, such as <code>count = 10</code>.</p>
<h5>Data types</h5><p>Common Python types include int, float, str and bool. Lists store ordered collections, tuples are immutable sequences, and dictionaries store key-value pairs.</p>
<h5>Control flow</h5><p>Conditional statements choose which block executes. Loops repeat a block while a condition holds or for each item in an iterable.</p>
<h5>Functions</h5><p>Functions package reusable instructions. Parameters receive input values, and return sends a result back to the caller.</p>""",
"""<ul><li><code>if / elif / else</code>: conditional execution.</li><li><code>for</code>: iteration over an iterable.</li><li><code>while</code>: repetition while a condition is true.</li><li><code>def</code>: function definition.</li></ul>""",
"""<p>Given <code>marks = [70, 80, 90]</code>, calculate the average.</p><ol><li>Sum: 70 + 80 + 90 = 240.</li><li>Number of values: 3.</li><li>Average = 240 / 3 = <strong>80</strong>.</li></ol>""",
[
mcq("Beginner","Which Python type stores True or False?",["int","str","bool","list"],"bool","Boolean values are True and False."),
mcq("Intermediate","Which keyword defines a function in Python?",["class","def","return","import"],"def","The def keyword starts a function definition."),
mcq("Advanced","What does range(2, 6) generate?",["2,3,4,5,6","2,3,4,5","1,2,3,4,5","2,6"],"2,3,4,5","The stop value 6 is excluded."),
mcq("Exam","Which collection is immutable?",["List","Dictionary","Set","Tuple"],"Tuple","A tuple cannot be modified after creation.")
])
])
]

# GATE PREPARATION
gate = [
subject("Engineering Mathematics","Core mathematics practice for technical GATE papers.",
[
topic("Linear Algebra: Matrices and Rank","CORE",
"""<h5>Matrix</h5><p>A matrix is a rectangular arrangement of elements in rows and columns. Its order is m × n when it contains m rows and n columns.</p>
<h5>Rank</h5><p>The rank is the maximum number of linearly independent rows or columns. It equals the number of pivots in row-echelon form.</p>
<h5>Elementary row operations</h5><p>Interchanging rows, multiplying a row by a non-zero scalar, and adding a multiple of one row to another preserve rank.</p>
<h5>Linear systems</h5><p>A system Ax = b is consistent when the rank of A equals the rank of its augmented matrix [A|b]. A unique solution additionally requires that rank equal the number of unknowns.</p>""",
"""<ul><li>rank(A) ≤ min(m,n).</li><li>rank(Iₙ) = n.</li><li>For an invertible square matrix, rank(A) = n.</li><li>Consistency: rank(A) = rank([A|b]).</li></ul>""",
"""<p>Find the rank of the 2 × 2 identity matrix.</p><ol><li>Its rows are (1,0) and (0,1).</li><li>Neither row is a scalar multiple of the other.</li><li>Both are independent, so rank = <strong>2</strong>.</li></ol>""",
[
mcq("Beginner","Rank of a 3 × 3 identity matrix?",["0","1","2","3"],"3","All three rows are linearly independent."),
mcq("Intermediate","Maximum possible rank of a 3 × 5 matrix?",["2","3","5","8"],"3","Rank cannot exceed the smaller matrix dimension."),
mcq("Advanced","If a square matrix has non-zero determinant, its rank is:",["0","1","Less than n","n"],"n","A non-zero determinant implies invertibility and full rank."),
mcq("Exam","A system is inconsistent when:",["rank(A) = rank([A|b])","rank(A) < rank([A|b])","Both ranks are zero","A is square"],"rank(A) < rank([A|b])","The augmented matrix has greater rank than the coefficient matrix.")
]),
topic("Calculus: Integration","CORE",
"""<h5>Antiderivatives</h5><p>Integration reverses differentiation. An indefinite integral represents a family of antiderivatives and includes a constant of integration.</p>
<h5>Standard integrals</h5><p>Power functions, exponential functions and trigonometric functions have standard antiderivatives.</p>
<h5>Definite integrals</h5><p>A definite integral over an interval gives the signed accumulation of a function. The fundamental theorem of calculus connects definite integration with antiderivatives.</p>
<h5>Methods</h5><p>Substitution simplifies composite expressions. Integration by parts is useful for products of functions.</p>""",
"""<ul><li>∫xⁿ dx = xⁿ⁺¹/(n+1) + C, n ≠ -1.</li><li>∫1/x dx = ln|x| + C.</li><li>∫eˣ dx = eˣ + C.</li><li>∫ₐᵇ f(x)dx = F(b) - F(a).</li></ul>""",
"""<p>Evaluate ∫(3x² + 2) dx.</p><ol><li>Integrate each term.</li><li>∫3x² dx = x³.</li><li>∫2 dx = 2x.</li><li>Result: <strong>x³ + 2x + C</strong>.</li></ol>""",
[
mcq("Beginner","∫2x dx equals:",["2x² + C","x² + C","x + C","2 + C"],"x² + C","The antiderivative of 2x is x²."),
mcq("Intermediate","∫₀¹ 2x dx equals:",["0","1","2","4"],"1","Antiderivative is x²; evaluate 1² - 0²."),
mcq("Advanced","Which method is commonly suitable for ∫x eˣ dx?",["Partial fractions","Integration by parts","Row reduction","Cramer's rule"],"Integration by parts","The integrand is a product of two functions."),
mcq("Exam","The constant of integration is needed in:",["Every derivative","Indefinite integration","Only matrix operations","Only limits"],"Indefinite integration","All antiderivatives differ by a constant.")
])
]),
subject("General Aptitude","Reasoning, quantitative aptitude and language practice.",
[
topic("Quantitative Aptitude: Percentages and Ratios","FOUNDATION",
"""<h5>Percentages</h5><p>A percentage expresses a quantity per hundred. Convert a percentage to a fraction by dividing by 100.</p>
<h5>Percentage change</h5><p>Compare the change with the original value, not the final value. An increase and a decrease of the same percentage do not generally cancel.</p>
<h5>Ratios</h5><p>A ratio a:b compares quantities in the same units. If the total is known, add the ratio parts and divide the total by that sum.</p>""",
"""<ul><li>x% of N = xN/100.</li><li>Percentage change = (change/original) × 100.</li><li>If a:b and total T, first share = aT/(a+b).</li></ul>""",
"""<p>Divide 360 in the ratio 5:7.</p><ol><li>Total parts = 12.</li><li>One part = 360/12 = 30.</li><li>Shares = 150 and 210.</li></ol>""",
[
mcq("Beginner","25% of 200 is:",["25","40","50","75"],"50","200 × 25/100 = 50."),
mcq("Intermediate","Divide 80 in ratio 3:5. Smaller share?",["20","30","40","50"],"30","Eight parts; each is 10; smaller share is 3 × 10."),
mcq("Advanced","A value rises from 80 to 100. Percentage increase?",["20%","25%","30%","40%"],"25%","Increase is 20; 20/80 × 100 = 25%."),
mcq("Exam","If A:B = 2:3 and B:C = 4:5, A:C is:",["8:15","2:5","4:15","6:5"],"8:15","Make B common: 8:12 and 12:15, so A:C = 8:15.")
])
])
]

# CDS PREPARATION
cds = [
subject("English","Grammar, vocabulary and reading comprehension practice.",
[
topic("Subject–Verb Agreement","FOUNDATION",
"""<h5>Core rule</h5><p>A singular subject generally takes a singular verb; a plural subject takes a plural verb. The verb agrees with the actual subject, not a nearby noun in a modifying phrase.</p>
<h5>Indefinite pronouns</h5><p>Words such as everyone, somebody and each are generally treated as singular. Words such as many and several are plural.</p>
<h5>Either/or and neither/nor</h5><p>When subjects are joined by either/or or neither/nor, the verb generally agrees with the nearer subject.</p>
<h5>Collective nouns</h5><p>Collective nouns may be treated as singular when the group acts as one unit. Usage can vary by context and dialect.</p>""",
"""<ul><li>He works; they work.</li><li>Each of the students is ready.</li><li>The list of items is on the desk.</li><li>Neither the teacher nor the students are absent.</li></ul>""",
"""<p>Choose the correct form: 'The quality of these products ___ excellent.'</p><ol><li>Find the subject: quality.</li><li>'Of these products' is a modifying phrase.</li><li>Quality is singular, so use <strong>is</strong>.</li></ol>""",
[
mcq("Beginner","Each of the players ___ ready.",["are","is","were","have"],"is","Each is singular."),
mcq("Intermediate","The bouquet of roses ___ beautiful.",["are","were","is","have"],"is","The subject is bouquet, not roses."),
mcq("Advanced","Neither the manager nor the employees ___ available.",["is","was","are","has"],"are","The nearer subject employees is plural."),
mcq("Exam","Choose the correct sentence.",["The news are encouraging.","The news is encouraging.","The news were encouraging.","The news have encouraging."],"The news is encouraging.","News is grammatically singular.")
]),
topic("Vocabulary and Reading Comprehension","PRACTICE",
"""<h5>Vocabulary in context</h5><p>Synonyms have similar meanings, while antonyms have opposite meanings. The correct choice depends on context and tone.</p>
<h5>Roots and word families</h5><p>Recognising common prefixes, suffixes and roots can help infer unfamiliar words. For example, 'bene' is associated with good or well.</p>
<h5>Comprehension</h5><p>Read for the central idea, supporting details, tone and inference. An inference must be supported by the passage rather than outside assumptions.</p>
<h5>Sentence completion</h5><p>Use grammar and meaning together. Eliminate options that break the sentence's logic or grammatical structure.</p>""",
"""<ul><li>Synonym: similar meaning.</li><li>Antonym: opposite meaning.</li><li>Inference: conclusion supported by evidence.</li><li>Main idea: central message of a passage.</li></ul>""",
"""<p>Passage: 'Regular exercise improves stamina and supports general well-being. Consistency is more useful than occasional intense activity.'</p><ol><li>Identify the repeated idea: regularity.</li><li>Find the contrast: consistency versus occasional intensity.</li><li>Main idea: sustainable habits support well-being.</li></ol>""",
[
mcq("Beginner","Choose the synonym of 'Abundant'.",["Scarce","Plentiful","Empty","Rare"],"Plentiful","Abundant means existing in large quantities."),
mcq("Intermediate","Choose the antonym of 'Reluctant'.",["Unwilling","Hesitant","Eager","Doubtful"],"Eager","Reluctant means unwilling or hesitant."),
mcq("Advanced","A conclusion drawn from clues in a passage is called:",["A title","An inference","A quotation","A heading"],"An inference","Inference uses evidence to reach a supported conclusion."),
mcq("Exam","Choose the correctly spelt word.",["Accomodation","Acommodation","Accommodation","Acomodation"],"Accommodation","Accommodation has double c and double m.")
])
]),
subject("Elementary Mathematics","Arithmetic and algebra practice.",
[
topic("Percentages, Profit and Loss","FOUNDATION",
"""<h5>Percentage</h5><p>Percentage converts a ratio into a value out of 100. Always identify the base value before calculating a percentage change.</p>
<h5>Cost price and selling price</h5><p>Profit occurs when selling price exceeds cost price. Loss occurs when selling price is below cost price.</p>
<h5>Discount</h5><p>Discount is calculated on the marked price. The selling price is the marked price after discount.</p>""",
"""<ul><li>Profit = SP - CP.</li><li>Loss = CP - SP.</li><li>Profit% = Profit/CP × 100.</li><li>Loss% = Loss/CP × 100.</li><li>Discount = MP - SP.</li></ul>""",
"""<p>An item costs ₹500 and sells for ₹600.</p><ol><li>Profit = 600 - 500 = ₹100.</li><li>Profit percentage = 100/500 × 100.</li><li>Profit = <strong>20%</strong>.</li></ol>""",
[
mcq("Beginner","10% of 450 is:",["35","40","45","50"],"45","450 × 10/100 = 45."),
mcq("Intermediate","CP ₹200, SP ₹240. Profit percentage?",["10%","15%","20%","25%"],"20%","Profit = 40; 40/200 × 100 = 20%."),
mcq("Advanced","An item marked ₹800 has a 15% discount. Selling price?",["₹620","₹660","₹680","₹700"],"₹680","Discount = 120; selling price = 800 - 120."),
mcq("Exam","A 20% loss occurs on CP ₹750. Find SP.",["₹550","₹575","₹600","₹625"],"₹600","SP = 80% of 750 = ₹600.")
])
])
]

# AFCAT PREPARATION
afcat = [
subject("English","Vocabulary, grammar and comprehension.",
[
topic("Vocabulary: Synonyms, Antonyms and Idioms","FOUNDATION",
"""<h5>Synonyms and antonyms</h5><p>A synonym is a word with a similar meaning; an antonym expresses an opposite meaning. A word's exact sense should be checked in its sentence.</p>
<h5>Idioms</h5><p>An idiom is an established expression whose meaning is not always predictable from its individual words. Learn idioms with a short example sentence.</p>
<h5>One-word substitution</h5><p>This tests the ability to express a phrase using one precise word. Pay attention to the exact definition and grammatical role.</p>
<h5>Contextual vocabulary</h5><p>Use surrounding words to identify tone and meaning. Avoid selecting an option merely because it is a familiar synonym.</p>""",
"""<ul><li>Abundant = plentiful.</li><li>Reluctant = unwilling.</li><li>Concise = brief but complete.</li><li>Optimistic = hopeful.</li></ul>""",
"""<p>Sentence: 'The instructions were concise and easy to follow.'</p><ol><li>Concise describes the instructions.</li><li>The context suggests clarity without unnecessary length.</li><li>Meaning: <strong>brief but complete</strong>.</li></ol>""",
[
mcq("Beginner","Synonym of 'Abundant'?",["Scarce","Plentiful","Empty","Weak"],"Plentiful","Abundant means plentiful."),
mcq("Intermediate","Antonym of 'Expand'?",["Extend","Enlarge","Contract","Increase"],"Contract","Contract means to become smaller."),
mcq("Advanced","'To break the ice' means:",["To damage something","To begin a friendly conversation","To end a meeting","To create confusion"],"To begin a friendly conversation","The idiom refers to easing social interaction."),
mcq("Exam","A person who speaks many languages is a:",["Linguist","Polyglot","Orator","Novelist"],"Polyglot","A polyglot knows or uses several languages.")
]),
topic("Grammar: Tenses and Error Detection","CORE",
"""<h5>Tense</h5><p>Tense places an action in time. Simple, continuous, perfect and perfect continuous forms communicate different relationships between actions and time.</p>
<h5>Subject–verb agreement</h5><p>Match the verb to the subject. Ignore intervening phrases when identifying the main subject.</p>
<h5>Articles</h5><p>'A' and 'an' are indefinite articles; 'the' is definite. The choice between a and an depends on the initial sound, not simply the first letter.</p>
<h5>Prepositions</h5><p>Prepositions express relationships such as time, place and direction. Many verb-preposition combinations are idiomatic and must be learnt in context.</p>""",
"""<ul><li>Present simple: subject + base verb (with third-person singular agreement).</li><li>Present continuous: am/is/are + verb-ing.</li><li>Present perfect: has/have + past participle.</li><li>Past perfect: had + past participle.</li></ul>""",
"""<p>Correct: 'She has completed the assignment.'</p><ol><li>Subject is she.</li><li>Present perfect uses has + past participle.</li><li>Completed is the past participle.</li></ol>""",
[
mcq("Beginner","He ___ to the library every day.",["go","goes","going","gone"],"goes","Third-person singular takes goes."),
mcq("Intermediate","Choose the correct article: '___ honest person'.",["A","An","The only","No article"],"An","Honest begins with a vowel sound."),
mcq("Advanced","By the time we arrived, the train ___.",["leaves","has left","had left","will leave"],"had left","The earlier past action uses past perfect."),
mcq("Exam","Identify the correct sentence.",["Neither of them are ready.","Neither of them is ready.","Neither of them were ready.","Neither of them have ready."],"Neither of them is ready.","Neither is generally treated as singular in this construction.")
])
]),
subject("Numerical Ability and Reasoning","Quantitative and logical problem solving.",
[
topic("Ratio, Proportion and Time–Distance","FOUNDATION",
"""<h5>Ratio</h5><p>A ratio compares quantities. Convert both quantities into the same unit before simplifying.</p>
<h5>Proportion</h5><p>Two ratios are proportional when their cross-products are equal.</p>
<h5>Speed, distance and time</h5><p>Speed measures distance travelled per unit time. Ensure units are consistent before calculation.</p>
<h5>Average speed</h5><p>Average speed is total distance divided by total time. It is not always the arithmetic mean of two speeds.</p>""",
"""<ul><li>a:b = a/b.</li><li>a/b = c/d implies ad = bc.</li><li>Speed = Distance/Time.</li><li>Distance = Speed × Time.</li><li>Time = Distance/Speed.</li></ul>""",
"""<p>A vehicle travels 150 km in 3 hours.</p><ol><li>Speed = distance/time.</li><li>150/3 = 50.</li><li>Average speed = <strong>50 km/h</strong>.</li></ol>""",
[
mcq("Beginner","Simplify 12:18.",["2:3","3:2","4:9","6:5"],"2:3","Divide both terms by 6."),
mcq("Intermediate","A vehicle travels 120 km in 2 hours. Speed?",["40 km/h","50 km/h","60 km/h","80 km/h"],"60 km/h","120/2 = 60 km/h."),
mcq("Advanced","Divide 72 in ratio 5:7. Larger share?",["30","35","42","48"],"42","Twelve parts; one part is 6; larger share is 7 × 6."),
mcq("Exam","If speed doubles for the same distance, travel time becomes:",["Double","Half","Four times","Unchanged"],"Half","Time is inversely proportional to speed for fixed distance.")
]),
topic("Logical Reasoning: Series and Coding","CORE",
"""<h5>Number series</h5><p>Check consecutive differences first. If they are not constant, inspect ratios, second differences, squares, cubes or alternating patterns.</p>
<h5>Letter series</h5><p>Map letters to positions in the alphabet. Look for consistent increments or alternating rules.</p>
<h5>Coding and decoding</h5><p>Compare original and coded forms to identify shifts, reversals, substitutions or position-based rules.</p>
<h5>Accuracy</h5><p>Test a proposed rule against every given term. A pattern that explains only part of the series is insufficient.</p>""",
"""<ul><li>Alphabet positions: A = 1 through Z = 26.</li><li>Square numbers: 1, 4, 9, 16, 25...</li><li>Cube numbers: 1, 8, 27, 64...</li><li>Constant difference: a, a+d, a+2d...</li></ul>""",
"""<p>Find the next term: 3, 6, 12, 24.</p><ol><li>Compare consecutive terms.</li><li>Each term is multiplied by 2.</li><li>Next term = 24 × 2 = <strong>48</strong>.</li></ol>""",
[
mcq("Beginner","Next term: 5, 10, 15, 20, __.",["22","24","25","30"],"25","Add 5 each time."),
mcq("Intermediate","Next term: 1, 4, 9, 16, __.",["20","24","25","36"],"25","These are consecutive squares."),
mcq("Advanced","If CAT is coded as DBU by shifting each letter forward by one, DOG becomes:",["EPH","CNG","FQI","EOG"],"EPH","D→E, O→P, G→H."),
mcq("Exam","Find the missing term: 2, 6, 18, 54, __.",["108","126","162","216"],"162","Each term is multiplied by 3.")
])
])
]

# PLACEMENT PREPARATION
placement = [
subject("Data Structures and Algorithms","Fundamental structures, complexity and algorithmic reasoning.",
[
topic("Arrays and Complexity Analysis","FOUNDATION",
"""<h5>Array structure</h5><p>An array stores elements in indexed positions. In a typical contiguous-memory array, index access is constant time.</p>
<h5>Traversal and search</h5><p>Traversal visits elements one by one. Linear search checks each element and has O(n) worst-case time. Binary search requires sorted data and repeatedly halves the search interval.</p>
<h5>Insertion and deletion</h5><p>Inserting or deleting near the beginning of an array may require shifting elements, so the operation is generally O(n).</p>
<h5>Complexity</h5><p>Big-O describes an asymptotic upper bound on growth. It helps compare algorithms as input size increases.</p>""",
"""<ul><li>Index access: O(1).</li><li>Linear search: O(n).</li><li>Binary search on sorted data: O(log n).</li><li>Full traversal: O(n).</li><li>Auxiliary space depends on extra storage used.</li></ul>""",
"""<p>For an array of 100 elements, how many elements may linear search inspect in the worst case?</p><ol><li>The target may be at the final position or absent.</li><li>Every element may need to be checked.</li><li>Worst-case checks = <strong>100</strong>, proportional to n.</li></ol>""",
[
mcq("Beginner","Array access by index is typically:",["O(1)","O(log n)","O(n)","O(n²)"],"O(1)","Direct indexing gives constant-time access."),
mcq("Intermediate","Worst-case linear search in n elements is:",["O(1)","O(log n)","O(n)","O(n log n)"],"O(n)","It may inspect every element."),
mcq("Advanced","Binary search requires the input to be:",["Random","Sorted","Reversed","Unique only"],"Sorted","The algorithm relies on ordered comparisons."),
mcq("Exam","Two nested loops each running n times usually produce:",["O(1)","O(log n)","O(n)","O(n²)"],"O(n²)","The inner loop runs n times for each of n outer iterations.")
]),
topic("Stacks, Queues and Linked Lists","CORE",
"""<h5>Stack</h5><p>A stack follows Last In, First Out (LIFO). Push inserts an item; pop removes the top item. It is useful for function calls, undo operations and expression evaluation.</p>
<h5>Queue</h5><p>A queue follows First In, First Out (FIFO). Enqueue inserts at the rear; dequeue removes from the front. Scheduling and buffering are common uses.</p>
<h5>Linked list</h5><p>A linked list consists of nodes containing data and links. Insertion can be efficient when the target position is already known, but accessing an arbitrary index requires traversal.</p>
<h5>Trade-offs</h5><p>Arrays offer direct indexed access. Linked lists offer flexible node insertion but require pointer traversal and extra link storage.</p>""",
"""<ul><li>Stack: LIFO.</li><li>Queue: FIFO.</li><li>Stack push/pop: O(1) at the top.</li><li>Queue enqueue/dequeue: O(1) with suitable front/rear references.</li><li>Linked-list search: O(n).</li></ul>""",
"""<p>Push 10, then 20, then 30 onto an empty stack. Perform one pop.</p><ol><li>Stack from bottom to top: 10, 20, 30.</li><li>Pop removes the top item.</li><li>Removed item = <strong>30</strong>.</li></ol>""",
[
mcq("Beginner","Which structure follows LIFO?",["Queue","Stack","Tree","Graph"],"Stack","The last inserted item is removed first."),
mcq("Intermediate","Which structure is suitable for a printer queue?",["Stack","Queue","Binary tree","Hash set"],"Queue","Print jobs are typically processed in arrival order."),
mcq("Advanced","Accessing the kth element of a singly linked list generally takes:",["O(1)","O(log n)","O(n)","O(n²)"],"O(n)","Nodes must be traversed sequentially."),
mcq("Exam","Which operation removes the top stack element?",["Push","Pop","Enqueue","Insert"],"Pop","Pop removes the top item.")
])
]),
subject("Core Computer Science","Programming, databases, operating systems and networking.",
[
topic("Object-Oriented Programming","FOUNDATION",
"""<h5>Class and object</h5><p>A class defines a structure and behaviour; an object is an instance of that class.</p>
<h5>Encapsulation</h5><p>Encapsulation groups data with methods and controls how internal state is accessed.</p>
<h5>Abstraction</h5><p>Abstraction exposes essential behaviour while hiding implementation details.</p>
<h5>Inheritance</h5><p>Inheritance allows a derived class to reuse and extend the behaviour of a base class.</p>
<h5>Polymorphism</h5><p>Polymorphism allows a common interface to represent different underlying behaviours. Method overriding is a common example.</p>""",
"""<ul><li>Class: blueprint.</li><li>Object: instance.</li><li>Encapsulation: controlled data access.</li><li>Abstraction: hide implementation complexity.</li><li>Inheritance: extend an existing class.</li><li>Polymorphism: common interface, varied behaviour.</li></ul>""",
"""<p>Suppose a base class <code>Vehicle</code> defines a method <code>move()</code>. A <code>Car</code> class inherits from Vehicle and provides its own implementation.</p><ol><li>Vehicle is the base class.</li><li>Car is the derived class.</li><li>Reusing and extending Vehicle demonstrates <strong>inheritance</strong>.</li><li>Calling move() on different vehicle objects can demonstrate polymorphism.</li></ol>""",
[
mcq("Beginner","A class is best described as:",["An object instance","A blueprint for objects","A database row","A loop"],"A blueprint for objects","A class defines the structure and behaviour of instances."),
mcq("Intermediate","Which OOP pillar is associated with acquiring properties from a base class?",["Abstraction","Inheritance","Compilation","Iteration"],"Inheritance","A derived class inherits from a base class."),
mcq("Advanced","Method overriding is commonly associated with:",["Polymorphism","File handling","Sorting","Indexing"],"Polymorphism","Different classes can provide different implementations of a common method."),
mcq("Exam","Hiding internal implementation and exposing essential behaviour is:",["Inheritance","Abstraction","Iteration","Instantiation"],"Abstraction","Abstraction reduces the details a user must understand.")
]),
topic("DBMS and SQL","CORE",
"""<h5>Database fundamentals</h5><p>A database organises data for storage, retrieval and management. A relational database represents data in tables with rows and columns.</p>
<h5>Keys</h5><p>A primary key uniquely identifies each row. A foreign key references a key in another table and helps represent relationships.</p>
<h5>SQL commands</h5><p>SELECT retrieves records; INSERT adds rows; UPDATE changes values; DELETE removes rows. WHERE filters rows.</p>
<h5>Joins</h5><p>INNER JOIN returns matching rows from both tables. LEFT JOIN preserves every row from the left table and includes matching right-side values when available.</p>
<h5>Normalisation</h5><p>Normalisation organises relational data to reduce unnecessary duplication and update anomalies.</p>""",
"""<ul><li><code>SELECT columns FROM table;</code></li><li><code>WHERE</code>: filter rows.</li><li><code>ORDER BY</code>: sort results.</li><li><code>GROUP BY</code>: group rows.</li><li><code>COUNT()</code>: count rows or non-null values.</li></ul>""",
"""<p>Retrieve employees whose salary exceeds 30000:</p><pre><code>SELECT name, salary
FROM employees
WHERE salary &gt; 30000;</code></pre><ol><li>SELECT chooses the columns.</li><li>FROM identifies the table.</li><li>WHERE applies the condition.</li></ol>""",
[
mcq("Beginner","Which SQL command retrieves records?",["INSERT","UPDATE","SELECT","DELETE"],"SELECT","SELECT retrieves data."),
mcq("Intermediate","Which key uniquely identifies a row?",["Foreign key","Primary key","Duplicate key","Temporary key"],"Primary key","A primary key uniquely identifies each record."),
mcq("Advanced","Which clause filters grouped results?",["WHERE","ORDER BY","HAVING","FROM"],"HAVING","HAVING applies conditions after grouping."),
mcq("Exam","Which join preserves all rows from the left table?",["INNER JOIN","LEFT JOIN","CROSS JOIN","SELF JOIN"],"LEFT JOIN","LEFT JOIN preserves all left-table rows.")
])
]),
subject("Operating Systems and Computer Networks","System-level fundamentals for technical interviews and assessments.",
[
topic("Operating Systems: Processes and Memory","CORE",
"""<h5>Process and thread</h5><p>A process is a running program with its own execution context and resources. A thread is a unit of execution within a process. Threads in the same process generally share its address space.</p>
<h5>Scheduling</h5><p>CPU scheduling selects which ready process or thread receives processor time. Common algorithms include FCFS, SJF, priority scheduling and round robin.</p>
<h5>Memory management</h5><p>Virtual memory gives processes an abstraction of address space. Paging divides virtual memory into fixed-size pages and physical memory into frames.</p>
<h5>Deadlock</h5><p>Deadlock involves processes waiting indefinitely for resources. The classic necessary conditions are mutual exclusion, hold and wait, no preemption and circular wait.</p>""",
"""<ul><li>Turnaround time = completion time - arrival time.</li><li>Waiting time = turnaround time - burst time.</li><li>Response time = first response time - arrival time.</li><li>Round robin uses a time quantum.</li></ul>""",
"""<p>A process arrives at time 0, runs for 5 units and completes at time 8.</p><ol><li>Turnaround time = 8 - 0 = 8.</li><li>Burst time = 5.</li><li>Waiting time = 8 - 5 = <strong>3 units</strong>.</li></ol>""",
[
mcq("Beginner","A running instance of a program is a:",["File","Process","Folder","Compiler"],"Process","A process is a program in execution."),
mcq("Intermediate","Which scheduler uses a time quantum?",["FCFS","Round robin","Non-preemptive SJF only","FIFO disk scheduling"],"Round robin","Round robin allocates a time slice to each ready process."),
mcq("Advanced","How many necessary Coffman conditions are classically listed for deadlock?",["2","3","4","5"],"4","Mutual exclusion, hold and wait, no preemption and circular wait."),
mcq("Exam","Virtual memory primarily provides:",["Only cache storage","An address-space abstraction","A faster CPU","A network protocol"],"An address-space abstraction","It separates process address spaces from physical memory layout.")
]),
topic("Computer Networks: TCP/IP and HTTP","CORE",
"""<h5>Network models</h5><p>Layered models divide communication into responsibilities. The TCP/IP model commonly uses link, internet, transport and application layers.</p>
<h5>IP and MAC addresses</h5><p>IP addresses identify interfaces at the network layer. MAC addresses are used for delivery on a local link.</p>
<h5>TCP and UDP</h5><p>TCP provides reliable, ordered byte-stream delivery. UDP is connectionless and has lower protocol overhead, but does not itself guarantee delivery or ordering.</p>
<h5>HTTP and HTTPS</h5><p>HTTP is an application-layer protocol used for web communication. HTTPS protects HTTP communication using TLS.</p>
<h5>DNS</h5><p>DNS translates domain names into records such as IP addresses.</p>""",
"""<ul><li>HTTP: application layer.</li><li>TCP: reliable transport.</li><li>UDP: connectionless transport.</li><li>DNS: domain-name resolution.</li><li>HTTPS: HTTP protected with TLS.</li></ul>""",
"""<p>A browser needs to contact a website using its domain name.</p><ol><li>The browser or operating system checks available DNS information.</li><li>A DNS lookup resolves the domain to an address.</li><li>The client establishes the required transport connection.</li><li>For HTTPS, TLS protects the application communication.</li></ol>""",
[
mcq("Beginner","Which protocol resolves domain names?",["FTP","DNS","SMTP","ARP"],"DNS","DNS resolves domain names to records such as IP addresses."),
mcq("Intermediate","Which transport protocol provides reliable ordered delivery?",["UDP","TCP","IP","DNS"],"TCP","TCP provides reliable, ordered byte-stream delivery."),
mcq("Advanced","HTTPS commonly uses which security protocol?",["TLS","DHCP","ICMP","ARP"],"TLS","TLS protects the HTTP communication channel."),
mcq("Exam","Which layer is responsible for routing between networks?",["Application","Transport","Internet/Network","Presentation"],"Internet/Network","IP operates at the internet or network layer.")
])
])
]

DATA = {
    "semester-preparation.html": (
        "Semester Preparation",
        "Build strong foundations through structured concept learning and worked practice.",
        semester,
        "This is a flexible semester-learning structure, not a claimed official LPU syllabus. Match the subjects and units to the learner's verified programme and semester."
    ),
    "gate-preparation.html": (
        "GATE Preparation",
        "Study core concepts, mathematical methods and aptitude through progressive practice.",
        gate,
        "GATE papers may include MCQ, MSQ and Numerical Answer Type questions. Negative marking applies to specified MCQs; verify the current paper-specific instructions and marking scheme."
    ),
    "cds-preparation.html": (
        "CDS Preparation",
        "Build English, mathematics and general-awareness skills through topic-wise study.",
        cds,
        "CDS written examination papers use objective questions. The English and General Knowledge papers are common, while Elementary Mathematics is applicable to the relevant academies. Verify the latest UPSC notification and paper structure."
    ),
    "afcat-preparation.html": (
        "AFCAT Preparation",
        "Strengthen language, numerical ability, reasoning and general awareness.",
        afcat,
        "AFCAT practice should reflect objective questions and the latest official syllabus. Confirm current duration, marking rules and subject coverage from the official notification."
    ),
    "placement-preparation.html": (
        "Placement Preparation",
        "Prepare for aptitude rounds, technical assessments and foundational interviews.",
        placement,
        "Placement assessments vary by employer. These modules cover common technical foundations and are not a representation of any single company's official test."
    )
}

for filename, (title, intro, subjects, pattern) in DATA.items():
    path = PAGES / filename
    original = path.read_text(encoding="utf-8")
    replacement = make_page(title, intro, subjects, pattern)

    start = original.find("Starter Notes and Practice")
    if start < 0:
        start = original.find("LEARN AND TEST YOURSELF")
    if start < 0:
        raise RuntimeError(f"Could not find learning section in {filename}")

    section_start = original.rfind("<section", 0, start)
    section_end = original.find("</section>", start)
    if section_start < 0 or section_end < 0:
        raise RuntimeError(f"Could not locate section boundaries in {filename}")

    section_end += len("</section>")
    updated = original[:section_start] + replacement + original[section_end:]
    path.write_text(updated, encoding="utf-8")
    print(f"Updated: {filename}")

print("All five learning sections have been rebuilt.")
