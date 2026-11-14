/**
 * ACADEX - PHYSICAL BOOK LOCATOR SCRIPT
 * Preserves the campus physical book search, shelf location discovery, and availability records.
 */

(() => {
  'use strict';

  // Library verified catalog
  const libraryCatalog = [
    {
      id: 'book-001',
      title: 'Calculus Volume 1',
      author: 'Edwin Herman & Gilbert Strang',
      field: 'Engineering & Technology',
      program: 'B.Tech',
      building: 'Central Library Block 34',
      floor: '2nd Floor',
      section: 'Mathematics (Section M)',
      shelf: 'Rack 04 / Shelf B',
      callNumber: 'QA303.2 .H47 2024',
      availability: '4 copies available (2 on loan)',
      status: 'available'
    },
    {
      id: 'book-002',
      title: 'Fluid Mechanics & Hydraulic Machines',
      author: 'Dr. R.K. Bansal',
      field: 'Engineering & Technology',
      program: 'B.Tech Civil / Mechanical',
      building: 'Central Library Block 34',
      floor: '3rd Floor',
      section: 'Fluid Engineering (Section ME)',
      shelf: 'Rack 12 / Shelf C',
      callNumber: 'TA357 .B36 2023',
      availability: '6 copies available',
      status: 'available'
    },
    {
      id: 'book-003',
      title: 'Fundamentals of Agronomy',
      author: 'ICAR Committee on Agricultural Education',
      field: 'Agriculture',
      program: 'B.Sc. Agriculture',
      building: 'Agriculture Block 38 Library',
      floor: '1st Floor',
      section: 'Crop Sciences (Section AG)',
      shelf: 'Rack 02 / Shelf A',
      callNumber: 'S494.5 .A47 2023',
      availability: '5 copies available',
      status: 'available'
    },
    {
      id: 'book-004',
      title: 'Principles of Soil Science',
      author: 'M.M. Rai',
      field: 'Agriculture',
      program: 'B.Sc. Agriculture',
      building: 'Agriculture Block 38 Library',
      floor: '1st Floor',
      section: 'Soil Sciences (Section SS)',
      shelf: 'Rack 02 / Shelf C',
      callNumber: 'S591 .S65 2022',
      availability: '3 copies available',
      status: 'available'
    },
    {
      id: 'book-005',
      title: 'Constitutional Law of India',
      author: 'Dr. J.N. Pandey',
      field: 'Law',
      program: 'BA LL.B. / BBA LL.B.',
      building: 'Law Faculty Library Block 32',
      floor: '4th Floor',
      section: 'Constitutional Jurisprudence',
      shelf: 'Rack 08 / Shelf B',
      callNumber: 'KNS1744.5 .P36 2024',
      availability: '7 copies available',
      status: 'available'
    },
    {
      id: 'book-006',
      title: 'Indian Penal Code & Criminal Procedure',
      author: 'Ratanlal & Dhirajlal',
      field: 'Law',
      program: 'BA LL.B.',
      building: 'Law Faculty Library Block 32',
      floor: '4th Floor',
      section: 'Criminal Law (Section CL)',
      shelf: 'Rack 09 / Shelf A',
      callNumber: 'KNS3800 .R38 2023',
      availability: '2 copies available (low stock)',
      status: 'low'
    },
    {
      id: 'book-007',
      title: 'Textbook of Pharmaceutics-I',
      author: 'R.M. Mehta',
      field: 'Pharmaceutical Sciences',
      program: 'B.Pharm',
      building: 'Pharmacy Library Block 36',
      floor: '2nd Floor',
      section: 'Pharmaceutical Formulations',
      shelf: 'Rack 05 / Shelf B',
      callNumber: 'RS201 .M44 2023',
      availability: '5 copies available',
      status: 'available'
    },
    {
      id: 'book-008',
      title: 'Pharmacognosy & Phytochemistry',
      author: 'C.K. Kokate, A.P. Purohit',
      field: 'Pharmaceutical Sciences',
      program: 'B.Pharm',
      building: 'Pharmacy Library Block 36',
      floor: '2nd Floor',
      section: 'Natural Products (Section NP)',
      shelf: 'Rack 06 / Shelf D',
      callNumber: 'RS160 .K65 2024',
      availability: '4 copies available',
      status: 'available'
    },
    {
      id: 'book-009',
      title: 'Principles and Practice of Management',
      author: 'L.M. Prasad',
      field: 'Management & Commerce',
      program: 'BBA / MBA',
      building: 'Management Studies Block 35',
      floor: '2nd Floor',
      section: 'General Management (Section MG)',
      shelf: 'Rack 14 / Shelf A',
      callNumber: 'HD31 .P73 2023',
      availability: '8 copies available',
      status: 'available'
    },
    {
      id: 'book-010',
      title: 'Marketing Management: A Strategic Approach',
      author: 'Philip Kotler & Kevin Lane Keller',
      field: 'Management & Commerce',
      program: 'MBA',
      building: 'Management Studies Block 35',
      floor: '3rd Floor',
      section: 'Marketing & Sales (Section MKT)',
      shelf: 'Rack 16 / Shelf C',
      callNumber: 'HF5415 .K68 2024',
      availability: '6 copies available',
      status: 'available'
    },
    {
      id: 'book-011',
      title: 'Artificial Intelligence: A Modern Approach',
      author: 'Stuart Russell & Peter Norvig',
      field: 'Computer Science & IT',
      program: 'B.Tech CSE (AI-ML)',
      building: 'Central Library Block 34',
      floor: '4th Floor',
      section: 'Computer Science (Section CS)',
      shelf: 'Rack 22 / Shelf B',
      callNumber: 'Q335 .R87 2023',
      availability: '5 copies available',
      status: 'available'
    },
    {
      id: 'book-012',
      title: 'Computer Networking: A Top-Down Approach',
      author: 'James F. Kurose & Keith W. Ross',
      field: 'Computer Science & IT',
      program: 'B.Tech CSE (Cybersecurity / Networks)',
      building: 'Central Library Block 34',
      floor: '4th Floor',
      section: 'Networks & Security (Section NS)',
      shelf: 'Rack 24 / Shelf A',
      callNumber: 'TK5105 .K87 2024',
      availability: '4 copies available',
      status: 'available'
    }
  ];

  document.addEventListener('DOMContentLoaded', () => {
    const searchForm = document.querySelector('.library-search');
    const searchInput = searchForm ? searchForm.querySelector('input') : null;
    const locationPanel = document.querySelector('.location-panel');
    const resultsContainer = document.getElementById('bookLocatorResults');

    if (!locationPanel) return;

    // References to location items
    const items = locationPanel.querySelectorAll('.location-item strong');
    const buildingEl = items[0];
    const floorEl = items[1];
    const sectionEl = items[2];
    const shelfEl = items[3];
    const callNumberEl = items[4];
    const availabilityEl = items[5];

    let selectedBook = libraryCatalog[0];

    function updateLocationDisplay(book) {
      if (!book) return;
      selectedBook = book;

      if (buildingEl) buildingEl.textContent = book.building;
      if (floorEl) floorEl.textContent = book.floor;
      if (sectionEl) sectionEl.textContent = book.section;
      if (shelfEl) shelfEl.textContent = book.shelf;
      if (callNumberEl) callNumberEl.textContent = book.callNumber;
      if (availabilityEl) {
        availabilityEl.textContent = book.availability;
        availabilityEl.style.color = book.status === 'low' ? '#d97706' : '#059669';
      }

      // Highlight selected card
      if (resultsContainer) {
        resultsContainer.querySelectorAll('.book-item-card').forEach(card => {
          card.classList.toggle('selected', card.dataset.id === book.id);
        });
      }
    }

    function renderResults(filtered) {
      if (!resultsContainer) return;
      resultsContainer.innerHTML = '';

      if (!filtered.length) {
        resultsContainer.innerHTML = `
          <div style="padding: 24px; border: 1px dashed #dce2ef; border-radius: 12px; text-align: center; color: var(--color-text-secondary); font-size: 13px;">
            No printed books matching your query found in the library catalogue.
          </div>
        `;
        return;
      }

      filtered.forEach(book => {
        const card = document.createElement('div');
        card.className = 'book-item-card' + (book.id === selectedBook.id ? ' selected' : '');
        card.dataset.id = book.id;
        card.innerHTML = `
          <div class="book-item-info">
            <h4>${book.title}</h4>
            <p>${book.author} · <span style="color: var(--color-primary);">${book.field}</span> (${book.program})</p>
          </div>
          <span class="book-item-badge ${book.status}">${book.availability.split('(')[0].trim()}</span>
        `;
        card.addEventListener('click', () => {
          updateLocationDisplay(book);
          locationPanel.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
        });
        resultsContainer.appendChild(card);
      });
    }

    function handleSearch() {
      const query = (searchInput ? searchInput.value : '').trim().toLowerCase();
      if (!query) {
        renderResults(libraryCatalog);
        return;
      }

      const filtered = libraryCatalog.filter(b => {
        return b.title.toLowerCase().includes(query) ||
               b.author.toLowerCase().includes(query) ||
               b.field.toLowerCase().includes(query) ||
               b.program.toLowerCase().includes(query) ||
               b.callNumber.toLowerCase().includes(query);
      });

      renderResults(filtered);
      if (filtered.length) {
        updateLocationDisplay(filtered[0]);
      }
    }

    if (searchForm) {
      searchForm.addEventListener('submit', (e) => {
        e.preventDefault();
        handleSearch();
      });
    }

    if (searchInput) {
      searchInput.addEventListener('input', handleSearch);
    }

    // Initial render
    renderResults(libraryCatalog);
    updateLocationDisplay(libraryCatalog[0]);
  });
})();

