from pathlib import Path
import shutil
import re

page = Path("pages/exams/quick-revision.html")
html = page.read_text(encoding="utf-8")

backup = Path("quick-revision-before-differentiation-update.html")
shutil.copy2(page, backup)

pattern = re.compile(
    r'<h3>Differentiation</h3>\s*<ul>.*?</ul>',
    re.DOTALL
)

replacement = """<h3>Differentiation – Important Rules</h3>

<ul>
    <li>
        <strong>Power Rule:</strong>
        When differentiating a power of x, bring the exponent
        in front and reduce it by one.
        <p>Example: If y = x³, its derivative is 3x².</p>
        <p>Rule: \\\\(\\\\frac{d}{dx}x^n=nx^{n-1}\\\\)</p>
    </li>

    <li>
        <strong>Product Rule:</strong>
        Use this when two functions are multiplied.
        Differentiate the first function and multiply it by
        the second, then add the first function multiplied
        by the derivative of the second.
        <p>Rule: \\\\((uv)'=u'v+uv'\\\\)</p>
    </li>

    <li>
        <strong>Quotient Rule:</strong>
        Use this when one function is divided by another.
        Multiply the denominator by the derivative of the
        numerator, subtract the numerator multiplied by the
        derivative of the denominator, and divide by the
        denominator squared.
        <p>Rule: \\\\((u/v)'=(vu'-uv')/v^2\\\\)</p>
    </li>

    <li>
        <strong>What does a derivative mean?</strong>
        A derivative tells us how quickly something changes
        at a particular moment. On a graph, it represents
        the slope of the tangent at a point.
        <p>Example: In motion, the derivative of position
        with respect to time gives instantaneous velocity.</p>
    </li>
</ul>"""

updated, count = pattern.subn(replacement, html, count=1)

if count != 1:
    raise SystemExit("Differentiation section not found. Original file unchanged.")

page.write_text(updated, encoding="utf-8")
print("Differentiation notes updated successfully.")
print(f"Backup: {backup}")
