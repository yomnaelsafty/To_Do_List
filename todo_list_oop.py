def add_task(todo_list):
    """
    Prompts the user to enter a task and adds it to the todo_list.

    Parameters:
    todo_list (list): The list storing all tasks.
    """
    task = input("Enter a task: ")
    todo_list.append(task)
    print("Your task is added")


def view_tasks(todo_list):
    """
    Displays all tasks in the todo_list. If the list is empty, notifies the user.

    Parameters:
    todo_list (list): The list storing all tasks.
    """
    if not todo_list:
        print("No tasks to display")
    else:
        print("Your tasks:")
        for task in todo_list:
            print(f"- {task}")


def remove_task(todo_list):
    """
    Prompts the user to enter a task and removes it from the todo_list if it exists.
    If the task is not found, notifies the user.

    Parameters:
    todo_list (list): The list storing all tasks.
    """
    if not todo_list:
        print("No tasks to remove")
    else:
        task = input("Enter a task to remove: ")
        if task in todo_list:
            todo_list.remove(task)
            print("Your task is removed")
        else:
            print("Task not found")


def main():
    """
    Main loop of the program that handles user input and calls the appropriate functions
    based on the command given by the user.
    """
    todo_list = []

    while True:
        user_action = input("Enter a command (add, view, remove, exit): ").strip().lower()

        if user_action == "add":
            add_task(todo_list)
        elif user_action == "view":
            view_tasks(todo_list)
        elif user_action == "remove":
            remove_task(todo_list)
        elif user_action == "exit":
            print("Goodbye!")
            break
        else:
            print("Invalid command")


# Entry point of the script
if __name__ == "__main__":
    main()
