/**
 * ACADEX - CENTRAL APPLICATION & PROFILE SCRIPT
 * Handles global navigation, mobile hamburger menu, and profile synchronization.
 */

(() => {
  'use strict';

  const STORAGE_KEY = 'acadexProfile';

  // Helper selectors
  const $ = (selector, root = document) => root.querySelector(selector);
  const $$ = (selector, root = document) => [...root.querySelectorAll(selector)];

  // Get current profile
  function getProfile() {
    try {
      const saved = localStorage.getItem(STORAGE_KEY) || localStorage.getItem('acadexDemoProfile');
      if (saved) return JSON.parse(saved);
    } catch (e) {
      console.warn('Error reading profile from localStorage:', e);
    }
    return {
      name: '',
      registration: '',
      program: '',
      field: '',
      semester: '',
      school: '',
      year: ''
    };
  }

  // Save profile
  function saveProfile(data) {
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(data));
      // Also update demo profile key for compatibility
      localStorage.setItem('acadexDemoProfile', JSON.stringify(data));
      syncProfileUI(data);
      return true;
    } catch (e) {
      console.error('Error saving profile to localStorage:', e);
      return false;
    }
  }

  // Get user initials from name
  function getInitials(name) {
    if (!name || typeof name !== 'string') return 'ST';
    const parts = name.trim().split(/\s+/).filter(Boolean);
    if (!parts.length) return 'ST';
    if (parts.length === 1) return parts[0].slice(0, 2).toUpperCase();
    return (parts[0][0] + parts[parts.length - 1][0]).toUpperCase();
  }

  // Synchronize profile data across all visible elements
  function syncProfileUI(customProfile) {
    const p = customProfile || getProfile();
    const displayName = p.name ? p.name.trim() : 'Student';
    const initials = getInitials(displayName);

    // Top Navigation UI
    const navName = $('#topbarUserName');
    if (navName) navName.textContent = displayName;

    const navAvatar = $('#topbarUserAvatar');
    if (navAvatar) navAvatar.textContent = initials;

    // Legacy / Alternative attribute hooks
    $$('[data-user-name]').forEach(el => { el.textContent = displayName; });
    $$('[data-user-initials]').forEach(el => { el.textContent = initials; });
    $$('[data-user-program]').forEach(el => {
      el.textContent = p.program ? p.program : 'My academic profile';
    });

    // Academic Context Strip across pages (courses, digital library, book locator, exam prep, etc.)
    const progText = p.program ? p.program : 'Not added';
    const fieldText = p.field ? p.field : 'Not added';
    const semText = p.semester ? p.semester : 'Not added';
    const yearText = p.year ? p.year : 'Not added';

    $$('[data-academic-programme], [data-profile-program]').forEach(el => { el.textContent = progText; });
    $$('[data-academic-field], [data-profile-field]').forEach(el => { el.textContent = fieldText; });
    $$('[data-academic-semester], [data-profile-semester]').forEach(el => { el.textContent = semText; });
    $$('[data-academic-year], [data-profile-year]').forEach(el => { el.textContent = yearText; });

    // Profile page elements if present
    const profileAvatar = $('#profileAvatar');
    if (profileAvatar) profileAvatar.textContent = initials;

    const profileDisplayName = $('#profileDisplayName');
    if (profileDisplayName) profileDisplayName.textContent = p.name ? p.name : 'Student Name';

    const profileDisplayProgram = $('#profileDisplayProgram');
    if (profileDisplayProgram) {
      profileDisplayProgram.textContent = p.program ? p.program : 'Your academic profile';
    }

    // Populate form fields if form exists and hasn't been modified yet
    const form = $('#profileForm');
    if (form && p.name) {
      ['name', 'registration', 'program', 'field', 'semester', 'school', 'year'].forEach(field => {
        if (form.elements[field] && !form.elements[field].dataset.userEditing) {
          form.elements[field].value = p[field] || '';
        }
      });
    }
  }

  // Setup Mobile Menu Toggle
  function initMobileMenu() {
    const btn = $('#mobileMenuBtn');
    const nav = $('#topbarNav');
    if (!btn || !nav) return;

    btn.addEventListener('click', (e) => {
      e.stopPropagation();
      const isOpen = nav.classList.toggle('open');
      btn.setAttribute('aria-expanded', String(isOpen));
    });

    // Close when clicking any nav link
    $$('.nav-link', nav).forEach(link => {
      link.addEventListener('click', () => {
        nav.classList.remove('open');
        btn.setAttribute('aria-expanded', 'false');
      });
    });

    // Close when clicking outside
    document.addEventListener('click', (e) => {
      if (!nav.contains(e.target) && !btn.contains(e.target)) {
        nav.classList.remove('open');
        btn.setAttribute('aria-expanded', 'false');
      }
    });
  }

  // Initialize on load
  document.addEventListener('DOMContentLoaded', () => {
    initMobileMenu();
    syncProfileUI();
  });

  // Keep in sync across tabs or storage updates
  window.addEventListener('storage', (e) => {
    if (e.key === STORAGE_KEY || e.key === 'acadexDemoProfile') {
      syncProfileUI();
    }
  });

  // Expose to window for other scripts to use
  window.AcadexApp = {
    getProfile,
    saveProfile,
    syncProfileUI,
    getInitials
  };
})();
