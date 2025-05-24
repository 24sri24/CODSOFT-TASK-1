def display_menu():
    print("\nTo-Do List Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

def add_task(tasks):
    task = input("Enter the task to add: ")
    tasks.append(task)
    print(f"Task '{task}' added.")

def view_tasks(tasks):
    if tasks:
        print("\nTo-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    else:
        print("To-do list is empty.")

def remove_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            task_num = int(input("Enter the number to removes the task: "))
            removed_task = tasks.pop(task_num - 1)
            print(f"Task '{removed_task}' removed.")
        except (ValueError, IndexError):
            print("Invalid task number is entered.")

def main():
    tasks = []
    while True:
        display_menu()
        try:
            choice = int(input("Choose option: "))
            if choice == 1:
                add_task(tasks)
            elif choice == 2:
                view_tasks(tasks)
            elif choice == 3:
                remove_task(tasks)
            elif choice == 4:
                print("Exit")
                break
            else:
                print("Please select a valid option.")
        except ValueError:
            print("Enter a valid number.")

if __name__ == "__main__":
    main()

