# AcedeX Frontend Integration Guide

## Project boundary
The frontend structure and styling are maintained separately from application logic.

HTML and CSS pages are prepared for integration. JavaScript behaviour, academic data, API communication, dynamic rendering, search, filtering, authentication and state management are assigned to the integration developer.

Do not rebuild the visual pages unless a UI change is specifically requested.

## Pages
- `index.html` — Dashboard and module entry points.
- `pages/courses.html` — Academic field and programme browser.
- `pages/course-details.html` — Subject information and resources.
- `pages/digital-library.html` — Digital academic resource collections.
- `pages/book-locator.html` — Physical library catalogue and location.
- `pages/book-details.html` — Book metadata and related resources.
- `pages/exam-preparation.html` — Examination preparation categories.
- `pages/exam-details.html` — Exam overview and preparation resources.
- `pages/profile.html` — Student profile and learning space.

## JavaScript implementation required

### Shared application
- Initialise navigation and shared page behaviour.
- Connect profile information and dashboard data.
- Implement global search and notifications where present.
- Preserve existing HTML and CSS structure.

### Courses
- Load academic fields and programmes.
- Implement field → programme → semester → subject navigation.
- Render subject details, units and resources.
- Implement course and subject search.
- Populate breadcrumbs and subject metadata.

### Digital Library
- Load books, notes, journals, research papers and references.
- Implement resource search and category filters.
- Filter by academic field, programme, semester and subject.
- Link library resources to related course subjects.

### Book Locator
- Search the physical library catalogue.
- Display verified building, floor, section, rack, shelf and call number.
- Display verified availability and copy counts.
- Link book records to their detail pages.
- Never invent library location or inventory records.

### Book Details
- Populate title, author, edition, publisher, ISBN and description.
- Connect related subjects and resources.
- Link the physical-copy action to the relevant catalogue record.

### Exam Preparation
- Load semester examination, GATE, CDS, AFCAT and placement categories.
- Implement category and subject navigation.
- Connect revision notes, summaries, practice and reference material.

### Exam Details
- Populate examination syllabus and pattern.
- Render subjects, sections and topics.
- Connect topic notes, revision resources and practice questions.
- Integrate previous-year papers with their metadata.
- Distinguish official answer keys from independently prepared solutions.

### Student Profile
- Load authenticated student information.
- Populate programme, semester and academic details.
- Connect saved resources and learning activity.
- Respect the authentication and access-control design.

## Integration rules
1. Preserve existing page routes, IDs, classes and data attributes.
2. Keep JavaScript in the designated `js/` directory.
3. Avoid inline JavaScript in HTML.
4. Do not replace the page layouts with generated templates.
5. Keep data separate from rendering and application logic.
6. Validate imported data before rendering.
7. Do not execute uploaded JavaScript files supplied as academic data.
8. Use accessible labels and keyboard-friendly controls.
9. Provide clear empty, loading and error states.
10. Keep all user-specific data protected by backend access controls.

## Data structure direction
Use stable IDs for fields, programmes, semesters, subjects, resources, books and examinations.

Recommended hierarchy:

Academic field
  → Programme
    → Semester
      → Subject
        → Units
        → Resources
        → Books
        → PYQs

Examination
  → Subject or section
    → Topic
      → Notes
      → Revision material
      → Practice questions
      → PYQs

Resource records should include title, type, subject association, source, access URL and applicable rights/licence information.

Book records should include title, authors, edition, publisher, ISBN, catalogue ID and verified physical-location metadata where available.

PYQ records should include examination, year, session, paper code, subject/topic, question number, marks, answer source and rights/licence information.

## Important
The current frontend is a presentation layer. Search forms, filters and data areas are structural UI elements until the integration developer implements their behaviour. Ordinary page links provide the current navigation between available HTML pages.

## Previous-page navigation

Every inner HTML page contains a `.page-back-button` link with
`data-action="history-back"` and a fallback destination of `../index.html`.

JavaScript integration requirement:
- Detect clicks on elements with `data-action="history-back"`.
- If browser history has a usable previous entry, navigate using `history.back()`.
- Otherwise, follow the link's existing `href` fallback.
- Prevent the default link navigation only when handling browser history.
- Keep this behaviour in the shared application JavaScript.
- Do not add duplicate handlers to individual pages.

## IMPORTANT: True Previous-Page Navigation

The back button MUST behave like the browser Back button.

Required behaviour:
- Use the browser history stack with `window.history.back()`.
- Do NOT redirect every page to the homepage or dashboard.
- Do NOT use a fixed parent-page URL.
- Preserve the exact navigation sequence.

Example:
Homepage → Exam Preparation → Courses → Course Details

Back from Course Details must open Courses.
Back from Courses must open Exam Preparation.
Back from Exam Preparation must open Homepage.

Implementation:
- Target: `[data-action="history-back"]`
- Prevent the link's default navigation when browser history is available.
- Call `window.history.back()`.
- If no usable previous history entry exists, allow the existing homepage fallback link to work.
- Implement this once in the shared application JavaScript.

## CRITICAL FIX — Back Button Must Follow Actual Navigation History

The current back button incorrectly redirects users to the Dashboard.

This is NOT acceptable.

Every inner-page back button must return to the exact page from which the user entered the current page.

Example navigation:
Exam Preparation → AFCAT → Explore Courses → Course Details

Expected back navigation:
Course Details → Explore Courses → AFCAT → Exam Preparation

Implementation requirements for shared JavaScript:
1. Select all elements using `[data-action="history-back"]`.
2. On click, prevent the default link navigation.
3. If `window.history.length > 1`, call `window.history.back()`.
4. Do not replace browser history using `location.replace()`.
5. Do not redirect to `index.html` when a valid previous page exists.
6. Keep the homepage link only as a fallback for direct page entry with no usable previous page.
7. Do not treat an entire module as one history entry. Every actual page navigation must remain in browser history.
8. Register the handler once in shared application JavaScript.

Test the complete navigation sequence above, including all three Back actions.


<!-- ACEDEX_COURSES_HANDOVER_START -->
## Courses module frontend handover

### Approved navigation flow
Academic Field → Programme → Semester → Subject Detail.

### Frontend responsibilities
- HTML page structure and CSS presentation.
- Responsive layouts and accessible semantic markup.
- Stable IDs, classes and `data-*` attributes for integration.
- Static page-to-page links where appropriate.
- Clear loading, empty and unavailable states.

### Integration responsibilities
The JavaScript/data integration owner handles:
- Loading academic field, programme, semester and subject data.
- Dynamic page content and breadcrumb values.
- Search and filtering behaviour.
- Dynamic cards and resource lists.
- Bookmarking, progress, quizzes and user-specific state.
- Navigation state and browser history handling.

### Subject content model
The reusable Subject Detail page provides integration targets for:
- Subject overview, code, credits and description.
- Official syllabus and unit-wise topics.
- Short notes and quick revision material.
- Quizzes and practice questions.
- Important questions and previous year papers.
- Books, references, PDFs and presentations.

### Data integrity
Do not invent official LPU syllabus details, subject codes, credits, book availability, examination papers or physical library locations. Populate these sections only from verified academic data.

### Frontend boundary
This frontend handover does not introduce or modify JavaScript. Existing JavaScript files remain under the integration owner's responsibility.
<!-- ACEDEX_COURSES_HANDOVER_END -->


<!-- ACEDEX_LIBRARY_HANDOVER_START -->
## Digital Library frontend handover

The Digital Library is for academic resource discovery and access. It is not an e-commerce storefront.

The interface covers textbooks, references, lecture notes, research papers, journals, study material, presentations and previous year questions.

Resource filters should support academic field, programme, semester, subject, resource type, author and publication year.

Book/resource detail views should accommodate title, author, edition, publisher, subject, cover, description, availability, related resources and a Find This Book route where applicable.

The integration owner is responsible for dynamic search, filters, sorting, resource data, bookmarks and availability updates. Do not invent resource metadata or claim a book is available without verified inventory data.

The frontend owner is responsible for semantic HTML, responsive CSS, empty/loading states and stable integration hooks. No JavaScript is introduced by this work.
<!-- ACEDEX_LIBRARY_HANDOVER_END -->


<!-- ACEDEX_BOOK_LOCATOR_HANDOVER_START -->
## Physical Book Locator frontend handover

The Book Locator is designed to help students locate physical library inventory. It is not an online bookstore.

Each inventory record should support available verified fields:
- Book/resource identifier
- Title and author
- Subject
- Building
- Floor
- Section
- Rack
- Shelf
- Total copies
- Available copies
- Availability status

The integration owner handles inventory retrieval, search, filtering, sorting and live availability. The frontend provides the search/filter layout, result cards, location presentation, responsive styling and empty states.

Do not invent building names, floor numbers, rack identifiers, shelf locations, copy counts or availability. Do not add shopping-cart, checkout or payment functionality.
<!-- ACEDEX_BOOK_LOCATOR_HANDOVER_END -->

## Academic Field Pages – JavaScript Integration Handover

Six dedicated field pages are available in `pages/academic-fields/`.

The six page keys are:
- `computer-science-it`
- `engineering-technology`
- `management-commerce`
- `pharmaceutical-sciences`
- `agriculture`
- `law`

The page root exposes `data-academic-field` with the relevant field key.

Required integration:
1. Read the field key from `data-academic-field`.
2. Load only programmes mapped to that academic field.
3. Connect the course search input using `data-field-course-search`.
4. Render verified programme cards inside `[data-field-programmes]`.
5. Populate field-specific specialisations in `[data-field-specialisations]`.
6. Populate career information in `[data-field-careers]`.
7. Connect programme cards to the existing programme → semester → subject → reusable subject-detail hierarchy.
8. Preserve the existing shared subject-detail page; do not create duplicate subject systems.

The frontend currently provides static study-area and career examples for layout purposes. Verify all actual LPU programme names, availability and specialisations before presenting them as official offerings.

Do not add a Schools and Departments section. Do not create a separate placement preparation page. Placement preparation remains within Exam Preparation.

All JavaScript and academic data integration remain the teammate's responsibility. Do not modify the existing frontend HTML/CSS structure unnecessarily.

## Academic Field Page Integration Rules

The six field landing pages are static HTML/CSS frontend pages. The JavaScript/data teammate owns all dynamic functionality.

The field key is exposed through `data-academic-field`. Use this key to retrieve the matching academic data.

Required behaviour:
- Course search must be scoped to the currently opened field.
- Programme cards must show only programmes mapped to that field.
- Programme links must connect to the existing programme page.
- Semester links must connect to the existing semester page.
- Subject links must connect to the reusable `course-details.html` page.
- Specialisations and career information must be field-specific.
- Related resource links must preserve the existing Digital Library and Exam Preparation modules.

Do not create duplicate subject detail pages, a standalone placement module, or a Schools and Departments section.

Do not treat illustrative study areas as verified official LPU programme specialisations. Use the approved academic data source for official offerings.

## Profile and Common Student Features – Integration Handover

Frontend page: `pages/profile.html`
Stylesheet: `css/profile-pages.css`

The JavaScript/data integration teammate should connect:
1. Student profile information and academic details.
2. Saved resources and bookmarks.
3. Recently viewed programmes, subjects and resources.
4. Learning progress and activity summaries.
5. Quiz and mock-test history.
6. Student preferences.

Requirements:
- Populate information from the appropriate student record.
- Preserve empty states when no data exists.
- Reuse resource identifiers across modules.
- Do not fabricate student details, progress or quiz results.
- Keep dynamic functionality in the teammate-owned JavaScript layer.

---

# Semester Pages & Academic Path Integration

## 1. Semester Page Structure

The frontend contains 288 semester pages:

`pages/semesters/<specialisation-slug>/semester-<number>.html`

Example:
- `pages/semesters/artificial-intelligence-machine-learning/semester-1.html`
- `pages/semesters/artificial-intelligence-machine-learning/semester-2.html`

There are currently 8 placeholder semester pages for each of the 36 specialisations. These are frontend placeholders, not confirmation that every programme has eight semesters. The actual semester count must come from verified programme data.

## 2. Academic Path Explorer

Dashboard location: `index.html`

Existing controls:
- `#pathAcademicField` — selected academic field
- `#pathSpecialisation` — selected specialisation
- `#pathSemester` — selected semester
- `#exploreAcademicPath` — Explore action

Integration requirements:
1. Read the selected academic field.
2. Show only specialisations belonging to that field.
3. Keep the specialisation control disabled until a field is selected.
4. Populate valid semesters according to the selected programme.
5. Keep Explore disabled or show validation until all required selections are valid.
6. On Explore, navigate to the matching semester page using the selected specialisation slug and semester number.

Expected route pattern:

`pages/semesters/<specialisation-slug>/semester-<number>.html`

Do not send every selection to one fixed semester page.

## 3. Specialisation Semester Directory

Each file in `pages/specialisations/` contains a semester directory with links to its eight placeholder semester pages.

Relevant hooks:
- `data-specialisation-semesters`
- `data-semester-number`
- `data-specialisation-id`

The teammate should use verified programme data to show only the semesters available for the selected programme. Do not assume that all programmes have the same semester count.

## 4. Semester Page Data Hooks

Each semester page exposes:

- `data-specialisation-id` — specialisation slug
- `data-academic-field` — academic field slug
- `data-semester-number` — semester number
- `data-content-container="semester-workspace"` — semester workspace
- `data-content-container="semester-syllabus"` — syllabus area
- `data-content-container="semester-subjects"` — subject directory

Resource categories:
- `semester-notes`
- `semester-books`
- `semester-assignments`
- `semester-practicals`
- `semester-projects`
- `semester-pyqs`
- `semester-revision`

Populate these areas from the verified academic/resource data. Keep subject-level resources associated with the correct subject and semester.

## 5. Syllabus and Resource Downloads

The syllabus area currently contains a pending-upload state.

When a verified syllabus document is available:
- Display its correct document title.
- Provide a working download link.
- Use the actual file URL or project asset path supplied by the content/data layer.
- Do not create fake PDF links or placeholder download destinations.
- Show an unavailable state when no file exists.

Apply the same rule to notes, assignments, practical files, projects and PYQs. Resources that need detailed subject-wise navigation may open a dedicated resource page; simple files should offer direct downloads.

## 6. Subject-Level Navigation

The subject directory is currently a placeholder.

Once verified subject data is available, each subject should expose its name, course code and relevant metadata where supplied. Its resource links should lead to the correct subject material, not to another semester or specialisation.

## 7. Frontend Responsibility

The HTML/CSS frontend is already prepared. JavaScript, filtering, data loading, validation and navigation are the teammate's responsibility.

Do not duplicate the 288 HTML pages or replace the existing page structure when connecting the data. Preserve the existing IDs, classes and data attributes.

## 8. Academic Data Verification

The current semester count, subject list, course codes and syllabus files are placeholders until verified against the applicable programme curriculum. Do not present illustrative or unverified data as official LPU academic information.

