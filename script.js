/**
 * script.js
 * Student Task Management System
 * Features:
 *   - Add new task with title + description validation
 *   - Toggle task status between Pending and Completed (JavaScript-based)
 */

'use strict';

/* ── DOM References ─────────────────────────────────────── */
const form       = document.getElementById('task-form');
const titleInput = document.getElementById('task-title');
const descInput  = document.getElementById('task-desc');
const taskList   = document.getElementById('task-list');
const taskCount  = document.getElementById('task-count');
const formError  = document.getElementById('form-error');

/* ── Task ID Counter ────────────────────────────────────── */
let nextId = 4; // IDs 1-3 used by pre-existing HTML tasks

/* ═══════════════════════════════════════════════════════════
   HELPERS
   ═══════════════════════════════════════════════════════════ */

/** Updates the task-count badge to reflect current total */
function refreshCount() {
  taskCount.textContent = taskList.querySelectorAll('.task-item').length;
}

/** Shows a form validation error */
function showError(msg) {
  formError.textContent = msg;
}

/** Clears the form validation error */
function clearError() {
  formError.textContent = '';
}

/**
 * Escapes HTML special characters to prevent XSS.
 * @param {string} str
 * @returns {string}
 */
function escapeHtml(str) {
  const map = { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' };
  return str.replace(/[&<>"']/g, ch => map[ch]);
}

/* ═══════════════════════════════════════════════════════════
   STATUS TOGGLE
   JavaScript changes Pending ↔ Completed on button click
   ═══════════════════════════════════════════════════════════ */

/**
 * Toggles a task between Pending and Completed.
 * @param {HTMLElement} btn - The clicked toggle button
 */
function toggleStatus(btn) {
  const taskItem   = btn.closest('.task-item');
  const statusBadge = taskItem.querySelector('.task-status');
  const isPending  = statusBadge.classList.contains('status-pending');

  if (isPending) {
    // Pending → Completed
    statusBadge.textContent = 'Completed';
    statusBadge.classList.remove('status-pending');
    statusBadge.classList.add('status-completed');

    btn.textContent = 'Mark Pending';
    btn.classList.remove('btn-mark-done');
    btn.classList.add('btn-mark-pending');

    taskItem.classList.add('task-completed');
  } else {
    // Completed → Pending
    statusBadge.textContent = 'Pending';
    statusBadge.classList.remove('status-completed');
    statusBadge.classList.add('status-pending');

    btn.textContent = 'Mark Completed';
    btn.classList.remove('btn-mark-pending');
    btn.classList.add('btn-mark-done');

    taskItem.classList.remove('task-completed');
  }
}

/* Event delegation — handles both pre-loaded and newly added tasks */
taskList.addEventListener('click', function (event) {
  const btn = event.target.closest('.toggle-status-btn');
  if (btn) toggleStatus(btn);
});

/* ═══════════════════════════════════════════════════════════
   BUILD A TASK ELEMENT
   ═══════════════════════════════════════════════════════════ */

/**
 * Creates and returns a <li> task card element.
 * @param {number} id
 * @param {string} title
 * @param {string} description
 * @returns {HTMLLIElement}
 */
function createTaskElement(id, title, description) {
  const li = document.createElement('li');
  li.className = 'task-item';
  li.dataset.id = id;

  const today = new Date().toLocaleDateString('en-GB', {
    day: 'numeric', month: 'short', year: 'numeric'
  });

  li.innerHTML = `
    <div class="task-body">
      <div class="task-header">
        <h3 class="task-title">${escapeHtml(title)}</h3>
      </div>
      <p class="task-desc">${escapeHtml(description)}</p>
      <div class="task-status-row">
        <span class="status-label">Status:</span>
        <span class="task-status status-pending">Pending</span>
      </div>
      <div class="task-meta-row">
        <span class="meta-item"><strong>Added:</strong> ${today}</span>
        <button class="btn btn-mark-done toggle-status-btn" data-task-id="${id}">
          Mark Completed
        </button>
      </div>
    </div>
  `;

  return li;
}

/* ═══════════════════════════════════════════════════════════
   ADD TASK — FORM SUBMISSION
   ═══════════════════════════════════════════════════════════ */

form.addEventListener('submit', function (event) {
  event.preventDefault();
  clearError();

  const title = titleInput.value.trim();
  const desc  = descInput.value.trim();

  /* Blank-submission validation */
  if (title === '' && desc === '') {
    showError('Please enter both a task title and a description.');
    titleInput.focus();
    return;
  }
  if (title === '') {
    showError('Task title cannot be blank.');
    titleInput.focus();
    return;
  }
  if (desc === '') {
    showError('Description cannot be blank.');
    descInput.focus();
    return;
  }

  /* Append the new task, update counter, reset form */
  const newTask = createTaskElement(nextId++, title, desc);
  taskList.appendChild(newTask);

  refreshCount();
  form.reset();
  titleInput.focus();
});

/* ── Initialise count on page load ─────────────────────── */
refreshCount();
