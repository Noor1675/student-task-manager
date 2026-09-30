/**
 * script.js
 * Student Task Management System
 * Handles: add-task form submission, input validation, task rendering
 */

'use strict';

/* ── DOM References ─────────────────────────────────────── */
const form      = document.getElementById('task-form');
const titleInput = document.getElementById('task-title');
const descInput  = document.getElementById('task-desc');
const taskList   = document.getElementById('task-list');
const taskCount  = document.getElementById('task-count');
const formError  = document.getElementById('form-error');

/* ── Task ID Counter ────────────────────────────────────── */
let nextId = 4; // IDs 1-3 used by pre-existing HTML tasks

/* ── Helpers ────────────────────────────────────────────── */

/** Returns the number of rendered task items */
function getTaskCount() {
  return taskList.querySelectorAll('.task-item').length;
}

/** Updates the badge that shows the live task count */
function refreshCount() {
  taskCount.textContent = getTaskCount();
}

/** Shows a validation error message */
function showError(msg) {
  formError.textContent = msg;
}

/** Clears the validation error message */
function clearError() {
  formError.textContent = '';
}

/* ── Build a Task List Item ─────────────────────────────── */

/**
 * Creates and returns a <li> element for a task.
 * @param {number} id          - Unique task identifier
 * @param {string} title       - Task title
 * @param {string} description - Task description
 * @returns {HTMLLIElement}
 */
function createTaskElement(id, title, description) {
  const li = document.createElement('li');
  li.className = 'task-item';
  li.dataset.id = id;

  // Uses the same card structure as the pre-loaded tasks (Option B layout)
  li.innerHTML = `
    <div class="task-body">
      <div class="task-header">
        <h3 class="task-title">${escapeHtml(title)}</h3>
        <span class="task-status status-pending">Pending</span>
      </div>
      <p class="task-desc">${escapeHtml(description)}</p>
      <div class="task-meta-row">
        <span class="meta-item"><strong>Added:</strong> ${new Date().toLocaleDateString('en-GB', { day: 'numeric', month: 'short', year: 'numeric' })}</span>
      </div>
    </div>
  `;

  return li;
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

/* ── Form Submission Handler ────────────────────────────── */

form.addEventListener('submit', function (event) {
  event.preventDefault();
  clearError();

  const title = titleInput.value.trim();
  const desc  = descInput.value.trim();

  // Validation: blank submissions are not accepted
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

  // Create and append the new task
  const newTask = createTaskElement(nextId++, title, desc);
  taskList.appendChild(newTask);

  // Update counter and reset form
  refreshCount();
  form.reset();
  titleInput.focus();
});

/* ── Initialise Count on Page Load ─────────────────────── */
refreshCount();
