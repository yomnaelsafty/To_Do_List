# main.py

from todo import ToDoList

def main():
    """
    Entry point for the to-do list app.
    """
    app = ToDoList()
    while True:
        command = input("Enter a command (add, view, remove, exit): ").strip().lower()

        if command == "add":
            app.add_task()
        elif command == "view":
            app.view_tasks()
        elif command == "remove":
            app.remove_task()
        elif command == "exit":
            print("Goodbye!")
            break
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
