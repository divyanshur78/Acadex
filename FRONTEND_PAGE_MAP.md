# AcedeX Page and Component Map

| Page | Main purpose | Integration areas |
|---|---|---|
| index.html | Dashboard | Profile, search, module data |
| pages/courses.html | Course browser | Fields, programmes, semesters, subjects |
| pages/course-details.html | Subject details | Syllabus, units, resources, books |
| pages/digital-library.html | Digital library | Resource search and collections |
| pages/book-locator.html | Physical book locator | Catalogue, shelf location, availability |
| pages/book-details.html | Book details | Metadata, related resources, physical copy |
| pages/exam-preparation.html | Exam categories | Exam catalogue and resource collections |
| pages/exam-details.html | Exam workspace | Syllabus, topics, revision, PYQs |
| pages/profile.html | Student profile | Student identity and learning activity |

## Shared stylesheet
- `css/style.css`
- `css/components.css`
- `css/responsive.css`
- `css/course-pages.css`
- `css/library-pages.css`

## Existing integration scripts
The integration developer owns the JavaScript files in `js/`. The frontend implementation must not depend on them until they are connected by the integration developer.

## Navigation convention
All secondary pages are stored inside `pages/`. Links from those pages to the dashboard use `../index.html`; links to other secondary pages use filenames within the same directory.


<!-- ACEDEX_COURSES_MAP_START -->
## Courses module — approved page hierarchy

The Courses module follows this fixed academic hierarchy:

1. `pages/courses.html` — six academic fields.
2. `pages/programme.html` — programmes within the selected field.
3. `pages/semester.html` — semesters within the selected programme.
4. `pages/course-details.html` — reusable Subject Detail template.

### Integration hooks

| Page | Main integration hooks |
|---|---|
| Courses | `courseContent`, `courseBreadcrumbs`, `courseSearch` |
| Programme | `programmeTitle`, `programmeDescription`, `programmeMeta`, `programmeOverview`, `programmeSemesterGrid` |
| Semester | `semesterTitle`, `semesterDescription`, `semesterMeta`, `semesterOverview`, `semesterSubjectGrid`, `semesterResources` |
| Subject | `subjectTitle`, `subjectDescription`, `subjectMeta`, `subjectOverview`, `subjectUnits`, `subjectResources` |

### Subject Detail content containers

- `subject-units`
- `short-notes`
- `quick-revision`
- `quizzes`
- `important-questions`
- `previous-year-questions`
- `books-references`
- `subject-resources`

These are frontend integration targets. Dynamic data, search, filtering, navigation state and rendering belong to the JavaScript/data integration owner.

<!-- ACEDEX_COURSES_MAP_END -->


<!-- ACEDEX_LIBRARY_MAP_START -->
## Digital Library — approved structure

### Main resource categories
- Textbooks
- Reference books
- Lecture notes
- Research papers
- Journals
- Study material
- Presentations
- Previous year questions

### Resource discovery filters
- Academic field
- Programme
- Semester
- Subject
- Resource type
- Author
- Publication year

### Resource details
Each resource should support the available verified metadata:
- Title
- Author
- Edition
- Publisher
- Subject
- Cover
- Description
- Availability
- Related resources
- Find This Book

### Existing page files
- `pages/digital-library.html` — resource discovery and browsing.
- `pages/book-details.html` — reusable resource/book details.

### Integration boundary
Search, filters, sorting, dynamic resource cards, bookmarks and data loading are handled by the JavaScript/data integration owner. HTML/CSS provide the presentation and integration hooks.

<!-- ACEDEX_LIBRARY_MAP_END -->


<!-- ACEDEX_BOOK_LOCATOR_MAP_START -->
## Physical Book Locator

The Book Locator helps students find physical books inside the university library.

### Location information
- Library building
- Floor
- Section
- Rack
- Shelf
- Copy availability

### Search and filters
- Book title
- Author
- Subject
- Programme
- Availability
- Library location

### Page
- `pages/book-locator.html` — physical library search and location discovery.
- `pages/book-details.html` — reusable resource/book details, including a route to physical availability where applicable.

### Important boundary
This module is not an e-commerce store. It must not include cart, checkout, payment or purchasing flows. Library inventory and location details must come from verified university data.

<!-- ACEDEX_BOOK_LOCATOR_MAP_END -->

## Dedicated Academic Field Pages

Each of the six academic fields has an individual landing page under `pages/academic-fields/`.

| Academic field | Page |
|---|---|
| Computer Science & IT | `academic-fields/computer-science-it.html` |
| Engineering & Technology | `academic-fields/engineering-technology.html` |
| Management & Commerce | `academic-fields/management-commerce.html` |
| Pharmaceutical Sciences | `academic-fields/pharmaceutical-sciences.html` |
| Agriculture | `academic-fields/agriculture.html` |
| Law | `academic-fields/law.html` |

Each page contains:
- Field-specific overview and introduction
- Course/programme search integration hook
- Programme listing container
- Field-specific study areas and specialisations
- Programme → Semester → Subject pathway
- Career opportunity section
- Related Digital Library and Exam Preparation links

There is intentionally no Schools and Departments section.

Integration hooks:
- `data-academic-field`
- `data-field-course-search`
- `data-field-programmes`
- `data-field-specialisations`
- `data-field-careers`
- `data-content-container`

Programme, specialisation and career data must be verified before dynamic population. The HTML contains illustrative study areas and career directions, not a confirmed list of LPU offerings.

## Academic Field Page Navigation

The Courses landing page should link each academic field card to its dedicated page.

| Field | Destination |
|---|---|
| Computer Science & IT | `pages/academic-fields/computer-science-it.html` |
| Engineering & Technology | `pages/academic-fields/engineering-technology.html` |
| Management & Commerce | `pages/academic-fields/management-commerce.html` |
| Pharmaceutical Sciences | `pages/academic-fields/pharmaceutical-sciences.html` |
| Agriculture | `pages/academic-fields/agriculture.html` |
| Law | `pages/academic-fields/law.html` |

All six pages use the shared stylesheet `css/academic-field-pages.css`.

The field pages provide a common layout with field-specific content:
- Overview
- Course search and programme results
- Specialisations and study areas
- Programme-to-semester-to-subject pathway
- Career opportunities
- Related learning resources

Schools and Departments are intentionally excluded.

## Profile and Student Dashboard

Page: `pages/profile.html`
Stylesheet: `css/profile-pages.css`

Profile features:
- Student information and academic identity
- Programme, academic field and semester
- Saved resources and bookmarks
- Recently viewed courses and resources
- Learning progress
- Quiz and mock-test history
- Student preferences

All these features remain within the existing Profile page.
