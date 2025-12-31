"""
Unit tests for the TaskList collection.
"""
import unittest
from src.models.task import TaskList, Task


class TestTaskList(unittest.TestCase):
    """Test cases for the TaskList class."""
    
    def setUp(self):
        """Set up a fresh TaskList for each test."""
        self.task_list = TaskList()
    
    def test_add_task_with_valid_description(self):
        """Test adding a task with valid description."""
        task = self.task_list.add_task("Buy groceries")
        
        self.assertIsInstance(task, Task)
        self.assertEqual(task.id, 1)
        self.assertEqual(task.description, "Buy groceries")
        self.assertFalse(task.completed)
        
        # Verify the task is in the list
        all_tasks = self.task_list.get_all_tasks()
        self.assertEqual(len(all_tasks), 1)
        self.assertEqual(all_tasks[0].id, 1)
    
    def test_add_task_with_empty_description_raises_error(self):
        """Test that adding a task with empty description raises ValueError."""
        with self.assertRaises(ValueError):
            self.task_list.add_task("")
    
    def test_add_task_with_whitespace_only_description_raises_error(self):
        """Test that adding a task with whitespace-only description raises ValueError."""
        with self.assertRaises(ValueError):
            self.task_list.add_task("   ")
    
    def test_add_multiple_tasks_increments_ids(self):
        """Test that adding multiple tasks increments IDs sequentially."""
        task1 = self.task_list.add_task("First task")
        task2 = self.task_list.add_task("Second task")
        task3 = self.task_list.add_task("Third task")
        
        self.assertEqual(task1.id, 1)
        self.assertEqual(task2.id, 2)
        self.assertEqual(task3.id, 3)
        
        all_tasks = self.task_list.get_all_tasks()
        self.assertEqual(len(all_tasks), 3)
    
    def test_get_all_tasks_returns_empty_list_initially(self):
        """Test that get_all_tasks returns an empty list initially."""
        all_tasks = self.task_list.get_all_tasks()
        self.assertEqual(len(all_tasks), 0)
        self.assertEqual(all_tasks, [])
    
    def test_get_all_tasks_returns_all_added_tasks(self):
        """Test that get_all_tasks returns all added tasks."""
        self.task_list.add_task("First task")
        self.task_list.add_task("Second task")
        
        all_tasks = self.task_list.get_all_tasks()
        self.assertEqual(len(all_tasks), 2)
        self.assertEqual(all_tasks[0].description, "First task")
        self.assertEqual(all_tasks[1].description, "Second task")
    
    def test_get_task_by_id_returns_correct_task(self):
        """Test that get_task_by_id returns the correct task."""
        task1 = self.task_list.add_task("First task")
        task2 = self.task_list.add_task("Second task")
        
        retrieved_task = self.task_list.get_task_by_id(1)
        self.assertEqual(retrieved_task.id, task1.id)
        self.assertEqual(retrieved_task.description, "First task")
        
        retrieved_task = self.task_list.get_task_by_id(2)
        self.assertEqual(retrieved_task.id, task2.id)
        self.assertEqual(retrieved_task.description, "Second task")
    
    def test_get_task_by_id_returns_none_for_nonexistent_task(self):
        """Test that get_task_by_id returns None for non-existent task."""
        self.task_list.add_task("First task")
        
        retrieved_task = self.task_list.get_task_by_id(99)
        self.assertIsNone(retrieved_task)
    
    def test_update_task_updates_description(self):
        """Test that update_task updates the description."""
        self.task_list.add_task("Old description")
        
        result = self.task_list.update_task(1, "New description")
        
        self.assertTrue(result)
        task = self.task_list.get_task_by_id(1)
        self.assertEqual(task.description, "New description")
    
    def test_update_task_returns_false_for_nonexistent_task(self):
        """Test that update_task returns False for non-existent task."""
        result = self.task_list.update_task(99, "New description")
        
        self.assertFalse(result)
    
    def test_update_task_with_empty_description_raises_error(self):
        """Test that update_task with empty description raises ValueError."""
        self.task_list.add_task("Old description")
        
        with self.assertRaises(ValueError):
            self.task_list.update_task(1, "")
    
    def test_delete_task_removes_task(self):
        """Test that delete_task removes the task."""
        self.task_list.add_task("First task")
        self.task_list.add_task("Second task")
        
        result = self.task_list.delete_task(1)
        
        self.assertTrue(result)
        all_tasks = self.task_list.get_all_tasks()
        self.assertEqual(len(all_tasks), 1)
        self.assertEqual(all_tasks[0].id, 2)
    
    def test_delete_task_returns_false_for_nonexistent_task(self):
        """Test that delete_task returns False for non-existent task."""
        result = self.task_list.delete_task(99)
        
        self.assertFalse(result)
    
    def test_mark_complete_marks_task_as_complete(self):
        """Test that mark_complete marks the task as complete."""
        self.task_list.add_task("First task")
        
        result = self.task_list.mark_complete(1)
        
        self.assertTrue(result)
        task = self.task_list.get_task_by_id(1)
        self.assertTrue(task.completed)
    
    def test_mark_complete_returns_false_for_nonexistent_task(self):
        """Test that mark_complete returns False for non-existent task."""
        result = self.task_list.mark_complete(99)
        
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()