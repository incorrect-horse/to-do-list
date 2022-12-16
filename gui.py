import functions
import PySimpleGUI as psg

label = psg.Text("Enter a new task")
input_box = psg.InputText(tooltip="Enter a task", key="todo")
add_button = psg.Button("Add")
comp_button = psg.Button("Complete")
edit_button = psg.Button("Edit")
exit_button = psg.Button("Exit")

window = psg.Window(
    'My To-Do App',
        layout=[
        [label],
        [input_box, add_button, comp_button],
        [edit_button],
        [exit_button]],
        font=('Helvetica', 15))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todo_list = functions.get_todo_list()
            new_todo = values['todo'] + "\n"
            todo_list.append(new_todo)
            functions.write_todo_list(todo_list)
        case psg.WIN_CLOSED:
            break

window.close()
