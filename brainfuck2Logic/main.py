import PySimpleGUI as sg
from Translation.bf2Translator import BF2Translator
from FileColoring.coloring import Coloring
import os


def main():
    
    layout = [
        [
            sg.Text("Translate your Brainfuck2 code to C!", key="-INTRO-")
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
            sg.FileSaveAs(enable_events=True, size=(8, 1)),
        ],
        [
            sg.Button("Submit", key="-SUBMIT-", size=(8, 1)),
            sg.VSeparator(),
            sg.Button("File Coloring", key="-SWAP-")
        ]
    ]
    window = sg.Window("Bf2C", layout)
    is_coloring = False    

    def edit_window( is_coloring):
        if is_coloring:
            window["-INTRO-"].update("Translate your Brainfuck2 code to C!")
            window["-SWAP-"].update("File Coloring")
            is_coloring = False
        else:
            window["-INTRO-"].update("Get a colored HTML from your file!")
            window["-SWAP-"].update("Translate BF2")
            is_coloring = True

        return is_coloring

    def handle_translation():
        if values["-OUTPUT-"][-1] != 'c':
            sg.popup("Output file has to be .c", title="Error")
        else:
            tr = BF2Translator(values["-INPUT-"], values["-OUTPUT-"])
            tr.translate()
            sg.popup(f"File {values['-OUTPUT-']} succesfully created", title="Success")
    
    def handle_coloring():
        if not values["-OUTPUT-"].endswith("html"):
            sg.popup("Output file has to be .html", title="Error")
        else:
            cl = Coloring(values["-INPUT-"], values["-OUTPUT-"])
            cl.create_html()
            sg.popup(f"File {values['-OUTPUT-']} succesfully created", title="Success")

    while True:
        event, values = window.read()
        if event == "-SWAP-":
            # button_text = window["-SWAP-"].get_text()
            is_coloring = edit_window(is_coloring)
            
        if event == "-SUBMIT-":
            if values["-INPUT-"] == "" or not os.path.exists(values["-INPUT-"]):
                sg.popup("Invalid input file", title="Error")
            elif values["-OUTPUT-"] == "":
                sg.popup("Invalid output file", title="Error")

            if is_coloring:
                handle_coloring()
            else:
                handle_translation()
            window["-INPUT-"].update('')
            window["-OUTPUT-"].update('')
            
                

        if event == "Exit" or event == sg.WIN_CLOSED:
            break
    window.close()

main()
