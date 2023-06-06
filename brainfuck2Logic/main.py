import PySimpleGUI as sg
from Translation.bf2Translator import BF2Translator
import os

# path = os.path.realpath(__file__)
# dir = os.path.dirname(path)
# dir = dir.replace("brainfuck2_logic", "resources")

# os.chdir(dir)





def main():
    layout = [
        [
            sg.Text("Translate your Brainfuck2 code to C!")
        ],
        [
            sg.Text("Choose a file"),
            sg.In(enable_events=True, key="-INPUT-"),
            sg.FileBrowse(),
        ],
        [
            sg.Text("Output File:"),
            sg.In(enable_events=True, key="-OUTPUT-"),
        ],
        [
            sg.Button("Submit", key="-SUBMIT-")
        ]
    ]

    window = sg.Window("Bf2C", layout)
    while True:
        event, values = window.read()

        if event == "-SUBMIT-":
            if values["-INPUT-"] == "":
                sg.popup("Invalid input file")
            elif values["-OUTPUT-"] == "":
                sg.popup("Invalid output file")
            else:
                tr = BF2Translator(values["-INPUT-"], values["-OUTPUT-"])
                tr.translate()
                sg.popup(f"File {values['-OUTPUT-']} succesfully created")
                

        if event == "Exit" or event == sg.WIN_CLOSED:
            break
    window.close()

main()
