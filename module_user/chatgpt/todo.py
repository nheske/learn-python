# write a simple python to-do application
tasks = []

def show_menu():
    print("===== TO-DO APPLICATION =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Complete")
    print("4. Exit")

def add_task():
    task = input("Enter task description: ")
    tasks.append(task)
    print("Task added successfully!")

def view_tasks():
    if len(tasks) == 0:
        print("No tasks to display.")
    else:
        print("----- Tasks -----")
        for index, task in enumerate(tasks):
            print(f"{index + 1}. {task}")

def mark_task_complete():
    if len(tasks) == 0:
        print("No tasks to mark as complete.")
    else:
        view_tasks()
        task_index = int(input("Enter the task number to mark as complete: "))
        if 1 <= task_index <= len(tasks):
            completed_task = tasks.pop(task_index - 1)
            print(f"Task '{completed_task}' marked as complete!")
        else:
            print("Invalid task number.")

# Main program loop
while True:
    show_menu()
    choice = input("Enter your choice (1-4): ")
    print()

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        mark_task_complete()
    elif choice == "4":
        print("Exiting the program...")
        break
    else:
        print("Invalid choice. Please try again.")
    
    print()
