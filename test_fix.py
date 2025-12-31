import sys
import os
# Add the current directory to Python path
sys.path.insert(0, os.path.join(os.getcwd()))

from src.models.task import TaskList
from src.services.todo_service import TodoService
from src.cli.command_handler import CommandHandler

# Test the specific case
task_list = TaskList()
todo_service = TodoService(task_list)
command_handler = CommandHandler(todo_service)

# Add a task first so we can update it
result = command_handler.handle_command('add Test task')
print('Add result:', result)

# Now test the problematic update command
result = command_handler.handle_command('update 1   ')
print('Update with spaces result:', result)

# Test with just the update command and ID but no description
result = command_handler.handle_command('update 1')
print('Update with no description result:', result)