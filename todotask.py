tasks = [] 
def show_menu():
    print("\n========== TO-DO LIST MENU ==========")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Mark Task as Done")
    print("5. Delete Task")
    print("6. Exit")
    print("=====================================")

def view_tasks():
    if not tasks:
        print("\nNo tasks available.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            status = "✅ Done" if task["done"] else "❌ Not Done"
            print(f"{i}. {task['title']}  -->  {status}")

def add_task():
    title = input("Enter task title: ")
    if title.strip() == "":
        print("Task title cannot be empty.")
        return
    tasks.append({"title": title, "done": False})
    print(f"Task '{title}' added successfully!")

def update_task():
    view_tasks()
    if not tasks:
        return
    try:
        task_no = int(input("\nEnter task number to update: "))
        if 1 <= task_no <= len(tasks):
            new_title = input("Enter new task title: ")
            tasks[task_no - 1]["title"] = new_title
            print("Task updated successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def mark_done():
    view_tasks()
    if not tasks:
        return
    try:
        task_no = int(input("\nEnter task number to mark as done: "))
        if 1 <= task_no <= len(tasks):
            tasks[task_no - 1]["done"] = True
            print("Task marked as done!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task():
    view_tasks()
    if not tasks:
        return
    try:
        task_no = int(input("\nEnter task number to delete: "))
        if 1 <= task_no <= len(tasks):
            deleted = tasks.pop(task_no - 1)
            print(f"Task '{deleted['title']}' deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            view_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            update_task()
        elif choice == "4":
            mark_done()
        elif choice == "5":
            delete_task()
        elif choice == "6":
            print("Exiting To-Do List... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
