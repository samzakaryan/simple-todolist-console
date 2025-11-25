tasks = []
with open('tasks.txt', 'r') as file:
    tasks = [line.strip() for line in file]
valid_nums = (1, 2, 3, 4)
while True:
    print("\n" + "="*35)
    print("             TASK MANAGER")
    print("="*35)
    print("1 - Add Task")
    print("2 - Remove Task")
    print("3 - View Tasks")
    print("4 - Exit")
    print("="*35)
    user_input = 0
    while user_input == 0:
        try:
            user_input = int(input("Choose an option: "))
            if user_input not in valid_nums:
                print("Invalid option. Try 1–4.")
                user_input = 0
        except ValueError:
            print("Invalid input. Enter a number.")
    if user_input == 1:
        print("\n--- ADD TASK ---")
        add_task = input("Enter new task: ").strip()
        tasks.append(add_task)
        print("Task added successfully")
    elif user_input == 2:
        print("\n--- REMOVE TASK ---")
        if not tasks:
            print("No tasks to remove.\n")
        else:
            print("\nYour Tasks:")
            print("-"*20)
            for index, task in enumerate(tasks, 1):
                print(f"{index}. {task}")
            remove_task = 0
            while remove_task < 1 or remove_task > len(tasks):
                try:
                    remove_task = int(input("Select task number to remove: "))
                except ValueError:
                    print("Invalid number. Try again.")

            tasks.pop(remove_task - 1)
            print("Task removed successfully")
    elif user_input == 3:
        print("\n--- VIEW TASKS ---")
        if not tasks:
            print("No tasks to view.\n")
        else:
            print("\nYour Tasks:")
            print("-"*20)
            for index, task in enumerate(tasks, 1):
                print(f"{index}. {task}")
    else:
        print("\nSaving tasks...")
        with open('tasks.txt', 'w') as file:
            for task in tasks:
                file.write(task + '\n')
        print("Exiting the program...")
        break
