"""
Integration test for the add command flow.
"""
import unittest
from src.models.task import TaskList
from src.services.todo_service import TodoService
from src.cli.command_handler import CommandHandler


class TestAddTaskIntegration(unittest.TestCase):
    """Integration test for the add command flow."""
    
    def setUp(self):
        """Set up the command handler with dependencies for each test."""
        self.task_list = TaskList()
        self.todo_service = TodoService(self.task_list)
        self.command_handler = CommandHandler(self.todo_service)
    
    def test_add_task_command_success(self):
        """Test that the add command successfully adds a task."""
        result = self.command_handler.handle_command("add Buy groceries")
        
        # Verify the command response
        self.assertIn("Task 1 added: Buy groceries", result)
        
        # Verify the task was actually added to the list
        tasks = self.todo_service.get_all_tasks()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0].id, 1)
        self.assertEqual(tasks[0].description, "Buy groceries")
        self.assertFalse(tasks[0].completed)
    
    def test_add_task_command_with_empty_description_fails(self):
        """Test that the add command fails with empty description."""
        result = self.command_handler.handle_command("add")
        
        # Verify the error response
        self.assertEqual(result, "Error: Task description cannot be empty")
        
        # Verify no tasks were added
        tasks = self.todo_service.get_all_tasks()
        self.assertEqual(len(tasks), 0)
    
    def test_add_task_command_with_whitespace_only_description_fails(self):
        """Test that the add command fails with whitespace-only description."""
        result = self.command_handler.handle_command("add    ")
        
        # Verify the error response
        self.assertEqual(result, "Error: Task description cannot be empty")
        
        # Verify no tasks were added
        tasks = self.todo_service.get_all_tasks()
        self.assertEqual(len(tasks), 0)
    
    def test_multiple_add_tasks_command_success(self):
        """Test that multiple add commands work correctly."""
        result1 = self.command_handler.handle_command("add Buy groceries")
        result2 = self.command_handler.handle_command("add Finish report")
        
        # Verify the command responses
        self.assertIn("Task 1 added: Buy groceries", result1)
        self.assertIn("Task 2 added: Finish report", result2)
        
        # Verify both tasks were added to the list
        tasks = self.todo_service.get_all_tasks()
        self.assertEqual(len(tasks), 2)
        self.assertEqual(tasks[0].id, 1)
        self.assertEqual(tasks[0].description, "Buy groceries")
        self.assertEqual(tasks[1].id, 2)
        self.assertEqual(tasks[1].description, "Finish report")


if __name__ == '__main__':
    unittest.main()