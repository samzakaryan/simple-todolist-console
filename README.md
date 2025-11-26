# Task Manager

A simple command-line task management application written in Python. This program allows users to manage their daily tasks through an interactive menu system with persistent storage.

## Features

- Add new tasks to your list
- Remove existing tasks by selection
- View all current tasks
- Automatic task persistence to file
- Input validation and error handling
- Clean, formatted console interface

## Requirements

- Python 3.x
- No external dependencies required

## Installation

1. Clone or download this repository
2. Ensure you have Python 3 installed on your system
3. No additional setup required

## Usage

Run the program from your terminal:

```bash
python task_manager.py
```

### Menu Options

The program presents a menu with four options:

1. **Add Task** - Enter a new task to add to your list
2. **Remove Task** - Select and remove a task from your list
3. **View Tasks** - Display all current tasks
4. **Exit** - Save all tasks and close the program

### Data Storage

Tasks are automatically saved to `tasks.txt` when you exit the program. The file will be created in the same directory as the script if it doesn't exist. Previous tasks are loaded when you start the program.

## How It Works

- Tasks are stored in memory during program execution
- On startup, the program reads existing tasks from `tasks.txt`
- When you exit, all current tasks are written back to the file
- Each task is stored on a separate line in the text file

## Example Session

```
===================================
             TASK MANAGER
===================================
1 - Add Task
2 - Remove Task
3 - View Tasks
4 - Exit
===================================
Choose an option: 1

--- ADD TASK ---
Enter new task: Complete project documentation
Task added successfully
```

## File Structure

```
.
├── task_manager.py    # Main program file
└── tasks.txt          # Task storage file (created automatically)
```

## License

MIT License
