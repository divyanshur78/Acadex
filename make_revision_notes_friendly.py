from pathlib import Path
import shutil
import re

page = Path("pages/exams/quick-revision.html")
html = page.read_text(encoding="utf-8")

shutil.copy2(page, "quick-revision-before-friendly-notes.html")

replacements = {
    "Functions and Limits": "Functions and Limits – Understanding Inputs and Outputs",

    "<li>A function assigns exactly one output to each permitted input.</li>":
    "<li><strong>Function:</strong> A function takes an input and produces exactly one output for that input. Think of it like a machine: you give it a value, and it returns a result.</li>",

    "<li>Domain: permitted input values; range: resulting output values.</li>":
    "<li><strong>Domain and Range:</strong> The domain is the set of values you are allowed to put into a function. The range is the set of outputs the function can produce.</li>",

    "<li>A limit describes the value approached by a function near a point.</li>":
    "<li><strong>Limit:</strong> A limit tells us what value a function gets closer to as the input approaches a particular number. The function does not necessarily have to equal that value at the exact point.</li>",

    "<li>For polynomials, direct substitution evaluates the limit.</li>":
    "<li><strong>Finding polynomial limits:</strong> For a polynomial expression, you can usually find the limit by directly replacing the variable with the given value and simplifying.</li>",

    "<li>Power rule: \\\\(\\frac{d}{dx}x^n=nx^{n-1}\\\\).</li>":
    "<li><strong>Power Rule:</strong> Bring the exponent down as a multiplier and reduce the original exponent by one. Example: the derivative of x to the power 3 is 3x squared.</li>",

    "<li>Product rule: \\\\((uv)'=u'v+uv'\\\\).</li>":
    "<li><strong>Product Rule:</strong> When two functions are multiplied, differentiate the first while keeping the second unchanged, then add the first unchanged multiplied by the derivative of the second.</li>",

    "<li>Quotient rule: \\\\((u/v)'=(vu'-uv')/v^2\\\\).</li>":
    "<li><strong>Quotient Rule:</strong> When one function is divided by another, multiply the denominator by the derivative of the numerator, subtract the numerator multiplied by the derivative of the denominator, and divide everything by the denominator squared.</li>",

    "<li>A derivative represents instantaneous rate of change.</li>":
    "<li><strong>Meaning of a derivative:</strong> A derivative tells us how quickly something is changing at a particular moment. On a graph, it represents the slope of the tangent at that point. In motion, it can represent instantaneous velocity.</li>",

    "<li>Matrix order is rows × columns.</li>":
    "<li><strong>Matrix order:</strong> It tells us how many rows and columns a matrix contains. For example, a matrix with 2 rows and 3 columns has order 2 × 3.</li>",

    "<li>Matrix addition requires equal dimensions.</li>":
    "<li><strong>Matrix addition:</strong> Two matrices can be added only when they have the same number of rows and columns. Add the corresponding entries to get the answer.</li>",

    "<li>For an invertible square matrix, determinant is non-zero.</li>":
    "<li><strong>Determinant:</strong> A square matrix can have an inverse only when its determinant is not zero. A determinant of zero means the matrix is singular and has no inverse.</li>",

    "<li>Rank is the maximum number of linearly independent rows or columns.</li>":
    "<li><strong>Rank:</strong> Rank tells us how many independent rows or columns a matrix contains. In simple terms, it measures how much unique information the matrix has.</li>",

    "<li>O(1): constant time.</li>":
    "<li><strong>Constant time – O(1):</strong> The operation takes roughly the same amount of time regardless of how many items are stored. Example: accessing an array element using its index.</li>",

    "<li>O(log n): logarithmic growth.</li>":
    "<li><strong>Logarithmic time – O(log n):</strong> The amount of work grows slowly because the problem is repeatedly divided into smaller parts. Example: binary search in a sorted list.</li>",

    "<li>O(n): linear growth.</li>":
    "<li><strong>Linear time – O(n):</strong> The work increases with the number of items. If the number of items doubles, the work may roughly double. Example: checking every item in a list.</li>",

    "<li>O(n log n): common efficient sorting complexity.</li>":
    "<li><strong>O(n log n):</strong> This is a common time complexity for efficient sorting algorithms. The work grows faster than linear time but generally much more slowly than quadratic time.</li>",

    "<li>O(n²): often appears in two nested loops.</li>":
    "<li><strong>Quadratic time – O(n squared):</strong> This often occurs when one loop runs inside another loop. If the input size doubles, the number of operations may become roughly four times larger.</li>",

    "<li>Binary search requires sorted input and runs in O(log n) time.</li>":
    "<li><strong>Binary Search:</strong> This method works only on sorted data. It checks the middle element and repeatedly removes half of the remaining search area. Its time complexity is logarithmic, written as O(log n).</li>",

    "<li>Array: indexed collection of elements.</li>":
    "<li><strong>Array:</strong> A collection of elements stored in an indexed sequence. Each element can be accessed using its position or index.</li>",

    "<li>Stack: follows LIFO (Last In, First Out).</li>":
    "<li><strong>Stack – LIFO (Last In, First Out):</strong> The last item added is the first one removed. Imagine a stack of plates: you normally take the top plate first.</li>",

    "<li>Queue: follows FIFO (First In, First Out).</li>":
    "<li><strong>Queue – FIFO (First In, First Out):</strong> The first item added is the first one removed. It works like a queue of people waiting for their turn.</li>",

    "<li>Linked list: nodes connected through references.</li>":
    "<li><strong>Linked List:</strong> A sequence of nodes where each node stores data and a reference to the next node. Unlike a typical array, its elements do not need to be stored next to each other in memory.</li>",

    "<li>Push inserts into a stack; pop removes its top element.</li>":
    "<li><strong>Push and Pop:</strong> Push adds a new item to the top of a stack. Pop removes the item currently at the top.</li>",

    "<li>A database organises information for storage and retrieval.</li>":
    "<li><strong>Database:</strong> An organised collection of information that makes storing, searching, updating and managing data easier.</li>",

    "<li>A primary key uniquely identifies each row.</li>":
    "<li><strong>Primary Key:</strong> A column, or combination of columns, that uniquely identifies every record in a table. It cannot contain duplicate or NULL values.</li>",

    "<li>A foreign key references a key in another table.</li>":
    "<li><strong>Foreign Key:</strong> A column that connects one table to another by referring to a key in the related table. It helps maintain relationships between records.</li>",

    "<li>Candidate keys are minimal sets of attributes that uniquely identify rows.</li>":
    "<li><strong>Candidate Key:</strong> A minimal column or combination of columns that can uniquely identify a record. One candidate key is selected as the primary key.</li>",

    "<li>SELECT retrieves data; INSERT adds rows; UPDATE modifies rows; DELETE removes rows.</li>":
    "<li><strong>Basic SQL Commands:</strong> SELECT reads information, INSERT adds new records, UPDATE changes existing records, and DELETE removes records from a table.</li>",

    "<li>WHERE filters rows; ORDER BY sorts results.</li>":
    "<li><strong>WHERE and ORDER BY:</strong> WHERE displays only records that match a condition. ORDER BY arranges the results in ascending or descending order.</li>",

    "<li>GROUP BY groups rows for aggregate calculations.</li>":
    "<li><strong>GROUP BY:</strong> It collects records with the same value into groups. It is commonly used with calculations such as COUNT, SUM and AVG.</li>",

    "<li>1NF requires atomic values and no repeating groups.</li>":
    "<li><strong>First Normal Form (1NF):</strong> Each table cell should contain a single, indivisible value. Avoid storing multiple unrelated values in one cell or repeating groups of columns.</li>",

    "<li>Normalisation helps reduce redundancy and update anomalies.</li>":
    "<li><strong>Normalisation:</strong> The process of organising database tables to reduce repeated information and prevent problems when records are inserted, updated or deleted.</li>",

    "<li>A process is a program in execution.</li>":
    "<li><strong>Process:</strong> A program that is currently running. It has its own execution state and resources managed by the operating system.</li>",

    "<li>A thread is a unit of execution within a process.</li>":
    "<li><strong>Thread:</strong> A smaller unit of execution inside a process. Multiple threads can work within the same process and share many of its resources.</li>",

    "<li>Context switching changes the CPU from one execution context to another.</li>":
    "<li><strong>Context Switching:</strong> The operating system saves the current task's state and switches the CPU to another task. This allows multiple programs to share CPU time.</li>",

    "<li>Scheduling decides which ready process receives CPU time.</li>":
    "<li><strong>CPU Scheduling:</strong> The operating system decides which waiting process should use the CPU next and for how long.</li>",

    "<li>RAM provides working storage for active programs.</li>":
    "<li><strong>RAM (Random Access Memory):</strong> Temporary working memory used by programs while they are running. Its contents are normally lost when the computer is switched off.</li>",

    "<li>Virtual memory gives processes an abstraction of a larger address space.</li>":
    "<li><strong>Virtual Memory:</strong> A memory-management technique that gives each process its own address space. The operating system manages how virtual addresses relate to physical memory.</li>",

    "<li>Paging divides memory into fixed-size pages and frames.</li>":
    "<li><strong>Paging:</strong> Memory is divided into fixed-size blocks. The process's blocks are called pages, while the corresponding blocks in physical memory are called frames.</li>",

    "<li>Deadlock involves processes waiting indefinitely for resources.</li>":
    "<li><strong>Deadlock:</strong> A situation where two or more processes are stuck waiting for resources held by one another, so none of them can continue.</li>",

    "<li>The four necessary deadlock conditions are mutual exclusion, hold and wait, no preemption and circular wait.</li>":
    "<li><strong>Four Deadlock Conditions:</strong> Mutual exclusion means a resource cannot be shared at the same time; hold and wait means a process holds one resource while requesting another; no preemption means resources cannot simply be taken away; circular wait means processes form a cycle of waiting.</li>",

    "<li>Round Robin scheduling gives each ready process a time slice before moving to the next process.</li>":
    "<li><strong>Round Robin Scheduling:</strong> Each ready process receives a fixed period of CPU time, called a time quantum. If it is not finished, it moves to the back of the ready queue.</li>",

    "<li>OSI has seven layers: Physical, Data Link, Network, Transport, Session, Presentation and Application.</li>":
    "<li><strong>OSI Model:</strong> The Open Systems Interconnection model explains network communication in seven layers: Physical, Data Link, Network, Transport, Session, Presentation and Application. Each layer has a specific responsibility.</li>",

    "<li>TCP provides reliable, connection-oriented transport.</li>":
    "<li><strong>TCP (Transmission Control Protocol):</strong> A transport protocol that establishes a connection and helps deliver data reliably, in the correct order.</li>",

    "<li>UDP provides connectionless transport with lower overhead.</li>":
    "<li><strong>UDP (User Datagram Protocol):</strong> A connectionless transport protocol that sends data without guaranteeing delivery or order. It has less overhead and is useful when speed matters.</li>",

    "<li>IP handles logical addressing and packet routing.</li>":
    "<li><strong>IP (Internet Protocol):</strong> It provides logical addresses and helps route packets from one network to another.</li>",

    "<li>HTTP/HTTPS: web communication.</li>":
    "<li><strong>HTTP and HTTPS:</strong> Protocols used for communication between browsers and web servers. HTTPS adds encryption to protect the communication.</li>",

    "<li>DNS: translates domain names into IP addresses.</li>":
    "<li><strong>DNS (Domain Name System):</strong> It helps convert readable website names into IP addresses that computers use to locate servers.</li>",

    "<li>DHCP: assigns network configuration automatically.</li>":
    "<li><strong>DHCP (Dynamic Host Configuration Protocol):</strong> It automatically provides devices with network settings such as an IP address.</li>",

    "<li>SMTP: sends email.</li>":
    "<li><strong>SMTP (Simple Mail Transfer Protocol):</strong> It is commonly used to send outgoing email between mail clients and servers.</li>",

    "<li>FTP: transfers files.</li>":
    "<li><strong>FTP (File Transfer Protocol):</strong> A protocol designed to transfer files between computers over a network.</li>"
}

count = 0
for old, new in replacements.items():
    if old in html:
        html = html.replace(old, new)
        count += 1

page.write_text(html, encoding="utf-8")

print(f"Updated {count} student-friendly explanations.")
print("All six revision modules retained.")
print("Questions, answer reveals and accordion structure preserved.")
print("Backup: quick-revision-before-friendly-notes.html")
