/**
 * ACADEX - DYNAMIC ACADEMIC FIELD & SEMESTER NAVIGATOR
 * Complies with the field-specific academic structures specified in Section 6 & 7:
 * - Computer Science & IT: Specialisations -> Semesters 1-8 -> Courses & PDFs
 * - Engineering & Technology: Branches -> Semesters 1-8 -> Courses & PDFs
 * - Agriculture: Semesters 1-8 directly (no specialisation screen) -> Courses & PDFs
 * - Law: Semesters 1-10 directly (no specialisation screen) -> Courses & PDFs
 * - Pharmacy: Semesters 1-8 directly (no specialisation screen) -> Courses & PDFs
 * - Management: Programs (BBA / MBA, 6 semesters each) -> Courses & PDFs
 */

(() => {
  'use strict';

  const $ = (s, root = document) => root.querySelector(s);
  const $$ = (s, root = document) => [...root.querySelectorAll(s)];

  // Academic Fields Definition
  const academicFields = {
    'computer-science-it': {
      id: 'computer-science-it',
      name: 'Computer Science & IT',
      badge: '⌘',
      theme: 'field-blue',
      kicker: 'COMPUTING & INFORMATION TECHNOLOGY',
      description: 'Computer Science and Information Technology focus on the design, development and understanding of software, computing systems, data and digital technologies.',
      structureType: 'specialisation', // CS & IT uses specialisations
      levelLabel: 'SELECT SPECIALISATION / STUDY AREA',
      options: [
        {
          id: 'AI-ML',
          name: 'Artificial Intelligence & Machine Learning',
          description: 'Intelligent systems, deep neural networks, machine learning models, computer vision and natural language processing.',
          semesters: 8
        },
        {
          id: 'Data-Science',
          name: 'Data Science & Analytics',
          description: 'Statistical modeling, big data architectures, data engineering, visualization and quantitative decision analysis.',
          semesters: 8
        },
        {
          id: 'Cybersecurity',
          name: 'Cybersecurity',
          description: 'Network defense, cryptography, secure coding, penetration testing, digital forensics and security architectures.',
          semesters: 8
        },
        {
          id: 'Software-Engineering',
          name: 'Software Engineering',
          description: 'Modern software engineering principles, agile architectures, testing methodologies, DevOps and distributed systems.',
          semesters: 8
        },
        {
          id: 'Cloud-Computing',
          name: 'Cloud Computing',
          description: 'Cloud native systems, container orchestration, microservices, virtualization, serverless computing and cloud infrastructure.',
          semesters: 8
        },
        {
          id: 'IoT',
          name: 'Internet of Things',
          description: 'Connected smart devices, embedded hardware, sensor networks, edge analytics and IoT communication protocols.',
          semesters: 8
        },
        {
          id: 'Core',
          name: 'Computer Science – Core',
          description: 'Foundational computer science theory, algorithms, data structures, operating systems, compiler design and architecture.',
          semesters: 8
        }
      ]
    },

    'engineering-technology': {
      id: 'engineering-technology',
      name: 'Engineering & Technology',
      badge: '⌁',
      theme: 'field-purple',
      kicker: 'ENGINEERING DISCIPLINES',
      description: 'Explore core engineering disciplines, applied technical sciences, and innovation across university curriculum.',
      structureType: 'branch', // Engineering uses Branches, not CS-style specialisations!
      levelLabel: 'SELECT ENGINEERING BRANCH',
      options: [
        {
          id: 'Civil',
          name: 'Civil Engineering',
          description: 'Structural engineering, mechanics of materials, geotechnical design, surveying, environmental and transportation engineering.',
          semesters: 8
        },
        {
          id: 'Mechanical',
          name: 'Mechanical Engineering',
          description: 'Thermodynamics, fluid mechanics, kinematics, machine design, manufacturing technology and automotive systems.',
          semesters: 8
        },
        {
          id: 'Electrical',
          name: 'Electrical Engineering',
          description: 'Electric circuits, electrical machines, power systems, control systems, analog and digital electronics.',
          semesters: 8
        }
      ]
    },

    'agriculture': {
      id: 'agriculture',
      name: 'Agriculture',
      badge: '❋',
      theme: 'field-lime',
      kicker: 'AGRICULTURAL SCIENCES',
      description: 'Explore agricultural science, crop cultivation systems, soil management, agronomy and sustainable agricultural technologies.',
      structureType: 'direct-semesters', // Direct semester flow: no specialisation selection screen!
      semesters: 8
    },

    'law': {
      id: 'law',
      name: 'Law',
      badge: '⚖',
      theme: 'field-rose',
      kicker: 'LEGAL STUDIES',
      description: 'Explore jurisprudence, constitutional legislation, criminal law, corporate legal frameworks, human rights and justice systems.',
      structureType: 'direct-semesters', // Direct semester flow: no specialisation selection screen!
      semesters: 10 // Exactly 10 semesters!
    },

    'pharmaceutical-sciences': {
      id: 'pharmaceutical-sciences',
      name: 'Pharmaceutical Sciences',
      badge: '✚',
      theme: 'field-green',
      kicker: 'PHARMACY & DRUG DEVELOPMENT',
      description: 'Explore pharmaceutical chemistry, pharmaceutics, pharmacology, pharmacognosy, clinical research and drug regulatory affairs.',
      structureType: 'direct-semesters', // Direct semester flow: no specialisation selection screen!
      semesters: 8
    },

    'management-commerce': {
      id: 'management-commerce',
      name: 'Management & Commerce',
      badge: '▥',
      theme: 'field-orange',
      kicker: 'BUSINESS & MANAGEMENT STUDIES',
      description: 'Explore business strategy, marketing, corporate finance, organizational leadership, accounting and entrepreneurship.',
      structureType: 'program', // Contains exactly two programs: BBA and MBA, 6 semesters each!
      levelLabel: 'SELECT ACADEMIC PROGRAM',
      options: [
        {
          id: 'bba',
          name: 'BBA — Bachelor of Business Administration',
          description: 'Undergraduate business administration covering management principles, marketing, business economics, finance and operations.',
          semesters: 6
        },
        {
          id: 'mba',
          name: 'MBA — Master of Business Administration',
          description: 'Postgraduate management studies focusing on strategic leadership, corporate finance, organizational analysis and market dynamics.',
          semesters: 6
        }
      ]
    }
  };

  // State
  let activeFieldId = null;
  let activeOptionId = null; // Spec id, Branch id, or Program id
  let activeSemesterNumber = 1;

  // Clean title formatter
  function formatCourseTitle(resource) {
    if (resource.title && resource.title.trim()) {
      let t = resource.title.replace(/\.pdf$/i, '').replace(/[-_]/g, ' ');
      // Capitalize cleanly
      return t.replace(/\b\w/g, l => l.toUpperCase());
    }
    let fn = resource.fileName.replace(/\.pdf$/i, '').replace(/[-_]/g, ' ');
    return fn.replace(/\b\w/g, l => l.toUpperCase());
  }

  // Get matching resources from ACADEX_RESOURCES
  function getMatchingResources(fieldId, optionId, semesterNum) {
    const all = window.ACADEX_RESOURCES?.resources || [];
    const sem = Number(semesterNum);

    return all.filter(r => {
      if (Number(r.semester) !== sem) return false;

      if (fieldId === 'computer-science-it') {
        return r.programme === 'BTech' && r.branch === 'CSE' && r.specialisation === optionId;
      }
      if (fieldId === 'engineering-technology') {
        return r.programme === 'BTech' && r.branch === optionId;
      }
      if (fieldId === 'management-commerce') {
        return r.programme === 'Management' && (r.branch || '').toLowerCase() === (optionId || '').toLowerCase();
      }
      if (fieldId === 'agriculture') {
        return r.programme === 'Agriculture';
      }
      if (fieldId === 'law') {
        return r.programme === 'Law';
      }
      if (fieldId === 'pharmaceutical-sciences') {
        return r.programme === 'Pharmacy';
      }
      return false;
    });
  }

  // Determine path prefix to viewer (checking if currently inside pages/ or at root)
  function getViewerPath() {
    return window.location.pathname.includes('/pages/') ? 'pdf-viewer.html' : 'pages/pdf-viewer.html';
  }

  // Render the academic navigator into a target container
  function initAcademicNavigator(containerId = 'academicNavigatorPanel') {
    const container = document.getElementById(containerId);
    if (!container) return;

    // Open a specific field
    function openField(fieldId, autoSelectOption = null, autoSelectSemester = 1) {
      const field = academicFields[fieldId];
      if (!field) return;

      activeFieldId = fieldId;
      activeOptionId = autoSelectOption;
      activeSemesterNumber = autoSelectSemester;

      container.hidden = false;
      container.innerHTML = '';

      // Header
      const topDiv = document.createElement('div');
      topDiv.className = 'navigator-top';

      const titleCol = document.createElement('div');
      titleCol.innerHTML = `
        <div class="section-kicker">${field.kicker}</div>
        <h2>${field.name}</h2>
        <p>${field.description}</p>
      `;

      const backBtn = document.createElement('button');
      backBtn.className = 'navigator-back-btn';
      backBtn.type = 'button';
      backBtn.innerHTML = '← All Academic Fields';
      backBtn.addEventListener('click', () => {
        container.hidden = true;
        const grid = document.getElementById('academicFieldGrid') || document.getElementById('academicFieldsSection');
        if (grid) grid.scrollIntoView({ behavior: 'smooth', block: 'start' });
      });

      topDiv.append(titleCol, backBtn);
      container.appendChild(topDiv);

      // Branch/Specialisation/Program level (if applicable)
      if (field.structureType !== 'direct-semesters') {
        const stepLabel = document.createElement('div');
        stepLabel.className = 'navigator-step-label';
        stepLabel.textContent = field.levelLabel;
        container.appendChild(stepLabel);

        const chipsGrid = document.createElement('div');
        chipsGrid.className = 'navigator-chips-grid';

        // Select first option by default if none specified
        if (!activeOptionId && field.options.length) {
          activeOptionId = field.options[0].id;
        }

        field.options.forEach(opt => {
          const chip = document.createElement('button');
          chip.type = 'button';
          chip.className = 'navigator-chip' + (opt.id === activeOptionId ? ' active' : '');
          chip.textContent = opt.name;
          chip.addEventListener('click', () => {
            $$('.navigator-chip', chipsGrid).forEach(c => c.classList.remove('active'));
            chip.classList.add('active');
            activeOptionId = opt.id;
            renderSemestersAndCourses();
          });
          chipsGrid.appendChild(chip);
        });

        container.appendChild(chipsGrid);
      }

      // Container for Semesters and Courses
      const dynamicArea = document.createElement('div');
      dynamicArea.id = 'navigatorDynamicArea';
      container.appendChild(dynamicArea);

      renderSemestersAndCourses();
      container.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }

    // Render Semesters & Course resources
    function renderSemestersAndCourses() {
      const dynamicArea = document.getElementById('navigatorDynamicArea');
      if (!dynamicArea) return;
      dynamicArea.innerHTML = '';

      const field = academicFields[activeFieldId];
      if (!field) return;

      // Determine semester count
      let semesterCount = 8;
      let contextTitle = field.name;
      let contextDesc = '';

      if (field.structureType === 'direct-semesters') {
        semesterCount = field.semesters || 8;
        contextTitle = field.name;
      } else {
        const opt = field.options.find(o => o.id === activeOptionId) || field.options[0];
        if (opt) {
          semesterCount = opt.semesters;
          contextTitle = opt.name;
          contextDesc = opt.description;
        }
      }

      // If activeSemesterNumber exceeds count, reset to 1
      if (activeSemesterNumber > semesterCount) activeSemesterNumber = 1;

      // Semester Section
      const semSec = document.createElement('div');
      semSec.className = 'navigator-semester-section';

      if (contextDesc) {
        const descP = document.createElement('p');
        descP.style.cssText = 'color: var(--color-text-secondary); font-size: 12px; margin: 8px 0 14px;';
        descP.textContent = contextDesc;
        semSec.appendChild(descP);
      }

      const semLabel = document.createElement('div');
      semLabel.className = 'navigator-step-label';
      semLabel.textContent = `SELECT SEMESTER (1 TO ${semesterCount})`;
      semSec.appendChild(semLabel);

      const semGrid = document.createElement('div');
      semGrid.className = 'navigator-semesters-grid';

      for (let s = 1; s <= semesterCount; s++) {
        const btn = document.createElement('button');
        btn.type = 'button';
        btn.className = 'navigator-semester-btn' + (s === activeSemesterNumber ? ' active' : '');
        btn.textContent = `Semester ${s}`;
        btn.addEventListener('click', () => {
          activeSemesterNumber = s;
          $$('.navigator-semester-btn', semGrid).forEach(b => b.classList.remove('active'));
          btn.classList.add('active');
          renderCourseList();
        });
        semGrid.appendChild(btn);
      }

      semSec.appendChild(semGrid);
      dynamicArea.appendChild(semSec);

      // Courses Container
      const coursesSec = document.createElement('div');
      coursesSec.id = 'navigatorCoursesSection';
      coursesSec.className = 'navigator-courses-section';
      dynamicArea.appendChild(coursesSec);

      renderCourseList();
    }

    // Render course cards and PDFs
    function renderCourseList() {
      const coursesSec = document.getElementById('navigatorCoursesSection');
      if (!coursesSec) return;
      coursesSec.innerHTML = '';

      const field = academicFields[activeFieldId];
      let subTitle = field.name;
      if (field.structureType !== 'direct-semesters') {
        const opt = field.options.find(o => o.id === activeOptionId);
        if (opt) subTitle = opt.name;
      }

      const matches = getMatchingResources(activeFieldId, activeOptionId, activeSemesterNumber);

      // Header
      const head = document.createElement('div');
      head.className = 'navigator-courses-header';
      head.innerHTML = `
        <div>
          <div class="section-kicker">SEMESTER STUDY MATERIAL</div>
          <h3>${subTitle} · Semester ${activeSemesterNumber}</h3>
        </div>
        <span class="navigator-resource-count">${matches.length} ${matches.length === 1 ? 'Course Resource' : 'Course Resources'}</span>
      `;
      coursesSec.appendChild(head);

      if (!matches.length) {
        const empty = document.createElement('div');
        empty.className = 'navigator-empty-state';
        empty.innerHTML = `
          <strong>No indexed PDFs are currently mapped to this selection.</strong>
          <p style="margin: 6px 0 0; font-size: 12px;">Verified course materials and reference PDFs will appear here once added to the repository.</p>
        `;
        coursesSec.appendChild(empty);
        return;
      }

      const grid = document.createElement('div');
      grid.className = 'navigator-courses-grid';
      const viewerBase = getViewerPath();

      matches.forEach(r => {
        const actualUrl = 'https://media.githubusercontent.com/media/divyanshur78/Acadex/main/' +
          r.path.split('/').map(encodeURIComponent).join('/');
        const viewerUrl = `${viewerBase}?file=${encodeURIComponent(actualUrl)}`;
        const courseName = formatCourseTitle(r);

        const card = document.createElement('article');
        card.className = 'navigator-resource-card';
        card.innerHTML = `
          <div class="navigator-pdf-icon" aria-hidden="true">PDF</div>
          <div class="navigator-card-info">
            <strong title="${r.fileName}">${courseName}</strong>
            <small>${r.programme}${r.branch ? ' · ' + r.branch : ''}${r.specialisation ? ' · ' + r.specialisation : ''} · Semester ${r.semester}</small>
          </div>
          <div class="navigator-card-actions">
            <a href="${viewerUrl}" class="navigator-action-btn view-btn" target="_blank" rel="noopener noreferrer" title="View PDF">View</a>
            <a href="${actualUrl}" class="navigator-action-btn download-btn" download="${r.fileName}" target="_blank" rel="noopener noreferrer" title="Download PDF">Download</a>
          </div>
        `;
        grid.appendChild(card);
      });

      coursesSec.appendChild(grid);
    }

    // Connect field cards on page to open navigator
    $$('[data-field]').forEach(card => {
      card.addEventListener('click', (e) => {
        e.preventDefault();
        const fid = card.dataset.field;
        openField(fid);
      });
    });

    // Handle URL parameters or hash on load
    const params = new URLSearchParams(window.location.search);
    const fieldParam = params.get('field');
    const hash = window.location.hash.replace('#', '');

    if (fieldParam && academicFields[fieldParam]) {
      openField(fieldParam);
    } else if (academicFields[hash]) {
      openField(hash);
    }

    // Expose openField globally
    window.AcadexNavigator = {
      openField,
      academicFields
    };
  }

  // Initialize on DOM load
  document.addEventListener('DOMContentLoaded', () => {
    initAcademicNavigator('academicNavigatorPanel');
  });

})();

