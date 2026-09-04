def delete_todo():
    show_todos()

    if not todos:
        return

    try:
        todo_id = int(input("\nEnter todo ID to delete: "))

        for todo in todos:
            if todo["id"] == todo_id:
                todos.remove(todo)
                print("Todo deleted successfully!")
                return

        print("Todo not found.")

    except ValueError:
        print("Please enter a valid ID.")