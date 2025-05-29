# todo.py

class ToDoList:
    """
    A class to manage a simple to-do list.
    """

    def __init__(self):
        """
        Initializes an empty to-do list.
        """
        self.tasks = []

    def add_task(self):
        """
        Prompts the user to enter a task and adds it to the list.
        """
        task = input("Enter a task: ")
        self.tasks.append(task)
        print("Your task is added.")

    def view_tasks(self):
        """
        Displays all the tasks in the to-do list.
        """
        if not self.tasks:
            print("No tasks to display.")
        else:
            print("Your tasks:")
            for task in self.tasks:
                print(f"- {task}")

    def remove_task(self):
        """
        Prompts the user to enter a task and removes it from the list if found.
        """
        if not self.tasks:
            print("No tasks to remove.")
        else:
            task = input("Enter a task to remove: ")
            if task in self.tasks:
                self.tasks.remove(task)
                print("Your task is removed.")
            else:
                print("Task not found.")
