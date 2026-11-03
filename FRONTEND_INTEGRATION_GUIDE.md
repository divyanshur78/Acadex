# AcedeX Frontend Integration Guide

Version: 1.0
Purpose: Frontend-to-JavaScript integration specification.

---

## 1. Project overview

AcedeX is an academic platform designed to organise university learning
resources and examination preparation.

The platform contains six academic fields:

1. Computer Science & IT
2. Engineering & Technology
3. Management & Commerce
4. Pharmaceutical Sciences
5. Agriculture
6. Law

Main modules:

- Courses
- Digital Library
- Book Locator
- Exam Preparation
- Student Profile

The frontend is built with HTML5 and CSS3.
JavaScript is responsible for data loading, rendering, filtering,
searching, navigation behaviour and other dynamic interactions.

Do not redesign the existing interface when implementing JavaScript.

---

## 2. Development rules

1. Preserve existing HTML IDs.
2. Preserve existing data-* attributes.
3. Use descriptive JavaScript variable and function names.
4. Keep data separate from presentation.
5. Do not hardcode individual programmes or subjects into HTML.
6. Use reusable rendering functions.
7. Use semantic HTML elements.
8. Handle empty, loading and error states.
9. Never invent academic information or library inventory.
10. Do not execute uploaded JavaScript files from students or researchers.

---

## 3. Homepage DOM contract

| Element ID | Responsibility |
|---|---|
| mainSidebar | Main sidebar container |
| globalSearchForm | Global search form |
| globalSearchInput | Search input |
| academicFieldGrid | Academic field cards |
| platformModuleGrid | Main platform module cards |
| recentResourceList | Recently added resource items |
| academicOverview | Student academic overview |
| currentYear | Footer year |

Important data attributes:

- data-action="toggle-sidebar"
- data-action="open-notifications"
- data-user-name
- data-user-program
- data-user-initials
- data-search-scope="all"
- data-search-term
- data-field-card
- data-field-id
- data-module-id
- data-component
- data-empty-state

Do not rename these attributes without coordinating with the frontend owner.

---

## 4. Academic field data structure

Each academic field should follow this structure:

{
  "id": "computer-science-it",
  "name": "Computer Science & IT",
  "description": "Computing, software, data and information technology.",
  "slug": "computer-science-it",
  "programmes": []
}

The six field IDs are:

- computer-science-it
- engineering-technology
- management-commerce
- pharmaceutical-sciences
- agriculture
- law

---

## 5. Academic hierarchy

Use this hierarchy throughout the platform:

Academic Field
    |
    +-- Programme
            |
            +-- Semester
                    |
                    +-- Subject
                            |
                            +-- Units / Topics
                            +-- Notes
                            +-- Assignments
                            +-- Practicals
                            +-- Books
                            +-- Videos
                            +-- Previous Year Questions

A subject should be reusable across the Courses, Digital Library
and Exam Preparation modules where appropriate.

---

## 6. Suggested programme data structure

{
  "id": "btech-cse",
  "name": "Bachelor of Technology",
  "specialisation": "Computer Science and Engineering",
  "fieldId": "computer-science-it",
  "programmeCode": "",
  "durationYears": 4,
  "semesters": []
}

Exact programme names, codes, duration and curriculum must be
verified using authorised university sources before publication.

---

## 7. Suggested semester data structure

{
  "id": "btech-cse-sem-1",
  "programmeId": "btech-cse",
  "semesterNumber": 1,
  "academicYear": "",
  "subjects": []
}

---

## 8. Suggested subject data structure

{
  "id": "subject-unique-id",
  "name": "Subject Name",
  "subjectCode": "",
  "credits": null,
  "semesterId": "",
  "description": "",
  "units": [],
  "resources": [],
  "previousYearQuestions": []
}

---

## 9. Suggested resource data structure

{
  "id": "resource-unique-id",
  "title": "Resource Title",
  "type": "notes",
  "subjectId": "",
  "description": "",
  "fileUrl": "",
  "sourceUrl": "",
  "author": "",
  "publisher": "",
  "publicationYear": null,
  "accessType": "open",
  "licence": "",
  "createdAt": ""
}

Supported resource types may include:

- book
- notes
- research-paper
- journal
- presentation
- video
- reference
- assignment
- practical-manual
- question-paper

Only display verified resource links.

---

## 10. Book Locator data structure

{
  "id": "book-unique-id",
  "title": "Book Title",
  "author": "",
  "isbn": "",
  "callNumber": "",
  "building": "",
  "floor": "",
  "section": "",
  "rack": "",
  "shelf": "",
  "availableCopies": null,
  "totalCopies": null,
  "availability": "unknown"
}

Physical location and availability must come from authorised library
inventory data. Never generate fictional rack or shelf locations.

---

## 11. Exam Preparation hierarchy

Exam Preparation
    |
    +-- Semester Exams
    |       |
    |       +-- Programme
    |               |
    |               +-- Semester
    |                       |
    |                       +-- Subject
    |                               |
    |                               +-- Short Notes
    |                               +-- Quick Revision
    |                               +-- Summaries
    |                               +-- Practice Questions
    |                               +-- PYQs
    |
    +-- GATE
    |       |
    |       +-- Paper
    |               |
    |               +-- Subject
    |                       |
    |                       +-- Topic
    |                               |
    |                               +-- Revision
    |                               +-- Practice
    |                               +-- PYQs
    |
    +-- CDS
    |
    +-- AFCAT
    |
    +-- Placement Preparation

CDS, AFCAT and Placement Preparation should use their own
relevant subject/topic structures.

---

## 12. PYQ data requirements

PYQs belong inside the relevant subject or exam topic.
They are not a separate top-level module.

Suggested question structure:

{
  "id": "question-unique-id",
  "examId": "",
  "subjectId": "",
  "topicId": "",
  "year": null,
  "paperCode": "",
  "session": "",
  "questionNumber": "",
  "questionType": "mcq",
  "question": "",
  "options": [],
  "answer": "",
  "explanation": "",
  "answerSource": "aceDex-authored",
  "sourceUrl": "",
  "licence": ""
}

Official answer keys and AcedeX-authored explanations must be
clearly distinguished.

Uploaded JS files must never be executed in the student browser.
Import trusted data in a controlled process and validate it before use.
Prefer JSON, CSV and PDF as resource formats.

---

## 13. Search behaviour

The homepage search form uses:

- Form ID: globalSearchForm
- Input ID: globalSearchInput
- Attribute: data-search-scope="all"

The form should eventually search across:

- Programmes
- Subjects
- Books
- Notes
- Research papers
- Exam topics
- PYQs

Search results should link to the relevant page and record.

---

## 14. Empty states and data handling

The homepage already contains empty-state containers.

When data is available:

1. Replace the corresponding empty state with rendered content.
2. Do not duplicate the empty-state message.
3. Handle missing optional fields safely.
4. Show meaningful feedback if no results exist.
5. Do not display fake statistics or progress.

---

## 15. JavaScript implementation boundaries

Suggested JavaScript responsibilities:

### app.js
- Shared navigation behaviour
- Sidebar interaction
- Search coordination
- Shared UI helpers
- User profile information
- Common application initialisation

### courses.js
- Field selection
- Programme listing
- Semester selection
- Subject listing
- Subject details
- Course resource rendering

### library.js
- Library filters
- Resource listings
- Book details
- Book location display
- Availability presentation

### exam-prep.js
- Exam category navigation
- Subject/topic selection
- Revision resource rendering
- Practice questions
- PYQ rendering

Keep each module independent where possible.

---

## 16. Important collaboration rule

The JavaScript developer should request the latest versions of:

- index.html
- Relevant page HTML files
- css/style.css
- css/components.css
- css/responsive.css
- This integration guide

Before implementing a feature, inspect the existing IDs, classes,
data attributes and page structure.

Do not create a second UI or replace the design with a different
framework without agreement from the frontend developer.

The goal is to make JavaScript fit the AcedeX interface exactly.
