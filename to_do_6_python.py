# from functions import get_todos, write_todos
from modules import functions
import time
print("This is a to-do app.")
now = time.strftime('%d/%b/%Y %H:%M:%S')
print("It is", now)
todos = []

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):

        stripped_sentence = user_action[4:]
        todos.append(stripped_sentence + '\n')
        functions.write_todos('todos.txt', todos)

    elif user_action.startswith('show'):
        print("To-do activities are: ")
        todos = functions.get_todos()
        for index, item in enumerate(todos):
            index = index + 1
            item = item.strip("\n")
            row = f"{index}-{item}"
            print(row)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            print(number)

            number = number - 1
            todos = functions.get_todos()  #
            new_todo = input("Enter a new to-do: ")
            todos[number] = new_todo + '\n'

            functions.write_todos('todos.txt', todos)
        except ValueError:
            print("Your command is not valid, try again")
            continue
    elif user_action.startswith('complete'):
        try:
            todos = functions.get_todos()
            delete = int(user_action.replace("complete ", ""))
            delete = delete - 1
            item = todos.pop(delete)
            functions.write_todos('todos.txt', todos)
            print("Item deleted: ", item)
        except IndexError:
            print("Your command is not valid, try again")
            continue

    elif user_action.startswith('exit'):
        break
    else:
        print("Invalid command")

print("Bye")
