todos = []


def add_todo():
    title = input("Enter todo: ")

    todo = {
        "id": len(todos) + 1,
        "title": title,
        "completed": False
    }

    todos.append(todo)

    print("Todo added successfully!")


def show_todos():
    if not todos:
        print("No todos found.")
        return

    print("\n--- Todo List ---")

    for todo in todos:
        status = "Completed" if todo["completed"] else "Pending"

        print(
            f'{todo["id"]}. {todo["title"]} - {status}'
        )


add_todo()
show_todos()