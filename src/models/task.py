"""
Task model for the Todo application.
Represents a single todo item with id, description, and completion status.
"""
from typing import List, Optional


class Task:
    """
    Represents a single todo item in the application.
    
    Attributes:
        id (int): Unique identifier for the task, assigned sequentially starting from 1
        description (str): The text description of the task, cannot be empty
        completed (bool): Status indicating whether the task is completed, default is False
    """
    
    def __init__(self, task_id: int, description: str, completed: bool = False):
        """
        Initialize a Task instance.
        
        Args:
            task_id (int): Unique identifier for the task
            description (str): The task description
            completed (bool): Whether the task is completed (default: False)
        
        Raises:
            ValueError: If description is empty or id is not positive
        """
        if not description or not description.strip():
            raise ValueError("Task description cannot be empty")
        if task_id <= 0:
            raise ValueError("Task id must be a positive integer")
            
        self.id = task_id
        self.description = description.strip()
        self.completed = completed
    
    def __str__(self):
        """String representation of the task."""
        status = "Complete" if self.completed else "Incomplete"
        return f"[{self.id}]. {self.description} - {status}"
    
    def __repr__(self):
        """Developer representation of the task."""
        return f"Task(id={self.id}, description='{self.description}', completed={self.completed})"
    
    def mark_complete(self):
        """Mark the task as complete."""
        self.completed = True
    
    def update_description(self, new_description: str):
        """
        Update the task description.
        
        Args:
            new_description (str): The new description for the task
            
        Raises:
            ValueError: If new description is empty
        """
        if not new_description or not new_description.strip():
            raise ValueError("Task description cannot be empty")
        self.description = new_description.strip()


class TaskList:
    """
    In-memory collection that manages all Task entities in the application.
    """
    
    def __init__(self):
        """Initialize an empty TaskList."""
        self._tasks: List[Task] = []
        self._next_id = 1
    
    def add_task(self, description: str) -> Task:
        """
        Creates and adds a new Task with the provided description, 
        assigns next available ID, sets completed to False.
        
        Args:
            description (str): The task description to add
            
        Returns:
            Task: The newly created task
            
        Raises:
            ValueError: If description is empty
        """
        if not description or not description.strip():
            raise ValueError("Task description cannot be empty")
            
        task = Task(self._next_id, description.strip())
        self._tasks.append(task)
        self._next_id += 1
        return task
    
    def get_all_tasks(self) -> List[Task]:
        """
        Returns all tasks in the collection.
        
        Returns:
            List[Task]: All tasks in the collection
        """
        return self._tasks.copy()
    
    def get_task_by_id(self, task_id: int) -> Optional[Task]:
        """
        Returns the specific task with the given ID or None if not found.
        
        Args:
            task_id (int): The ID of the task to retrieve
            
        Returns:
            Optional[Task]: The task with the given ID or None if not found
        """
        for task in self._tasks:
            if task.id == task_id:
                return task
        return None
    
    def update_task(self, task_id: int, new_description: str) -> bool:
        """
        Updates the description of the task with the given ID.
        
        Args:
            task_id (int): The ID of the task to update
            new_description (str): The new description for the task
            
        Returns:
            bool: True if the task was updated, False if task was not found
            
        Raises:
            ValueError: If new description is empty
        """
        if not new_description or not new_description.strip():
            raise ValueError("Task description cannot be empty")
            
        task = self.get_task_by_id(task_id)
        if task:
            task.update_description(new_description)
            return True
        return False
    
    def delete_task(self, task_id: int) -> bool:
        """
        Removes the task with the given ID from the collection.
        
        Args:
            task_id (int): The ID of the task to delete
            
        Returns:
            bool: True if the task was deleted, False if task was not found
        """
        task = self.get_task_by_id(task_id)
        if task:
            self._tasks.remove(task)
            return True
        return False
    
    def mark_complete(self, task_id: int) -> bool:
        """
        Updates the completion status of the task with the given ID to True.
        
        Args:
            task_id (int): The ID of the task to mark complete
            
        Returns:
            bool: True if the task was marked complete, False if task was not found
        """
        task = self.get_task_by_id(task_id)
        if task:
            task.mark_complete()
            return True
        return False