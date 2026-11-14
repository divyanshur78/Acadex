/**
 * ACADEX - STUDENT PROFILE CONTROLLER
 * Handles profile form submission, local persistence, live summary updates,
 * and application-wide academic context syncing.
 */

(() => {
  'use strict';

  document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('profileForm');
    const statusMsg = document.getElementById('profileStatus');

    if (!form) return;

    // Load existing profile and populate form
    const current = window.AcadexApp ? window.AcadexApp.getProfile() : {};
    if (current && current.name) {
      ['name', 'registration', 'program', 'field', 'semester', 'school', 'year'].forEach(key => {
        if (form.elements[key]) {
          form.elements[key].value = current[key] || '';
        }
      });
    }

    // Mark fields when user is typing to avoid overriding during storage sync
    form.querySelectorAll('input, select').forEach(el => {
      el.addEventListener('input', () => {
        el.dataset.userEditing = 'true';
      });
    });

    // Handle form submission
    form.addEventListener('submit', (e) => {
      e.preventDefault();

      const formData = new FormData(form);
      const data = {
        name: (formData.get('name') || '').trim(),
        registration: (formData.get('registration') || '').trim(),
        program: (formData.get('program') || '').trim(),
        field: (formData.get('field') || '').trim(),
        semester: (formData.get('semester') || '').trim(),
        school: (formData.get('school') || '').trim(),
        year: (formData.get('year') || '').trim()
      };

      if (!data.name) {
        if (statusMsg) {
          statusMsg.style.color = '#ef4444';
          statusMsg.textContent = 'Please enter your student name.';
        }
        return;
      }

      if (window.AcadexApp) {
        window.AcadexApp.saveProfile(data);
      }

      // Remove editing flags
      form.querySelectorAll('input, select').forEach(el => {
        delete el.dataset.userEditing;
      });

      if (statusMsg) {
        statusMsg.style.color = '#10b981';
        statusMsg.textContent = 'Profile saved successfully.';
        setTimeout(() => {
          if (statusMsg.textContent === 'Profile saved successfully.') {
            statusMsg.textContent = '';
          }
        }, 4000);
      }
    });
  });
})();

