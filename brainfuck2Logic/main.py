import PySimpleGUI as sg
from FileColoring.coloring import Coloring
from antlr4 import *
from grammar.dist.bf2Lexer import bf2Lexer
from grammar.dist.bf2Parser import bf2Parser
from grammar.dist.bf2Visitor import bf2Visitor
from grammar.errorListener import ThrowingErrorListener
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
            sg.Text("Or"),
            sg.Button("File Coloring", key="-SWAP-")
        ]
    ]

    window = sg.Window("Brainfuck2GUI", layout)
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
    
    def translation_process():
        try:
            f = open(values["-INPUT-"], 'r')
            inputStream = InputStream(f.read())
            lexer = bf2Lexer(inputStream)
            lexer.removeErrorListener(lexer._listeners[0])
            lexer.addErrorListener(ThrowingErrorListener())

            stream = CommonTokenStream(lexer)
            parser = bf2Parser(stream)
            parser.removeErrorListener(parser._listeners[0])
            parser.addErrorListener(ThrowingErrorListener())

            context = parser.program()
            visitor = bf2Visitor()
            visitor.visit(context)
            visitor.generateFile(values["-OUTPUT-"])
            sg.popup(f"File {values['-OUTPUT-']} succesfully created", title="Success")
        except Exception as e:
            print(e)
            sg.popup(e, title="Error")

        

    def handle_translation():
        if values["-OUTPUT-"][-1] != 'c':
            sg.popup("Output file has to be .c", title="Error")
        else:
            # tr = BF2Translator(values["-INPUT-"], values["-OUTPUT-"])
            # tr.translate()
            translation_process()
            
    
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
            if not values["-INPUT-"]  or not os.path.exists(values["-INPUT-"]):
                sg.popup("Invalid input file", title="Error")
            elif values["-OUTPUT-"] == "":
                sg.popup("Invalid output file", title="Error")
            else:
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
