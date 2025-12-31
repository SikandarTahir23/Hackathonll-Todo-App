"""
Integration test for the delete command flow.
"""
import unittest
from src.models.task import TaskList
from src.services.todo_service import TodoService
from src.cli.command_handler import CommandHandler


class TestDeleteTaskIntegration(unittest.TestCase):
    """Integration test for the delete command flow."""
    
    def setUp(self):
        """Set up the command handler with dependencies for each test."""
        self.task_list = TaskList()
        self.todo_service = TodoService(self.task_list)
        self.command_handler = CommandHandler(self.todo_service)
    
    def test_delete_command_success(self):
        """Test that the delete command successfully deletes a task."""
        # Add a task first
        self.command_handler.handle_command("add Buy groceries")
        
        result = self.command_handler.handle_command("delete 1")
        
        # Verify the command response
        self.assertEqual(result, "Task 1 deleted")
        
        # Verify the task was actually deleted
        tasks = self.todo_service.get_all_tasks()
        self.assertEqual(len(tasks), 0)
    
    def test_delete_command_with_invalid_task_id_fails(self):
        """Test that the delete command fails with invalid task ID."""
        result = self.command_handler.handle_command("delete 99")
        
        # Verify the error response
        self.assertEqual(result, "Error: Task with ID 99 does not exist")
    
    def test_delete_command_with_invalid_id_format_fails(self):
        """Test that the delete command fails with invalid ID format."""
        result = self.command_handler.handle_command("delete abc")
        
        # Verify the error response
        self.assertEqual(result, "Error: Task ID must be a number")
    
    def test_delete_command_with_no_id_fails(self):
        """Test that the delete command fails with no ID provided."""
        result = self.command_handler.handle_command("delete")
        
        # Verify the error response
        self.assertEqual(result, "Error: Command requires additional arguments. Use 'help' for syntax.")
    
    def test_delete_command_with_multiple_tasks(self):
        """Test that the delete command works correctly with multiple tasks."""
        # Add multiple tasks first
        self.command_handler.handle_command("add Buy groceries")
        self.command_handler.handle_command("add Finish report")
        self.command_handler.handle_command("add Call mom")
        
        # Delete the second task
        result = self.command_handler.handle_command("delete 2")
        
        # Verify the command response
        self.assertEqual(result, "Task 2 deleted")
        
        # Verify the tasks list is correct after deletion
        tasks = self.todo_service.get_all_tasks()
        self.assertEqual(len(tasks), 2)
        
        # Verify the correct task was deleted and others remain
        remaining_task_ids = [task.id for task in tasks]
        self.assertIn(1, remaining_task_ids)
        self.assertNotIn(2, remaining_task_ids)  # Task 2 should be deleted
        self.assertIn(3, remaining_task_ids)
    
    def test_delete_command_works_after_view(self):
        """Test that delete command works correctly after viewing tasks."""
        # Add tasks and view them first
        self.command_handler.handle_command("add Buy groceries")
        self.command_handler.handle_command("add Finish report")
        
        view_result = self.command_handler.handle_command("list")
        self.assertIn("Buy groceries", view_result)
        self.assertIn("Finish report", view_result)
        
        # Now delete one task
        result = self.command_handler.handle_command("delete 1")
        self.assertEqual(result, "Task 1 deleted")
        
        # Verify the task is no longer in the list when viewed again
        view_result = self.command_handler.handle_command("list")
        self.assertNotIn("Buy groceries", view_result)
        self.assertIn("Finish report", view_result)
    
    def test_delete_all_tasks(self):
        """Test deleting all tasks works correctly."""
        # Add multiple tasks
        self.command_handler.handle_command("add Task 1")
        self.command_handler.handle_command("add Task 2")
        
        # Delete both tasks
        self.command_handler.handle_command("delete 1")
        self.command_handler.handle_command("delete 2")
        
        # Verify the list is now empty
        result = self.command_handler.handle_command("list")
        self.assertEqual(result, "No tasks in your todo list")


if __name__ == '__main__':
    unittest.main()