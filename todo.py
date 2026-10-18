
# CodeOrbit Tech - Python Internship
# Task 2: To-Do List CLI App

# Store all tasks in a list
tasks = []


# Function to add a new task
def add_task():
    task = input("Enter your task: ").strip()

    if task:
        tasks.append(task)
        print("Task added successfully!")
    else:
        print("Task cannot be empty.")


# Function to view all tasks
def view_tasks():
    if not tasks:
        print("\nYour to-do list is empty.")
    else:
        print("\n======= YOUR TO-DO LIST =======")

        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

        print("===============================")


# Function to remove a task
def remove_task():
    view_tasks()

    if not tasks:
        return

    try:
        task_number = int(input("Enter the task number to remove: "))

        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            print(f"Task '{removed_task}' removed successfully!")
        else:
            print("Invalid task number. Please try again.")

    except ValueError:
        print("Invalid input! Please enter a number.")


# Main function to run the application
def main():
    while True:
        print("\n======= TO-DO LIST APP =======")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            add_task()

        elif choice == "2":
            view_tasks()

        elif choice == "3":
            remove_task()

        elif choice == "4":
            print("Thank you for using the To-Do List App!")
            break

        else:
            print("Invalid choice! Please select between 1 and 4.")


# Start the application
if __name__ == "__main__":
    main()
