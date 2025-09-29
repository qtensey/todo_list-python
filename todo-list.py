#todo list

# structure:
# 1. add task
# 2. view tasks
# 3. remove task
# 4. exit

todo_list = []

def add_task():
    """
    Add a new task to the todo list.
    """
    task = input("Enter the task you want to add: ")
    todo_list.append(task)
    print("Task added.")

def view_tasks():
    """
    View all tasks in the todo list.
    """
    if len(todo_list) == 0:
        print("No tasks in the todo list.")
    else:
        print("Todo List:")
        for idx, task in enumerate(todo_list, start=1):
            print(f"{idx}. {task}")

def delete_task():
    """
    Delete a task drom the todo list.
    """
    view_tasks()
    if len(todo_list) == 0:
        return
    try:
        task_num = int(input("Enter the task numbber to delete: "))
        if 0 < task_num <= len(todo_list):
            removed_task = todo_list.pop(task_num - 1)
            print(f"Task {removed_task} removed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    """
    Main function to run the todo list application.
    """
    while True:
        print("\nTodo List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")

        choice = int(input("Choose an option (1-4): "))
        if choice == 1:
            add_task()
        elif choice == 2:
            view_tasks()
        elif choice == 3:
            delete_task()
        elif choice == 4:
            print("Exiting the todo list application.")
            break
        else:
            print("Invalid choice. Please choose a number between 1 and 4.")

if __name__ == "__main__":
    main()