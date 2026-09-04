todos = []


def show_todos():
    if not todos:
        print("No todos found.")
        return

    print("\n--- Todo List ---")

    for todo in todos:
        status = "Completed" if todo["completed"] else "Pending"
        print(f'{todo["id"]}. {todo["title"]} - {status}')


def complete_todo():
    show_todos()

    if not todos:
        return

    try:
        todo_id = int(input("\nEnter todo ID to complete: "))

        for todo in todos:
            if todo["id"] == todo_id:
                todo["completed"] = True
                print("Todo completed!")
                return

        print("Todo not found.")

    except ValueError:
        print("Please enter a valid ID.")