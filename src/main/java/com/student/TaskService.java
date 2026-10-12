package com.student;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

/**
 * Service class for managing student tasks.
 */
public class TaskService {

    public static class Task {
        private final int id;
        private final String title;
        private final String description;
        private final String priority;
        private boolean completed;

        public Task(int id, String title, String description, String priority) {
            if (title == null || title.trim().isEmpty()) {
                throw new IllegalArgumentException("Task title cannot be blank");
            }
            if (description == null || description.trim().isEmpty()) {
                throw new IllegalArgumentException("Task description cannot be blank");
            }
            this.id = id;
            this.title = title.trim();
            this.description = description.trim();
            this.priority = (priority != null && !priority.trim().isEmpty()) ? priority.trim().toLowerCase() : "medium";
            this.completed = false;
        }

        public int getId() { return id; }
        public String getTitle() { return title; }
        public String getDescription() { return description; }
        public String getPriority() { return priority; }
        public boolean isCompleted() { return completed; }
        public void setCompleted(boolean completed) { this.completed = completed; }
    }

    private final List<Task> tasks = new ArrayList<>();
    private int nextId = 1;

    public TaskService() {
        // Pre-populate default sample tasks matching the UI
        addTask("Complete Git Assignment — Parts 1 & 2", "Set up local Git repo, commits, branches, and push to GitHub.", "high");
        addTask("Read DevOps Textbook — Chapter 3", "Study CI/CD pipelines and concepts.", "medium");
        addTask("Submit Database Normalisation Lab", "Finalise SQL queries and submit PDF report.", "low");
    }

    public Task addTask(String title, String description, String priority) {
        Task task = new Task(nextId++, title, description, priority);
        tasks.add(task);
        return task;
    }

    public List<Task> getAllTasks() {
        return Collections.unmodifiableList(tasks);
    }

    public int getTaskCount() {
        return tasks.size();
    }

    public boolean toggleTaskStatus(int id) {
        for (Task task : tasks) {
            if (task.getId() == id) {
                task.setCompleted(!task.isCompleted());
                return true;
            }
        }
        return false;
    }
}
