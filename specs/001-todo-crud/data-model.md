# Data Model: Todo Task CRUD – Phase I (Console, In-Memory)

**Feature**: 001-todo-crud
**Date**: 2025-12-25

## Entities

### Task

**Description**: Represents a single todo item in the application

**Fields**:
- `id` (integer): Unique identifier for the task, assigned sequentially starting from 1
- `description` (string): The text description of the task, cannot be empty
- `completed` (boolean): Status indicating whether the task is completed, default is False

**Validation Rules**:
- `id` must be a positive integer
- `description` must be a non-empty string (1+ characters)
- `completed` must be a boolean value

**State Transitions**:
- Initial state: `completed` = False
- Transition to completed: When user marks task as complete

### TaskList

**Description**: In-memory collection that manages all Task entities in the application

**Operations**:
- `add_task(description: string)`: Creates and adds a new Task with the provided description, assigns next available ID, sets completed to False
- `get_all_tasks()`: Returns all tasks in the collection
- `get_task_by_id(id: integer)`: Returns the specific task with the given ID or None if not found
- `update_task(id: integer, new_description: string)`: Updates the description of the task with the given ID
- `delete_task(id: integer)`: Removes the task with the given ID from the collection
- `mark_complete(id: integer)`: Updates the completion status of the task with the given ID to True

**Validation Rules**:
- All operations must validate that the task ID exists before performing the operation
- Update operations must validate that the new description is not empty
- All operations must maintain data integrity within the collection

**Constraints**:
- All data exists only in memory and is cleared when the application exits
- Collection maintains order of tasks as they were added
- No duplicate IDs are allowed in the collection