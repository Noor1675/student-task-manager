package com.student;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class TaskServiceTest {

    private TaskService taskService;

    @BeforeEach
    void setUp() {
        taskService = new TaskService();
    }

    @Test
    @DisplayName("Initial tasks count should be 3")
    void testInitialTasksCount() {
        assertEquals(3, taskService.getTaskCount());
    }

    @Test
    @DisplayName("Adding a valid task increases task count")
    void testAddNewTask() {
        TaskService.Task newTask = taskService.addTask("DevOps Tomcat Lab", "Deploy WAR on Tomcat 10", "high");
        assertNotNull(newTask);
        assertEquals(4, taskService.getTaskCount());
        assertEquals("DevOps Tomcat Lab", newTask.getTitle());
        assertEquals("high", newTask.getPriority());
        assertFalse(newTask.isCompleted());
    }

    @Test
    @DisplayName("Adding task with blank title throws exception")
    void testBlankTitleThrowsException() {
        assertThrows(IllegalArgumentException.class, () -> {
            taskService.addTask("   ", "Description", "low");
        });
    }

    @Test
    @DisplayName("Toggle task status toggles completed flag")
    void testToggleTaskStatus() {
        boolean toggled = taskService.toggleTaskStatus(1);
        assertTrue(toggled);
        assertTrue(taskService.getAllTasks().get(0).isCompleted());
    }
}
