# Mark's Python Password Generator
import string
import secrets
import PySimpleGUI as sg
sg.theme('dark grey 9')
alphabet = string.ascii_letters + string.digits + "!#$%&?@"

def passgen():
    password = ''.join(secrets.choice(alphabet) for i in range(10))
    return password

if __name__ == '__main__':
    layout = [[sg.Text("Mark's Python Password Generator")],
              [sg.Text("New 10 Character password: ")],
              [sg.Text(size=(20, 1), key='-OUTPUT-')],
              [sg.Button("Run!"), sg.Button("Exit")]]
    window = sg.Window("MPPG", layout)
    event, values = window.read()
    password = passgen()
    window['-OUTPUT-'].update(password, text_color='yellow')
    while True:
        event, values = window.read()
        if event == "Run!":
            password = passgen()
            window['-OUTPUT-'].update(password, text_color='yellow')
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
    window.close()