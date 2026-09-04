todos = []


def add_todo():
    title = input("Enter todo: ").strip()

    if not title:
        print("Todo cannot be empty.")
        return

    todo = {
        "id": len(todos) + 1,
        "title": title,
        "completed": False
    }

    todos.append(todo)

    print("✅ Todo added successfully!")


def show_todos():

    if not todos:
        print("\n📭 No todos found.")
        return

    print("\n========== TODO LIST ==========")

    for todo in todos:

        status = "✅ Completed" if todo["completed"] else "⏳ Pending"

        print(
            f'{todo["id"]}. {todo["title"]} - {status}'
        )

    print("===============================")


def update_todo():

    show_todos()

    if not todos:
        return

    try:
        todo_id = int(input("Enter todo ID: "))

        for todo in todos:

            if todo["id"] == todo_id:

                new_title = input(
                    "Enter new title: "
                ).strip()

                if new_title:
                    todo["title"] = new_title
                    print("✅ Todo updated successfully!")
                else:
                    print("❌ Title cannot be empty.")

                return

        print("❌ Todo not found.")

    except ValueError:
        print("❌ Please enter a valid ID.")


def complete_todo():

    show_todos()

    if not todos:
        return

    try:
        todo_id = int(input("Enter todo ID: "))

        for todo in todos:

            if todo["id"] == todo_id:

                todo["completed"] = True

                print("✅ Todo completed!")

                return

        print("❌ Todo not found.")

    except ValueError:
        print("❌ Please enter a valid ID.")


def delete_todo():

    show_todos()

    if not todos:
        return

    try:
        todo_id = int(input("Enter todo ID: "))

        for todo in todos:

            if todo["id"] == todo_id:

                todos.remove(todo)

                print("🗑️ Todo deleted!")

                return

        print("❌ Todo not found.")

    except ValueError:
        print("❌ Please enter a valid ID.")


def main():

    while True:

        print("""
==============================
       PYTHON TODO APP
==============================

1. Add Todo
2. Show Todos
3. Update Todo
4. Complete Todo
5. Delete Todo
6. Exit

==============================
""")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_todo()

        elif choice == "2":
            show_todos()

        elif choice == "3":
            update_todo()

        elif choice == "4":
            complete_todo()

        elif choice == "5":
            delete_todo()

        elif choice == "6":
            print("Goodbye! 👋")
            break

        else:
            print("❌ Invalid choice.")


if __name__ == "__main__":
    main()