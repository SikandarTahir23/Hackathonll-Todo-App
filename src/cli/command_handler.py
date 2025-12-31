"""
Command handler for the Todo application.
Parses user commands and routes them to appropriate services.
"""
from typing import Optional
from src.services.todo_service import TodoService


class CommandHandler:
    """
    Handles user commands and routes them to appropriate services.
    """
    
    def __init__(self, todo_service: TodoService):
        """
        Initialize the command handler.
        
        Args:
            todo_service (TodoService): The service to handle business logic
        """
        self.todo_service = todo_service
    
    def handle_command(self, user_input: str) -> Optional[str]:
        """
        Parse and handle a user command.
        
        Args:
            user_input (str): The raw user input
            
        Returns:
            Optional[str]: Response to display to the user, or None for no output
        """
        # Split the input into command and arguments
        parts = user_input.strip().split(' ', 1)
        command = parts[0].lower()
        args = parts[1] if len(parts) > 1 else ""
        
        # Route to appropriate command handler
        if command == "add":
            return self._handle_add(args)
        elif command in ["list", "view"]:
            return self._handle_list()
        elif command == "update":
            return self._handle_update(args)
        elif command == "delete":
            return self._handle_delete(args)
        elif command == "complete":
            return self._handle_complete(args)
        elif command == "help":
            return self._handle_help()
        elif command in ["exit", "quit"]:
            return self._handle_exit()
        else:
            return "Unknown command. Type 'help' for available commands."
    
    def _handle_add(self, args: str) -> str:
        """Handle the add command."""
        try:
            if not args.strip():
                return "Error: Task description cannot be empty"
            result = self.todo_service.add_task(args.strip())
            return f"Task {result.id} added: {result.description}"
        except ValueError as e:
            return f"Error: {str(e)}"
    
    def _handle_list(self) -> str:
        """Handle the list/view command."""
        tasks = self.todo_service.get_all_tasks()
        if not tasks:
            return "No tasks in your todo list"
        
        task_list_str = "\n".join(str(task) for task in tasks)
        return task_list_str
    
    def _handle_update(self, args: str) -> str:
        """Handle the update command."""
        try:
            # Parse task_id and new_description
            parts = args.split(' ', 1)
            if len(parts) < 2:
                return "Error: Command requires additional arguments. Use 'help' for syntax."

            try:
                task_id = int(parts[0])
            except ValueError:
                return "Error: Task ID must be a number"

            new_description = parts[1]

            # Check if the new description is empty or just whitespace
            if not new_description.strip():
                return "Error: Task description cannot be empty"

            if not self.todo_service.update_task(task_id, new_description.strip()):
                return f"Error: Task with ID {task_id} does not exist"

            return f"Task {task_id} updated: {new_description.strip()}"
        except ValueError as e:
            return f"Error: {str(e)}"
    
    def _handle_delete(self, args: str) -> str:
        """Handle the delete command."""
        try:
            if not args.strip():
                return "Error: Command requires additional arguments. Use 'help' for syntax."
            
            try:
                task_id = int(args.strip())
            except ValueError:
                return "Error: Task ID must be a number"
            
            if not self.todo_service.delete_task(task_id):
                return f"Error: Task with ID {task_id} does not exist"
            
            return f"Task {task_id} deleted"
        except Exception as e:
            return f"Error: {str(e)}"
    
    def _handle_complete(self, args: str) -> str:
        """Handle the complete command."""
        try:
            if not args.strip():
                return "Error: Command requires additional arguments. Use 'help' for syntax."
            
            try:
                task_id = int(args.strip())
            except ValueError:
                return "Error: Task ID must be a number"
            
            if not self.todo_service.mark_task_complete(task_id):
                return f"Error: Task with ID {task_id} does not exist"
            
            return f"Task {task_id} marked complete"
        except Exception as e:
            return f"Error: {str(e)}"
    
    def _handle_help(self) -> str:
        """Handle the help command."""
        help_text = """
Available commands:
  add <description>     - Add a new task
  list or view        - View all tasks
  update <id> <desc>  - Update a task description
  delete <id>         - Delete a task
  complete <id>       - Mark a task as complete
  help                - Show this help message
  exit or quit        - Exit the application
        """.strip()
        return help_text
    
    def _handle_exit(self) -> str:
        """Handle the exit command."""
        return "Goodbye!"