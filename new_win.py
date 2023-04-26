from modules import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo: ", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")

error_message = sg.Text("", size=(30, 1), text_color="red", key="error_message")

window = sg.Window('My To-Do App',
                   layout=[[label], [input_box, add_button], [list_box, edit_button], [error_message]],
                   font=('Ariel', 20))
while True:
    event, values = window.read()
    print("Event: ", event)
    print("Values: ", values)
    print(values['todos'])
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
                window['error_message'].update("")
                print(index)
            except IndexError:
                error_text = "Select a To-do item first"
                window['error_message'].update(error_text)
                print("An IndexError occurred. Please make sure you selected a todo item.")

                # todos = functions.get_todos()
                # todos.append(new_todo)
        case 'todos':
            value_to_show = values['todos'][0]
            print(value_to_show)
            window['todo'].update(value_to_show)

        case sg.WIN_CLOSED:
            break
