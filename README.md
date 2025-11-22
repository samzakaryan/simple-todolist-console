# To-Do List

A simple command-line to-do list application built with Python. Manage your tasks with an easy-to-use menu system and automatic file saving.

## Features

- ✅ Add new tasks
- ❌ Remove completed tasks by number
- 📋 View all tasks with numbered list
- 💾 Automatic saving - tasks persist between sessions
- ✔️ Input validation to prevent errors
- 🔄 Loads previous tasks on startup

## Requirements

- Python 3.x

## Setup

1. Clone the repository:
```bash
   git clone https://github.com/yourusername/todolist.git
   cd todolist
```

2. Create a `tasks.txt` file in the same directory (or it will be created automatically):
```bash
   touch tasks.txt
```

## How to Use

Run the program:
```bash
python todolist.py
```

### Menu Options:
- **1** - Add a new task
- **2** - Remove a task (by number)
- **3** - View all tasks
- **4** - Exit and save

## Example Usage
```
1 - Add task
2 - Remove task
3 - View tasks
4 - Exit
Choose an option: 1
Add new task: Buy groceries
Task added successfully

Choose an option: 3

Your Tasks
1 Buy groceries
2 Finish homework
3 Call dentist

Choose an option: 2

Your Tasks
1 Buy groceries
2 Finish homework
3 Call dentist
Choose a task to remove: 2
Task removed successfully
```

## File Structure
```
todolist/
├── todolist.py      # Main program
└── tasks.txt        # Saved tasks (auto-generated)
```

## How It Works

- Tasks are stored in `tasks.txt`
- On startup, the program loads existing tasks
- When you exit (option 4), all tasks are automatically saved
- Input validation prevents crashes from invalid entries

## Future Improvements

- [ ] Mark tasks as complete without removing them
- [ ] Add task priority levels
- [ ] Add due dates for tasks
- [ ] Search/filter tasks
- [ ] Edit existing tasks

## License

MIT License
