"""
Integration test for the update command flow.
"""
import unittest
from src.models.task import TaskList
from src.services.todo_service import TodoService
from src.cli.command_handler import CommandHandler


class TestUpdateTaskIntegration(unittest.TestCase):
    """Integration test for the update command flow."""
    
    def setUp(self):
        """Set up the command handler with dependencies for each test."""
        self.task_list = TaskList()
        self.todo_service = TodoService(self.task_list)
        self.command_handler = CommandHandler(self.todo_service)
    
    def test_update_command_success(self):
        """Test that the update command successfully updates a task description."""
        # Add a task first
        self.command_handler.handle_command("add Buy groceries")
        
        result = self.command_handler.handle_command("update 1 Buy milk and bread")
        
        # Verify the command response
        self.assertEqual(result, "Task 1 updated: Buy milk and bread")
        
        # Verify the task was actually updated
        task = self.todo_service.get_task_by_id(1)
        self.assertIsNotNone(task)
        self.assertEqual(task.description, "Buy milk and bread")
    
    def test_update_command_with_invalid_task_id_fails(self):
        """Test that the update command fails with invalid task ID."""
        result = self.command_handler.handle_command("update 99 New description")
        
        # Verify the error response
        self.assertEqual(result, "Error: Task with ID 99 does not exist")
    
    def test_update_command_with_invalid_id_format_fails(self):
        """Test that the update command fails with invalid ID format."""
        result = self.command_handler.handle_command("update abc New description")
        
        # Verify the error response
        self.assertEqual(result, "Error: Task ID must be a number")
    
    def test_update_command_with_empty_new_description_fails(self):
        """Test that the update command fails with empty new description."""
        # Add a task first
        self.command_handler.handle_command("add Buy groceries")
        
        result = self.command_handler.handle_command("update 1")
        
        # Verify the error response
        self.assertEqual(result, "Error: Command requires additional arguments. Use 'help' for syntax.")
    
    def test_update_command_with_empty_description_string_fails(self):
        """Test that the update command fails with empty description string."""
        # Add a task first
        self.command_handler.handle_command("add Buy groceries")
        
        result = self.command_handler.handle_command("update 1   ")
        
        # Verify the error response
        self.assertEqual(result, "Error: Task description cannot be empty")
    
    def test_update_command_with_no_arguments_fails(self):
        """Test that the update command fails with no arguments."""
        result = self.command_handler.handle_command("update")
        
        # Verify the error response
        self.assertEqual(result, "Error: Command requires additional arguments. Use 'help' for syntax.")
    
    def test_update_command_with_multiple_tasks(self):
        """Test that the update command works correctly with multiple tasks."""
        # Add multiple tasks first
        self.command_handler.handle_command("add Buy groceries")
        self.command_handler.handle_command("add Finish report")
        self.command_handler.handle_command("add Call mom")
        
        # Update the second task
        result = self.command_handler.handle_command("update 2 Submit final report")
        
        # Verify the command response
        self.assertEqual(result, "Task 2 updated: Submit final report")
        
        # Verify the tasks have correct descriptions
        task1 = self.todo_service.get_task_by_id(1)
        task2 = self.todo_service.get_task_by_id(2)
        task3 = self.todo_service.get_task_by_id(3)
        
        self.assertEqual(task1.description, "Buy groceries")
        self.assertEqual(task2.description, "Submit final report")
        self.assertEqual(task3.description, "Call mom")
    
    def test_update_command_works_after_view(self):
        """Test that update command works correctly after viewing tasks."""
        # Add tasks and view them first
        self.command_handler.handle_command("add Buy groceries")
        self.command_handler.handle_command("add Finish report")
        
        view_result = self.command_handler.handle_command("list")
        self.assertIn("Buy groceries", view_result)
        self.assertIn("Finish report", view_result)
        
        # Now update one task
        result = self.command_handler.handle_command("update 1 Buy milk and bread")
        self.assertEqual(result, "Task 1 updated: Buy milk and bread")
        
        # Verify the task is now updated when viewed again
        view_result = self.command_handler.handle_command("list")
        self.assertIn("Buy milk and bread", view_result)
        self.assertNotIn("Buy groceries", view_result)
        self.assertIn("Finish report", view_result)


if __name__ == '__main__':
    unittest.main()