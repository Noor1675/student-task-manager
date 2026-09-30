# Student Task Management System

## Project Overview

The **Student Task Management System** is a lightweight, browser-based web application built as the first milestone in a continuing DevOps project series. It allows students to view, add and manage their academic tasks directly in a modern web browser — no server or database required.

---

## Purpose

This project demonstrates the full local Git workflow:
- Creating and structuring a version-controlled project.
- Staging related files and writing meaningful commit messages.
- Developing new features on isolated branches and merging them into `main`.

The same repository will be extended in future assignments to include GitHub remote collaboration, Maven build management, Jenkins CI/CD pipelines, Terraform provisioning and application monitoring.

---

## Current Features (v0.1 — Initial Release)

| Feature | Description |
|---|---|
| Task display | Three pre-populated sample student tasks shown on page load |
| Add task | A form with **Title** and **Description** fields appends a new task to the list |
| Blank validation | Submissions with an empty title or description are rejected with an error message |
| Live task counter | A badge next to the "My Tasks" heading updates automatically |
| Responsive layout | Usable on desktop, tablet and mobile screens |

---

## File Structure

```
student-task-manager/
├── index.html    — Page structure, form and sample task list
├── style.css     — Dark-theme styles, layout and animations
├── script.js     — Add-task logic and input validation
├── README.md     — This documentation file
└── .gitignore    — Patterns for files excluded from version control
```

---

## Usage Instructions

1. **Clone or download** this repository to your local machine.
2. Open **`index.html`** in any modern web browser (Chrome, Firefox, Edge, Safari).
3. Use the **Add New Task** form to enter a task title and description, then click **+ Add Task**.
4. Blank fields will display a validation error — both fields must be filled before a task is accepted.

No build step, package manager or internet connection is required to run the application.

---

## Planned DevOps Work

| Assignment | Work Planned |
|---|---|
| Part 1 (current) | Local Git — branching, commits, merge |
| Part 2 | GitHub — remote push, pull request, release v1.0.0 |
| Part 3 | Maven — project structure and automated tests |
| Part 4 | Jenkins — CI/CD pipeline |
| Part 5 | Terraform — infrastructure provisioning |
| Part 6 | Monitoring — application health and alerting |

---

## Author

- **Project:** Student Task Management System  
- **Course:** DevOps Practical Series  
- **Year:** 2026
