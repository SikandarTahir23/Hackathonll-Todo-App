# Todo Task Manager

A simple console-based todo application that allows users to manage tasks using CRUD operations. All tasks are stored in memory only and will be cleared when the program exits.

## Features

- Add new tasks
- View all tasks
- Update task descriptions
- Delete tasks
- Mark tasks as complete
- Simple command-line interface

## Requirements

- Python 3.8 or higher

## Installation

1. Clone or download the repository
2. Navigate to the project directory

## Usage

Run the application:

```bash
python src/main.py
```

The application will start and display a prompt for commands. Available commands include:

- `add <description>` - Add a new task
- `list` or `view` - View all tasks
- `update <id> <new description>` - Update a task description
- `delete <id>` - Delete a task
- `complete <id>` - Mark a task as complete
- `help` - Show available commands
- `exit` or `quit` - Exit the application

### Example Workflow

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

## Project Structure

```
src/
├── main.py              # Entry point and command loop
├── models/
│   └── task.py          # Task entity and TaskList collection
├── services/
│   └── todo_service.py  # Business logic for CRUD operations
└── cli/
    └── command_handler.py # Command parsing and execution
```

## Testing

Unit tests are located in the `tests/unit/` directory.
Integration tests are located in the `tests/integration/` directory.

To run tests:
```bash
python -m unittest discover tests/
```

## Architecture

The application follows a simple layered architecture:
- **Presentation Layer**: CLI interface handles user input/output via command_handler.py
- **Business Logic Layer**: todo_service.py manages all CRUD operations and validation
- **Data Layer**: task.py contains Task entity and TaskList collection in memory

## Notes

- All data is stored in memory only and will be cleared when you exit the application
- Task IDs are assigned sequentially starting from 1
- Completed tasks will be marked as such in the list view
- The application will provide error messages for invalid commands or operations