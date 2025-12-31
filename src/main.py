#!/usr/bin/env python3
"""
Main entry point for the Todo Task CRUD application.
Implements a console-based interface for managing tasks.
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.cli.command_handler import CommandHandler
from src.services.todo_service import TodoService
from src.models.task import TaskList


def main():
    """
    Main application entry point.
    Initializes services and starts the command loop.
    """
    print("Welcome to the Todo Task Manager!")
    print("Type 'help' for available commands or 'exit' to quit.")
    
    # Initialize the task storage
    task_list = TaskList()
    
    # Initialize the business logic service
    todo_service = TodoService(task_list)
    
    # Initialize the command handler
    command_handler = CommandHandler(todo_service)
    
    # Start the command loop
    while True:
        try:
            # Get user input
            user_input = input("\ntodo> ").strip()
            
            # Handle empty input
            if not user_input:
                continue
            
            # Process the command
            result = command_handler.handle_command(user_input)
            
            # Display the result
            if result:
                print(result)
                
            # Exit if command handler indicates to exit
            if user_input.lower() in ['exit', 'quit']:
                break
                
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break
        except EOFError:
            print("\n\nGoodbye!")
            break


if __name__ == "__main__":
    main()