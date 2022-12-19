import functions
import PySimpleGUI as psg

label = psg.Text("Enter a new task")
input_box = psg.InputText(tooltip="Enter a task", key="new_task", size=[40, 1])
add_button = psg.Button("Add")
list_box = psg.Listbox(values=functions.get_todo_list(), key="todo_list",
                       enable_events=True, size=[45, 10])
edit_button = psg.Button("    Edit    ")
comp_button = psg.Button("Complete")
exit_button = psg.Button("Exit")

l_col_cont = [[label],
             [add_button, input_box],
             [list_box],
             [exit_button]]

r_col_cont = [[edit_button],
             [comp_button]]

left_col = psg.Column(l_col_cont)
right_col = psg.Column(r_col_cont)

layout = [[left_col, right_col]]

window = psg.Window(
    'My To-Do App',
        layout,
        font=('Helvetica', 15))

#window = psg.Window(
#    'My To-Do App',
#        layout=[
#            [label],
#            [add_button, input_box],
#            [list_box, edit_button],
#            [comp_button, exit_button]],
#        font=('Helvetica', 15))

while True:
    event, values = window.read()
    print(1, event)
    print(2, values)
    print(3, values['todo_list'])
    match event:
        case "Add":
            todo_list = functions.get_todo_list()
            new_todo = values['new_task'].capitalize() + "\n"
            todo_list.append(new_todo)
            functions.write_todo_list(todo_list)
            window['todo_list'].update(values=todo_list)
        case "    Edit    ":
            edit_task = values['todo_list'][0]
            new_task = values['new_task']
            todo_list = functions.get_todo_list()
            index = todo_list.index(edit_task)
            todo_list[index] = new_task + "\n"
            functions.write_todo_list(todo_list)
            window['todo_list'].update(values=todo_list)
        case "Complete":
            comp_task = values['todo_list'][0]
            comp_todos = functions.get_todo_list()
            comp_todos.remove(comp_task)
            functions.write_todo_list(comp_todos)
            window['todo_list'].update(values=comp_todos)
            window['new_task'].update(value="")
        case "Exit":
            break
        case "todo_list":
            window['new_task'].update(value=values["todo_list"][0].strip('\n'))
        case psg.WIN_CLOSED:
            break

window.close()
