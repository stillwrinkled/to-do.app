from modules import functions
import PySimpleGUI as sg
import time

sg.theme("TealMono")
clock = sg.Text("", key='clock', font=("Ariel", 10), text_color="grey")

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo: ", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")
error_message = sg.Text("", size=(30, 1), text_color="red", key="error_message")

layout = [[clock],[label],[input_box, add_button], [list_box], [edit_button, complete_button, exit_button]]

window = sg.Window('My To-Do App', layout, font=('Ariel', 20))

while True:
    event, values = window.read(timeout=10)
    window["clock"].update(time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case 'Add':
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(todos)
        case 'Edit':
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo + "\n"
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                print(index)
            except IndexError:
                error_text = "Select a to-do item first > type in a new to-do and click \'Edit\'"
                sg.popup(error_text, font=('Ariel', 18))
        case 'Complete':
            try:
                completed_task = values['todos'][0]
                todos = functions.get_todos()
                index = todos.index(completed_task)
                todos.pop(index)
                functions.write_todos(todos)
                window['todos'].update(todos)
                window['todo'].update("")
            except IndexError:
                error_text = "Select a to-do item first & click \'Complete\'"
                sg.popup(error_text, font=('Ariel', 18))

        case 'todos':
            value_to_show = values['todos'][0]
            window['todo'].update(value_to_show)

        case 'Exit':
            break

        case sg.WIN_CLOSED:
            break

print("Bye")
window.close()
