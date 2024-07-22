# from functions import get_todos, write_todos
import functions
import time

current_time = time.strftime("%b %d, %Y %H:%M:%S")
# print("The time is below: ")
print(f"It is {current_time}")

user_name = 'Jay'

while True:
    user_action = input("Type add, show, edit, complete, or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]
        todo = todo.capitalize()

        # read items from todos.txt using .readlines()
        todos = functions.get_todos()

        # append the user input to the newly created list(todos)
        todos.append(todo + "\n")

        # create a new file named todos.txt and append the list using .writelines()
        functions.write_todos(todos)

    elif user_action.startswith("show"):
        todos = functions.get_todos()
        print(todos)
        for n, each_todo in enumerate(todos):
            each_todo = each_todo.strip('\n')
            print(f"{n + 1}. {each_todo}")

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])

            todos = functions.get_todos()

            print(todos[number - 1])
            new_todo = input("Enter new todo: ")
            new_todo = new_todo.capitalize()
            todos[number - 1] = new_todo + '\n'

            functions.write_todos(todos)
        except ValueError:
            print("Invalid Command. You need to enter the todo number instead of typing the entire thing.")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = functions.get_todos()
            index = number - 1
            todo_to_remove = todos[index].strip("\n")
            todos.pop(index)

            functions.write_todos(todos)
            print(f"{todo_to_remove} was removed from the list.")

            for index, x in enumerate(todos):
                x = x.strip('\n')
                print(f"{index + 1}. {x}")
        except ValueError:
            print("Invalid Command. You need to enter the todo number instead of typing the entire thing.")
            continue
        except IndexError:
            print("Invalid Command. Index out of range!")
            continue

    elif user_action.startswith("exit"):
        break
    else:
        print("You entered an incorrect command!")

print("Bye!")
