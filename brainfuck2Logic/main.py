import PySimpleGUI as sg
from Translation.bf2Translator import BF2Translator
import os


def main():
    layout = [
        [
            sg.Text("Translate your Brainfuck2 code to C!")
        ],
        [
            sg.Text("Input file:", size=(8, 1)),
            sg.In(enable_events=True, key="-INPUT-"),
            sg.FileBrowse(size=(8, 1)),
        ],
        [
            sg.Text("Output File:", size=(8, 1)),
            sg.In(enable_events=True, key="-OUTPUT-"),
            # sg.FileBrowse(),
            sg.FileSaveAs(enable_events=True, key="-OUTPUT-", size=(8, 1)),
        ],
        [
            sg.Button("Submit", key="-SUBMIT-", size=(8, 1))
        ]
    ]

    window = sg.Window("Bf2C", layout)
    while True:
        event, values = window.read()

        if event == "-SUBMIT-":
            if values["-INPUT-"] == "" or not os.path.exists(values["-INPUT-"]):
                sg.popup("Invalid input file")
            elif values["-OUTPUT-"] == "":
                sg.popup("Invalid output file")
            elif values["-OUTPUT-"][-1] != 'c':
                sg.popup("Output file has to be .c")
            else:
                tr = BF2Translator(values["-INPUT-"], values["-OUTPUT-"])
                tr.translate()
                sg.popup(f"File {values['-OUTPUT-']} succesfully created")
                

        if event == "Exit" or event == sg.WIN_CLOSED:
            break
    window.close()

main()
