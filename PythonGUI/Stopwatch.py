import PySimpleGUI as sg

layout = [
    [sg.Text('')],
    [sg.Button('Start'), sg.Button('lap')]
]

window = sg.Window('Default', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

window.close()