# AcedeX — Student Academic Personalisation
## Complete JavaScript and Backend Integration Handoff

**Purpose:** This document is the implementation specification for the JavaScript teammate or an AI assistant working on AcedeX. Read this document together with `FRONTEND_INTEGRATION_GUIDE.md` and `FRONTEND_PAGE_MAP.md` before changing code.

**Frontend ownership:** Member 2 owns the HTML/CSS UI. The JavaScript teammate owns JavaScript behaviour, data integration and coordination with the backend. Do not ask Member 2 to implement JavaScript.

---

# 1. Project objective

AcedeX must show each authenticated student the academic content relevant to their own saved academic profile.

After registration and login, the application should identify the student's:

- Programme, such as B.Tech or M.Tech.
- Academic field or branch.
- Specialisation, where applicable.
- Admission batch or curriculum year.
- Current semester.
- Academic year, where applicable.
- Enrolled subjects and their identifiers.

The same academic identity must be used consistently across the dashboard, courses, digital library, book locator, semester preparation and subject-specific learning pages.

A student should not have to select their branch and semester repeatedly on every page when those details are already saved in their profile.

The website must not assume that all students in one programme share the same curriculum. Curriculum can differ by programme, branch, specialisation, admission batch and academic year.

# 2. Important implementation rules

1. Inspect the existing project before writing or replacing JavaScript.
2. Preserve existing working functionality, routes, page layouts and script integrations.
3. Do not create duplicate event listeners, duplicate API calls or competing profile stores.
4. Do not rename or remove existing HTML IDs, classes or data attributes without checking every page and coordinating with the frontend owner.
5. Use stable database IDs for programme, field, specialisation, semester, subject and resource relationships. Do not use display names as database identifiers.
6. Do not hardcode one student's branch, semester, subjects or resources.
7. Do not treat browser local storage as the authoritative student profile.
8. The backend must validate the authenticated student and enforce access to the correct records.
9. Never expose passwords, session secrets, private student data or privileged API credentials in frontend JavaScript.
10. Do not invent API endpoints and assume they already exist. Inspect the backend first, then agree on the actual API contract.
11. Keep competitive exam preparation such as GATE, CDS, AFCAT and placement preparation separate from university-semester filtering. Those tracks should remain accessible to students even when their university branch differs.
12. Do not replace verified university curriculum with guessed subject lists. Verify the relevant programme and batch curriculum before publishing it.

# 3. Existing page structure and integration locations

The following paths and hooks were observed in the current HTML inspection. Recheck the live files before implementation because the project may have changed since this inspection.

## A. Dashboard — `index.html`

Existing location:
- Main content begins with `<main class="main-content">`.
- Topbar contains the student profile link.
- The dashboard profile link points to `pages/profile.html`.

Existing integration hooks:
- `[data-user-initials]`
- `[data-user-name]`
- `[data-user-program]`
- `.semester-indicator`

JavaScript responsibilities:
- Load the authenticated student's profile when the dashboard starts.
- Update the user's name, initials and programme in the topbar.
- Display the student's current semester and academic context.
- Populate dashboard subject/course summaries using the saved profile.
- Show only relevant university learning resources.
- Keep general announcements or general exam-preparation content available where appropriate.

Do not create a second profile-fetching mechanism if a shared profile service already exists.

## B. Student profile — `pages/profile.html`

Existing location:
- Main content begins with `<main class="library-container">`.
- The page already contains an Academic Information card.
- The card contains Registration Number, Programme, Academic Field, Current Semester, School and Academic Year.

Existing integration location:
- The heading `Academic Information` identifies the academic information card.
- The academic values are currently displayed as static placeholder text.

JavaScript responsibilities:
- Fetch and display the authenticated student's profile.
- Replace placeholder values with backend-provided values.
- Display the correct student name and registration details.
- Support profile editing only for fields that the backend permits students to change.
- Validate changes and submit them to the backend.
- Refresh the shared academic profile after a successful update.
- Handle missing, incomplete or invalid academic information.

If editable form controls do not exist, coordinate the required HTML controls with the frontend owner. Do not silently redesign or remove the profile page.

## C. Courses — `pages/courses.html`

Existing location:
- Main content begins with `<main class="course-workspace">`.
- Course hero contains `#courseSearch`.
- Breadcrumb navigation uses `#courseBreadcrumbs`.
- Section heading uses `#courseSectionTitle` and `#courseSectionDescription`.
- Dynamic catalogue content is placed inside `#courseContent`.

Existing integration hooks:
- `#courseSearch`
- `#courseBreadcrumbs`
- `#courseSectionTitle`
- `#courseSectionDescription`
- `#courseContent`

JavaScript responsibilities:
- Load the academic catalogue.
- Restrict the student's university course browsing to their applicable programme, field, specialisation and curriculum batch.
- Display semesters available for that curriculum.
- Display subjects belonging to the selected semester.
- Display subject details and associated learning resources.
- Make the search work against the catalogue currently available to the student.
- Keep breadcrumb navigation consistent with the selected academic hierarchy.
- Handle empty results and loading failures.

The existing course page is designed around a catalogue hierarchy. Preserve its existing structure and inspect the current JavaScript before connecting data.

## D. Digital Library — `pages/digital-library.html`

Existing location:
- Main content begins with `<main class="library-container">`.
- The hero contains a library search form.
- The Explore Collections section contains Academic Books, Lecture Notes and Research Papers cards.

JavaScript responsibilities:
- Load library resources relevant to the student's subjects and semester.
- Support searching by book title, author, subject or resource title, according to available backend fields.
- Filter university study resources using the student's academic context.
- Preserve access to general reference and research collections where appropriate.
- Show resource details, availability and navigation links.
- Avoid displaying unrelated semester notes as if they belong to the student's curriculum.

The digital library must not be reduced to only one semester's books. General reference resources can remain available.

## E. Book Locator — `pages/book-locator.html`

Existing location:
- Main content begins with `<main class="library-container">`.
- The page has a book search form.
- The Book Location Details panel displays Building, Floor, Section, Rack/Shelf, Call Number and Availability.

JavaScript responsibilities:
- Search the physical library catalogue.
- Display verified physical location records.
- Connect a book to relevant subjects where that relationship exists.
- Show building, floor, section, rack/shelf and call number from actual records.
- Show availability only when supported by current library data.
- Handle books with missing or unverified location information.

Do not fabricate shelf locations or availability. A book's academic relevance and its physical location are separate data relationships.

## F. Exam Preparation — `pages/exam-preparation.html`

Existing location:
- Main content begins with `<main class="library-container exam-container">`.
- Exam categories use cards with `data-exam-category`.

JavaScript responsibilities:
- Keep the semester preparation track relevant to the student's saved university profile.
- Keep GATE, CDS, AFCAT and placement preparation available as separate general preparation tracks.
- Do not filter competitive exam tracks using the student's university semester.
- Load the appropriate exam track and resource data.

## G. Semester Preparation — `pages/exams/semester-preparation.html`

Existing location:
- Main content begins with `<main class="library-container track-container">`.
- Page body includes the semester exam category.
- Main sections include syllabus, notes, books, practice and learning resources.

Existing integration hooks observed in the project:
- `data-specialisation-id`
- `data-academic-field`
- `data-semester-number`
- `data-content-container`
- `data-exam-category="semester"`

JavaScript responsibilities:
- Resolve the student's saved academic profile.
- Load the curriculum for the matching programme, field, specialisation and batch.
- Display the correct semester subjects and syllabus.
- Populate syllabus, notes, books and practice containers with matching resources.
- Keep PYQs associated with the correct subject, semester, programme and applicable year.
- Do not show a subject from another branch or curriculum as if it belongs to this student.

The existing disclaimer about differences between programme and academic-year curricula must be preserved.

## H. Four separate semester learning pages

These pages already exist:

- `pages/exams/unit-wise-notes.html`
- `pages/exams/concept-summaries.html`
- `pages/exams/definitions-formulas.html`
- `pages/exams/solved-examples.html`

Existing integration hooks observed:
- `[data-academic-selection]`
- `[data-filter="programme"]`
- `[data-filter="semester"]`
- `[data-selected-programme]`
- `[data-semester-number]`
- `[data-content-container]`
- `[data-specialisation-id]`
- `[data-academic-field]`

JavaScript responsibilities:
- Resolve the saved academic profile.
- Display the student's programme, field and semester.
- Load the subjects available to that student.
- Display only the notes belonging to the selected subject and applicable curriculum.
- Keep unit-wise notes, concept summaries, definitions/formulas and solved examples in their respective pages.
- Support subject selection if the current HTML provides the required control.
- Preserve the existing page navigation and back links.
- Handle a student with no matching notes without displaying another student's material.

If the current selection elements are display-only placeholders rather than real controls, coordinate with the frontend owner before adding controls.

# 4. Recommended academic data hierarchy

Use a relational structure or an equivalent backend model with stable IDs.

Recommended hierarchy:

Institution
  -> Programme
    -> Academic Field / Branch
      -> Specialisation (optional)
        -> Admission Batch / Curriculum Version
          -> Semester
            -> Subject
              -> Units / Topics
                -> Notes / Summaries / Definitions / Formulas / Solved Examples

Additional relationships:

- Subject -> Recommended Books
- Subject -> Library Resources
- Book -> Physical Library Location
- Subject -> Quizzes and Practice Questions
- Subject -> Previous-Year Questions
- Exam Track -> Competitive Exam Resources

Do not assume every subject must have every resource type.

Recommended record identifiers:
- student_id
- programme_id
- academic_field_id
- specialisation_id (nullable where not applicable)
- curriculum_id
- admission_batch_id
- semester_id
- subject_id
- unit_id
- resource_id
- book_id
- library_location_id

Use nullable relationships only where the data model permits them. Confirm the actual backend schema before implementing queries.

# 5. Student profile data contract

The authenticated profile response should provide enough information to resolve the student's academic context.

Suggested logical response:

{
  "student": {
    "id": "stable-student-id",
    "name": "Student Name",
    "registration_number": "student-registration",
    "email": "student-email"
  },
  "academic_profile": {
    "programme_id": "programme-id",
    "programme_name": "B.Tech",
    "academic_field_id": "field-id",
    "academic_field_name": "Computer Science and Engineering",
    "specialisation_id": "specialisation-id-or-null",
    "specialisation_name": "Specialisation-or-null",
    "admission_batch_id": "batch-id",
    "curriculum_id": "curriculum-id",
    "current_semester_id": "semester-id",
    "current_semester_number": 1,
    "academic_year": "academic-year"
  },
  "profile_status": "complete"
}

This is an illustrative contract, not a claim that the backend already returns this JSON. Adapt field names to the actual backend.

The profile should also support a clear incomplete state when required academic fields are missing.

# 6. API contract to agree with the backend team

Before implementing fetch calls, inspect the existing backend routes, authentication system, database models and response formats.

The following are suggested API responsibilities, not existing guaranteed endpoints:

| Responsibility | Suggested endpoint |
|---|---|
| Get authenticated student profile | `GET /api/student/profile` |
| Update permitted profile fields | `PATCH /api/student/profile` |
| Get academic catalogue | `GET /api/academic/catalogue` |
| Get student's applicable curriculum | `GET /api/student/curriculum` |
| Get student's semester subjects | `GET /api/student/subjects` |
| Get resources for a subject | `GET /api/subjects/{subject_id}/resources` |
| Search library catalogue | `GET /api/library/search` |
| Get physical book location | `GET /api/library/books/{book_id}/location` |
| Get semester preparation data | `GET /api/student/semester-resources` |

The backend team must decide the final URLs, authentication method, query parameters and response formats.

Every student-specific endpoint must derive or validate the student identity from the authenticated session/token. Never trust a student_id supplied by the browser as proof of access.

The backend must verify that requested subject and resource IDs belong to the student's permitted curriculum or are otherwise publicly available.

# 7. JavaScript architecture

Use a shared implementation rather than repeating profile and filtering logic on every page.

Suggested organisation, subject to the existing project structure:

js/
  services/
    api.js
    auth-service.js
    student-profile-service.js
    academic-catalogue-service.js
    resource-service.js
  modules/
    academic-context.js
    dashboard-academic.js
    profile-academic.js
    courses-academic.js
    library-academic.js
    book-locator.js
    exam-academic.js
    semester-preparation.js
    semester-notes.js

These are proposed files, not a requirement to duplicate files that already exist. Inspect the current `js/` directory first. Reuse and extend existing modules where sensible.

Responsibilities:

**API service**
- Centralise requests and response handling.
- Apply the existing authentication mechanism.
- Handle HTTP errors and expired sessions consistently.
- Avoid exposing secrets.

**Student profile service**
- Fetch the authenticated student's profile.
- Normalise the profile response into one consistent in-memory representation.
- Provide profile data to page modules.
- Refresh the profile after a permitted update.
- Do not treat local storage as the source of truth.

**Academic context service**
- Resolve programme, field, specialisation, curriculum and semester IDs.
- Provide shared filtering parameters.
- Keep the profile consistent across pages.
- Avoid separate pages maintaining conflicting copies of the same academic identity.

**Page modules**
- Run only on pages where their required elements exist.
- Use the existing HTML integration hooks.
- Render data into the correct containers.
- Keep page-specific behaviour separate from shared profile logic.

# 8. Script loading and page initialisation

Inspect each page's existing script tags before adding anything.

Recommended approach:
- Load shared dependencies before page-specific modules.
- Use the existing project script-loading convention.
- Prefer `defer` or the existing module strategy where appropriate.
- Avoid loading the same script twice.
- Avoid inline JavaScript if the project already uses external JS files.
- Ensure a page module checks for its required DOM elements before running.
- Do not make every page load every page-specific module.

Suggested initialisation sequence:

1. Wait until the page DOM is ready.
2. Check whether the page requires an authenticated student.
3. Check the current authentication state.
4. Fetch the authenticated student's academic profile.
5. Handle an expired session or incomplete profile.
6. Initialise the shared academic context.
7. Initialise the page-specific module.
8. Fetch and render the relevant resources.
9. Display an appropriate loading, empty, error or success state.

Do not implement this sequence twice in different scripts. Use one shared entry point or the project's existing initialisation pattern.

# 9. Filtering rules

University semester content must match all applicable dimensions:

- Programme ID
- Academic field / branch ID
- Specialisation ID, if applicable
- Curriculum or admission batch ID
- Semester ID
- Subject ID

A resource should be displayed only when its curriculum relationship is valid.

Do not filter solely by a text label such as "B.Tech" or "Semester 1".

For general resources:
- General reference books may be available across programmes.
- Research papers may be available across programmes.
- GATE, CDS, AFCAT and placement resources should remain independently accessible.
- A resource with no branch restriction must be explicitly marked as general or shared in the data model.

# 10. Registration, login and profile changes

Registration:
- Collect the academic information required by the agreed backend model.
- Use valid IDs from the academic catalogue wherever possible.
- Validate required fields.
- Do not allow arbitrary programme or semester labels to become trusted academic records.

Login:
- Authenticate using the existing authentication system.
- Fetch the profile from the backend after authentication.
- Route incomplete profiles to the appropriate profile-completion flow.
- Do not display personalised academic resources until the required profile context is resolved.

Profile updates:
- Allow only fields the backend permits students to update.
- Validate changes on the backend.
- Refresh the shared profile after a successful update.
- Re-render affected page content.
- Preserve academic history and previous learning progress where the backend supports it.

Semester progression:
- Do not simply overwrite academic history.
- Update the current semester through the approved backend process.
- Preserve prior semester records, completed learning activity and progress.
- Load the new semester's subjects and resources only after the backend confirms the change.

# 11. UI states and error handling

Every data-driven section should handle:

**Loading**
- Show a clear loading state while the request is in progress.
- Avoid showing stale content as if it belongs to the current student.

**Success**
- Render only validated records relevant to the student's profile.

**Empty**
- Explain that no matching resources are currently available.
- Do not silently substitute another branch's resources.

**Incomplete profile**
- Explain which academic information is missing.
- Provide a link to the profile page.

**Unauthenticated**
- Use the project's existing login flow.
- Do not expose student-specific content.

**Expired session**
- Handle the response consistently and require re-authentication through the existing system.

**Server or network failure**
- Display a readable error and a retry option where appropriate.
- Do not clear a valid profile merely because one resource request failed.

# 12. Security and data integrity

- Authentication and authorisation must be enforced by the backend.
- Never rely on hidden HTML, disabled controls or frontend filtering for security.
- Validate all submitted IDs and relationships on the server.
- Do not allow a student to request another student's private profile or progress.
- Do not expose private student data in public catalogue responses.
- Use the existing CSRF protection if cookie-based authentication is used.
- Validate uploaded academic resources through the backend.
- Do not render untrusted content as raw HTML.
- Do not publish unverified curriculum or library-location data.

# 13. Coordination with the HTML/CSS owner

The HTML/CSS owner has already created page structures and integration placeholders.

Before asking for additional markup:
1. Check whether an existing ID, class or data attribute can be reused.
2. Check whether a required form or control already exists elsewhere.
3. Explain which exact page and section needs a new element.
4. Specify the required ID, class, data attribute, input type and expected behaviour.
5. Keep new markup consistent with the existing design.
6. Do not ask the HTML/CSS owner to write JavaScript.

If the existing HTML does not provide a control needed for a feature, coordinate the markup change instead of inserting a large new UI through JavaScript.

# 14. Required testing checklist

## Account and profile
- [ ] A newly registered student receives a valid academic profile.
- [ ] Login loads the correct profile.
- [ ] Dashboard name, initials and programme are correct.
- [ ] Profile page displays the correct academic details.
- [ ] Incomplete profiles are handled clearly.
- [ ] Profile updates are validated and persisted.

## Academic catalogue
- [ ] B.Tech and M.Tech catalogues are not mixed incorrectly.
- [ ] Different academic fields show their own curriculum.
- [ ] Specialisations are handled where applicable.
- [ ] Admission batch and curriculum version are respected.
- [ ] Semester subjects match the correct curriculum.

## Website-wide personalisation
- [ ] Dashboard shows relevant academic information.
- [ ] Courses displays the correct programme and subjects.
- [ ] Digital Library filters relevant semester resources.
- [ ] Book Locator displays verified physical location data.
- [ ] Semester Preparation shows the correct syllabus and subjects.
- [ ] All four separate notes pages load matching subject content.
- [ ] Competitive exam tracks remain available independently.

## Edge cases and security
- [ ] A student with no matching notes sees an empty state.
- [ ] A failed API request does not show another student's resources.
- [ ] A student cannot access another student's private profile by changing an ID.
- [ ] An expired session is handled.
- [ ] A semester change refreshes the correct content.
- [ ] Previous academic progress is not accidentally erased.
- [ ] No duplicate event listeners or repeated requests are introduced.
- [ ] Existing page navigation and current functionality still work.

# 15. Definition of completion

The implementation is complete only when:

1. The authenticated student's academic profile is fetched from the backend.
2. The same profile context is used consistently across all relevant pages.
3. Programme, branch, specialisation, batch and semester relationships are validated.
4. University resources are filtered using stable IDs and the applicable curriculum.
5. General competitive exam resources remain independently accessible.
6. Physical book location information comes from verified library records.
7. Loading, empty, incomplete-profile, error and session states work.
8. Backend access control is tested.
9. Existing AcedeX functionality remains intact.
10. The integration guide and API contract are updated to reflect the actual implementation.

---

# 16. Instructions for the GPT or developer continuing this work

When continuing AcedeX JavaScript integration:

1. Read this entire handoff first.
2. Read `FRONTEND_INTEGRATION_GUIDE.md` and `FRONTEND_PAGE_MAP.md`.
3. Inspect the existing `js/` folder and backend before editing.
4. Inspect the exact HTML hooks listed in this document.
5. Report which relevant JavaScript and backend files already exist.
6. Identify missing backend endpoints or data relationships before assuming they exist.
7. Propose the smallest safe implementation plan.
8. Implement one coherent stage at a time.
9. Preserve the HTML/CSS owner's page structures and existing content.
10. Test the affected pages and report exactly what is implemented, what remains and what requires backend support.

**Do not assume that a suggested endpoint, module filename or JSON response in this document already exists. These are implementation recommendations to be reconciled with the actual codebase.**
