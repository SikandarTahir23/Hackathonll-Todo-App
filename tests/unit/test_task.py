"""
Unit tests for the Task model.
"""
import unittest
from src.models.task import Task


class TestTask(unittest.TestCase):
    """Test cases for the Task class."""
    
    def test_task_creation_with_valid_data(self):
        """Test creating a task with valid data."""
        task = Task(1, "Buy groceries")
        self.assertEqual(task.id, 1)
        self.assertEqual(task.description, "Buy groceries")
        self.assertFalse(task.completed)
    
    def test_task_creation_with_custom_completion_status(self):
        """Test creating a task with completed status set to True."""
        task = Task(1, "Buy groceries", completed=True)
        self.assertEqual(task.id, 1)
        self.assertEqual(task.description, "Buy groceries")
        self.assertTrue(task.completed)
    
    def test_task_creation_with_empty_description_raises_error(self):
        """Test that creating a task with empty description raises ValueError."""
        with self.assertRaises(ValueError):
            Task(1, "")
    
    def test_task_creation_with_whitespace_only_description_raises_error(self):
        """Test that creating a task with whitespace-only description raises ValueError."""
        with self.assertRaises(ValueError):
            Task(1, "   ")
    
    def test_task_creation_with_negative_id_raises_error(self):
        """Test that creating a task with negative id raises ValueError."""
        with self.assertRaises(ValueError):
            Task(-1, "Buy groceries")
    
    def test_task_creation_with_zero_id_raises_error(self):
        """Test that creating a task with zero id raises ValueError."""
        with self.assertRaises(ValueError):
            Task(0, "Buy groceries")
    
    def test_task_str_representation(self):
        """Test the string representation of a task."""
        task = Task(1, "Buy groceries")
        expected = "[1]. Buy groceries - Incomplete"
        self.assertEqual(str(task), expected)
    
    def test_task_str_representation_completed(self):
        """Test the string representation of a completed task."""
        task = Task(1, "Buy groceries", completed=True)
        expected = "[1]. Buy groceries - Complete"
        self.assertEqual(str(task), expected)
    
    def test_task_repr_representation(self):
        """Test the developer representation of a task."""
        task = Task(1, "Buy groceries")
        expected = "Task(id=1, description='Buy groceries', completed=False)"
        self.assertEqual(repr(task), expected)
    
    def test_mark_task_complete(self):
        """Test marking a task as complete."""
        task = Task(1, "Buy groceries")
        self.assertFalse(task.completed)
        
        task.mark_complete()
        self.assertTrue(task.completed)
    
    def test_update_description_with_valid_data(self):
        """Test updating a task's description with valid data."""
        task = Task(1, "Buy groceries")
        self.assertEqual(task.description, "Buy groceries")
        
        task.update_description("Buy milk and bread")
        self.assertEqual(task.description, "Buy milk and bread")
    
    def test_update_description_with_empty_string_raises_error(self):
        """Test that updating a task's description with empty string raises ValueError."""
        task = Task(1, "Buy groceries")
        
        with self.assertRaises(ValueError):
            task.update_description("")
    
    def test_update_description_with_whitespace_only_raises_error(self):
        """Test that updating a task's description with whitespace-only raises ValueError."""
        task = Task(1, "Buy groceries")
        
        with self.assertRaises(ValueError):
            task.update_description("   ")


if __name__ == '__main__':
    unittest.main()