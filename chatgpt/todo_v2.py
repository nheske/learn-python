#can you change it so it shows a green check mark next to completed tasks and add a delete task feature
tasks = []

def show_menu():
    print("===== TO-DO APPLICATION =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Complete")
    print("4. Delete Task")
    print("5. Exit")

def add_task():
    task = input("Enter task description: ")
    tasks.append({"description": task, "completed": False})
    print("Task added successfully!")

def view_tasks():
    if len(tasks) == 0:
        print("No tasks to display.")
    else:
        print("----- Tasks -----")
        for index, task in enumerate(tasks):
            status = "[ ]"
            if task["completed"]:
                status = "[\u2713]"
            print(f"{index + 1}. {status} {task['description']}")

def mark_task_complete():
    if len(tasks) == 0:
        print("No tasks to mark as complete.")
    else:
        view_tasks()
        task_index = int(input("Enter the task number to mark as complete: "))
        if 1 <= task_index <= len(tasks):
            tasks[task_index - 1]["completed"] = True
            print("Task marked as complete!")
        else:
            print("Invalid task number.")

def delete_task():
    if len(tasks) == 0:
        print("No tasks to delete.")
    else:
        view_tasks()
        task_index = int(input("Enter the task number to delete: "))
        if 1 <= task_index <= len(tasks):
            deleted_task = tasks.pop(task_index - 1)
            print(f"Task '{deleted_task['description']}' deleted!")
        else:
            print("Invalid task number.")

# Main program loop
while True:
    show_menu()
    choice = input("Enter your choice (1-5): ")
    print()

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        mark_task_complete()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Exiting the program...")
        break
    else:
        print("Invalid choice. Please try again.")
    
    print()
