import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a todo")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(),
                      key='existing_todo',
                      enable_events=True,
                      size=[45,10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window("To-do App",
                   layout=[[label],
                        [input_box, add_button],
                        [list_box, edit_button, complete_button],
                        [exit_button]],
                   font=('Helvetica', 14))
while True:
    event, values = window.read()
    print(1, event)
    print(2, values)
    print(3, values['existing_todo'][0])
    match event:
        case "Add":
            todos = functions.get_todos()
            todos.append(values['todo'] + "\n")
            functions.write_todos(todos)
            window['existing_todo'].update(values=todos)

        case "Edit":
            todo_to_edit = values['existing_todo'][0]
            new_todo = values['todo'] + "\n"
            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['existing_todo'].update(values=todos)

        case "Complete":
            todo_to_complete = values['existing_todo'][0]
            print(f"Todo removed;  {todo_to_complete}")
            todos = functions.get_todos()
            todos.remove(todo_to_complete)
            functions.write_todos(todos)
            window["existing_todo"].update(values=todos)
            window["todo"].update(value="")

        case "Exit":
            break

        case "existing_todo":
            window['todo'].update(value=values['existing_todo'][0])

        case sg.WINDOW_CLOSED:
            break

window.close()
