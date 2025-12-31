"""
Todo service for the Todo application.
Implements business logic for CRUD operations and validation.
"""
from typing import List, Optional
from src.models.task import Task, TaskList


class TodoService:
    """
    Implements business logic for all CRUD operations and validation.
    """
    
    def __init__(self, task_list: TaskList):
        """
        Initialize the todo service.
        
        Args:
            task_list (TaskList): The collection to store tasks
        """
        self.task_list = task_list
    
    def add_task(self, description: str) -> Task:
        """
        Add a new task.
        
        Args:
            description (str): The task description
            
        Returns:
            Task: The newly created task
            
        Raises:
            ValueError: If description is empty
        """
        return self.task_list.add_task(description)
    
    def get_all_tasks(self) -> List[Task]:
        """
        Get all tasks.
        
        Returns:
            List[Task]: All tasks in the collection
        """
        return self.task_list.get_all_tasks()
    
    def get_task_by_id(self, task_id: int) -> Optional[Task]:
        """
        Get a task by its ID.
        
        Args:
            task_id (int): The ID of the task to retrieve
            
        Returns:
            Optional[Task]: The task with the given ID or None if not found
        """
        return self.task_list.get_task_by_id(task_id)
    
    def update_task(self, task_id: int, new_description: str) -> bool:
        """
        Update a task's description.
        
        Args:
            task_id (int): The ID of the task to update
            new_description (str): The new description for the task
            
        Returns:
            bool: True if the task was updated, False if task was not found
            
        Raises:
            ValueError: If new description is empty
        """
        return self.task_list.update_task(task_id, new_description)
    
    def delete_task(self, task_id: int) -> bool:
        """
        Delete a task.
        
        Args:
            task_id (int): The ID of the task to delete
            
        Returns:
            bool: True if the task was deleted, False if task was not found
        """
        return self.task_list.delete_task(task_id)
    
    def mark_task_complete(self, task_id: int) -> bool:
        """
        Mark a task as complete.
        
        Args:
            task_id (int): The ID of the task to mark complete
            
        Returns:
            bool: True if the task was marked complete, False if task was not found
        """
        return self.task_list.mark_complete(task_id)