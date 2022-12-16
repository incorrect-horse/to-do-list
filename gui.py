import functions
import PySimpleGUI as psg

label = psg.Text("Enter a new task")
input_box = psg.InputText(tooltip="Enter a task")
add_button = psg.Button("Add")
comp_button = psg.Button("Complete")

window = psg.Window(
    'My To-Do App',layout=[
        [label],
        [input_box, add_button, comp_button]])
window.read()
window.close()
