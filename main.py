# Mark's Python Password Generator
import string
import secrets
import PySimpleGUI as sg
sg.theme('dark grey 9')
# alphabet is a variable that possesses the characters, numbers, and special characters availible to the passgen() function to use to generate passwords
# you can add or remove characters from alphabet as needed to create passwords to fit your use case
alphabet = string.ascii_letters + string.digits + "!#$%&?@"

# Function to generate passwords
# to change the length of the password generated change the number in the range function to something other than 10
# function returns generated password.
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
