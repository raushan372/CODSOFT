import json
import os

TASKS_FILE = "tasks.json"

def load_tasks():
    """Load tasks from the JSON file."""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    """Save tasks to the JSON file."""
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

def display_tasks(tasks):
    """Display the list of tasks with status."""
    if not tasks:
        print("No tasks found.\n")
        return

    print("\nYour To-Do List:")
    for idx, task in enumerate(tasks, start=1):
        status = "✅" if task['done'] else "❌"
        print(f"{idx}. [{status}] {task['title']}")
    print()

def add_task(tasks):
    """Add a new task."""
    title = input("Enter task title: ").strip()
    if title:
        tasks.append({'title': title, 'done': False})
        print("Task added successfully.\n")
    else:
        print("Task title cannot be empty.\n")

def mark_task_done(tasks):
    """Mark a task as done."""
    display_tasks(tasks)
    try:
        index = int(input("Enter task number to mark as done: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]['done'] = True
            print("Task marked as done.\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

def delete_task(tasks):
    """Delete a task from the list."""
    display_tasks(tasks)
    try:
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            print(f"Task '{removed['title']}' deleted.\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

def main():
    """Main function to run the To-Do app."""
    tasks = load_tasks()

    while True:
        print("------ To-Do List Menu ------")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            mark_task_done(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            save_tasks(tasks)
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
