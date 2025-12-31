"""
Integration test for the mark complete command flow.
"""
import unittest
from src.models.task import TaskList
from src.services.todo_service import TodoService
from src.cli.command_handler import CommandHandler


class TestMarkCompleteIntegration(unittest.TestCase):
    """Integration test for the mark complete command flow."""
    
    def setUp(self):
        """Set up the command handler with dependencies for each test."""
        self.task_list = TaskList()
        self.todo_service = TodoService(self.task_list)
        self.command_handler = CommandHandler(self.todo_service)
    
    def test_complete_command_success(self):
        """Test that the complete command successfully marks a task as complete."""
        # Add a task first
        self.command_handler.handle_command("add Buy groceries")
        
        result = self.command_handler.handle_command("complete 1")
        
        # Verify the command response
        self.assertEqual(result, "Task 1 marked complete")
        
        # Verify the task was actually marked as complete
        task = self.todo_service.get_task_by_id(1)
        self.assertIsNotNone(task)
        self.assertTrue(task.completed)
    
    def test_complete_command_with_invalid_task_id_fails(self):
        """Test that the complete command fails with invalid task ID."""
        result = self.command_handler.handle_command("complete 99")
        
        # Verify the error response
        self.assertEqual(result, "Error: Task with ID 99 does not exist")
        
        # Verify no tasks were affected
        tasks = self.todo_service.get_all_tasks()
        self.assertEqual(len(tasks), 0)
    
    def test_complete_command_with_invalid_id_format_fails(self):
        """Test that the complete command fails with invalid ID format."""
        result = self.command_handler.handle_command("complete abc")
        
        # Verify the error response
        self.assertEqual(result, "Error: Task ID must be a number")
    
    def test_complete_command_with_no_id_fails(self):
        """Test that the complete command fails with no ID provided."""
        result = self.command_handler.handle_command("complete")
        
        # Verify the error response
        self.assertEqual(result, "Error: Command requires additional arguments. Use 'help' for syntax.")
    
    def test_complete_command_with_multiple_tasks(self):
        """Test that the complete command works correctly with multiple tasks."""
        # Add multiple tasks first
        self.command_handler.handle_command("add Buy groceries")
        self.command_handler.handle_command("add Finish report")
        self.command_handler.handle_command("add Call mom")
        
        # Complete the second task
        result = self.command_handler.handle_command("complete 2")
        
        # Verify the command response
        self.assertEqual(result, "Task 2 marked complete")
        
        # Verify the tasks have correct completion status
        task1 = self.todo_service.get_task_by_id(1)
        task2 = self.todo_service.get_task_by_id(2)
        task3 = self.todo_service.get_task_by_id(3)
        
        self.assertFalse(task1.completed)
        self.assertTrue(task2.completed)
        self.assertFalse(task3.completed)
    
    def test_complete_command_works_after_view(self):
        """Test that complete command works correctly after viewing tasks."""
        # Add tasks and view them first
        self.command_handler.handle_command("add Buy groceries")
        self.command_handler.handle_command("add Finish report")
        
        view_result = self.command_handler.handle_command("list")
        self.assertIn("Buy groceries", view_result)
        self.assertIn("Finish report", view_result)
        
        # Now complete one task
        result = self.command_handler.handle_command("complete 1")
        self.assertEqual(result, "Task 1 marked complete")
        
        # Verify the task is now marked complete when viewed again
        view_result = self.command_handler.handle_command("list")
        self.assertIn("Buy groceries - Complete", view_result)
        self.assertIn("Finish report - Incomplete", view_result)


if __name__ == '__main__':
    unittest.main()