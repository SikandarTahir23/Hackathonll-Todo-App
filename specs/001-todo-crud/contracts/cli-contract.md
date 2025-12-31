# API Contract: Todo Task CRUD CLI Commands

**Feature**: 001-todo-crud
**Date**: 2025-12-25

## Command Interface

This application provides a command-line interface where users interact by entering commands. Each command follows a specific format and returns predictable responses.

### Add Task Command
- **Command**: `add <description>`
- **Parameters**: 
  - `description` (string): The task description to add
- **Success Response**: "Task [ID] added: [description]"
- **Error Response**: "Error: Task description cannot be empty"
- **Validation**: 
  - Description must not be empty
  - Task is added to the in-memory list with completed=False

### View Tasks Command
- **Command**: `list` or `view`
- **Parameters**: None
- **Success Response**: 
  - For each task: "[ID]. [Description] - [Complete/Incomplete]"
  - If no tasks: "No tasks in your todo list"
- **Error Response**: None
- **Validation**: None

### Update Task Command
- **Command**: `update <task_id> <new_description>`
- **Parameters**:
  - `task_id` (integer): The ID of the task to update
  - `new_description` (string): The new description for the task
- **Success Response**: "Task [ID] updated: [new_description]"
- **Error Response**: 
  - "Error: Task with ID [X] does not exist"
  - "Error: Task description cannot be empty"
- **Validation**:
  - Task ID must exist in the list
  - New description must not be empty

### Delete Task Command
- **Command**: `delete <task_id>`
- **Parameters**:
  - `task_id` (integer): The ID of the task to delete
- **Success Response**: "Task [ID] deleted"
- **Error Response**: "Error: Task with ID [X] does not exist"
- **Validation**:
  - Task ID must exist in the list

### Mark Task Complete Command
- **Command**: `complete <task_id>`
- **Parameters**:
  - `task_id` (integer): The ID of the task to mark complete
- **Success Response**: "Task [ID] marked complete"
- **Error Response**: "Error: Task with ID [X] does not exist"
- **Validation**:
  - Task ID must exist in the list

### Help Command
- **Command**: `help`
- **Parameters**: None
- **Success Response**: List of all available commands with brief descriptions
- **Error Response**: None
- **Validation**: None

### Exit Command
- **Command**: `exit` or `quit`
- **Parameters**: None
- **Success Response**: Application terminates
- **Error Response**: None
- **Validation**: None

## Error Handling

All commands follow a consistent error response format:
- Format: "Error: [specific error description]"
- Errors are displayed to the user without application termination
- Invalid commands return: "Unknown command. Type 'help' for available commands."
- Missing arguments return: "Error: Command requires additional arguments. Use 'help' for syntax."

## State Management

- All data is stored in memory only
- Data is cleared when the application exits
- Task IDs are assigned sequentially starting from 1
- New tasks have completed=False by default