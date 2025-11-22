tasks = []
with open('py/todolist/tasks.txt', 'r') as file:
    tasks = [line.strip() for line in file]

valid_nums = (1, 2, 3, 4)
while True:
    print("\n1 - Add task")
    print("2 - Remove task")
    print("3 - View tasks")
    print("4 - Exit")
    user_input = 0
    while user_input == 0:
        try:
            user_input = int(input("Choose an option: "))
            if user_input not in valid_nums:
                user_input = 0
        except ValueError:
            print("Invalid Input")
    if user_input == 1:
        add_task = input("Add new task: ").strip()
        tasks.append(add_task)
        print("Task added succesfully")
    elif user_input == 2:
        if not tasks:
            print("No tasks to remove.\n")
        else:
            print("\nYour Tasks")
            for index, task in enumerate(tasks, 1):
                print(index, task)
            remove_task = 0
            while remove_task == 0 or remove_task < 1 or remove_task > len(tasks):
                try:
                    remove_task = int(input("Choose a task to remove: "))
                except ValueError:
                    print("Wrong input. Try again")
            tasks.pop(remove_task - 1)
            print("Task removed succesfully")
    elif user_input == 3:
        if not tasks:
            print("No tasks to view.\n")
        else:
            print("\nYour Tasks")
            for index, task in enumerate(tasks, 1):
                print(index, task)   
    else:
        with open('py/todolist/tasks.txt', 'w') as file:
            for task in tasks:
                file.write(task + '\n')
        print("Exiting the program...")
        break