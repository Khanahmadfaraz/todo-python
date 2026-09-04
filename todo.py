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


add_todo()

print(todos)