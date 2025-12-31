"""
Integration test for the view/list command flow.
"""
import unittest
from src.models.task import TaskList
from src.services.todo_service import TodoService
from src.cli.command_handler import CommandHandler


class TestViewTasksIntegration(unittest.TestCase):
    """Integration test for the view/list command flow."""
    
    def setUp(self):
        """Set up the command handler with dependencies for each test."""
        self.task_list = TaskList()
        self.todo_service = TodoService(self.task_list)
        self.command_handler = CommandHandler(self.todo_service)
    
    def test_view_command_with_empty_list(self):
        """Test that the view command shows appropriate message for empty list."""
        result = self.command_handler.handle_command("view")
        
        # Verify the response for empty list
        self.assertEqual(result, "No tasks in your todo list")
    
    def test_list_command_with_empty_list(self):
        """Test that the list command shows appropriate message for empty list."""
        result = self.command_handler.handle_command("list")
        
        # Verify the response for empty list
        self.assertEqual(result, "No tasks in your todo list")
    
    def test_view_command_with_one_task(self):
        """Test that the view command shows a single task correctly."""
        # Add a task first
        self.command_handler.handle_command("add Buy groceries")
        
        result = self.command_handler.handle_command("view")
        
        # Verify the response shows the task correctly
        self.assertIn("[1]. Buy groceries - Incomplete", result)
        self.assertNotIn("No tasks in your todo list", result)
    
    def test_list_command_with_multiple_tasks(self):
        """Test that the list command shows multiple tasks correctly."""
        # Add tasks first
        self.command_handler.handle_command("add Buy groceries")
        self.command_handler.handle_command("add Finish report")
        
        result = self.command_handler.handle_command("list")
        
        # Verify the response shows all tasks correctly
        self.assertIn("[1]. Buy groceries - Incomplete", result)
        self.assertIn("[2]. Finish report - Incomplete", result)
        self.assertNotIn("No tasks in your todo list", result)
    
    def test_view_command_with_completed_tasks(self):
        """Test that the view command shows completed tasks correctly."""
        # Add and complete a task
        self.command_handler.handle_command("add Buy groceries")
        self.command_handler.handle_command("complete 1")
        
        result = self.command_handler.handle_command("view")
        
        # Verify the response shows the completed task correctly
        self.assertIn("[1]. Buy groceries - Complete", result)
        self.assertNotIn("Incomplete", result)
    
    def test_list_command_with_mixed_completed_and_incomplete_tasks(self):
        """Test that the list command shows mixed completed/incomplete tasks correctly."""
        # Add tasks first
        self.command_handler.handle_command("add Buy groceries")
        self.command_handler.handle_command("add Finish report")
        self.command_handler.handle_command("add Call mom")
        
        # Complete one task
        self.command_handler.handle_command("complete 2")
        
        result = self.command_handler.handle_command("list")
        
        # Verify the response shows all tasks with correct status
        self.assertIn("[1]. Buy groceries - Incomplete", result)
        self.assertIn("[2]. Finish report - Complete", result)
        self.assertIn("[3]. Call mom - Incomplete", result)


if __name__ == '__main__':
    unittest.main()