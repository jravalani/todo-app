import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a todo")
input_box = sg.InputText(tooltip="Enter todo")
add_button = sg.Button("Add")

window = sg.Window("To-do App", layout=[[label], [input_box, add_button]])
window.read()
print("Hello")
window.close()
