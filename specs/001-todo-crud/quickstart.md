# Quickstart Guide: Todo Task CRUD Application

**Feature**: 001-todo-crud
**Date**: 2025-12-25

## Getting Started

1. Ensure you have Python 3.8+ installed on your system
2. Navigate to the project directory in your terminal
3. Run the application with: `python src/main.py`
4. The application will start and display a prompt for commands

## Available Commands

### Add a Task
```
add <task description>
```
Example:
```
add Buy groceries
```

### View All Tasks
```
list
```
or
```
view
```

### Update a Task
```
update <task_id> <new description>
```
Example:
```
update 1 Buy groceries and cook dinner
```

### Delete a Task
```
delete <task_id>
```
Example:
```
delete 1
```

### Mark Task Complete
```
complete <task_id>
```
Example:
```
complete 1
```

### Get Help
```
help
```

### Exit Application
```
exit
```
or
```
quit
```

## Example Workflow

1. Start the application: `python src/main.py`
2. Add tasks:
   ```
   add Buy groceries
   add Finish report
   ```
3. View tasks:
   ```
   list
   ```
4. Mark a task complete:
   ```
   complete 1
   ```
5. View updated list:
   ```
   list
   ```
6. Exit when done:
   ```
   exit
   ```

## Important Notes

- All data is stored in memory only and will be cleared when you exit the application
- Task IDs are assigned sequentially starting from 1
- Completed tasks will be marked as such in the list view
- The application will provide error messages for invalid commands or operations