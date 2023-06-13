from FileColoring.scanner import Scanner

class Coloring:
    sc = Scanner()

    prefix = "<!DOCTYPE html><html land=\"en\">\n<head>\n</head>\n<body>\n"
    sufix = "</body>\n</html>"

    colors = {"data_type": "navy", "keyword": "purple", "integer": "mediumspringgreen",
            "special": "cyan", "string": "chocolate", "right_bracket": "yellow",
            "left_bracket": "yellow", "operator": "white", "": "white", "ERROR": "red"}
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

    def create_html_line(self, tokens):
        line = "<div style=\"font-size: 0;\">\n"
        for token_name, token_value in tokens:
            if token_name == "":
                token_value = "&nbsp" * len(token_value)
            line += f"\t<span style=\"font-size: 20px; color: {self.colors[token_name]}\">{token_value}</span>\n"
        return line

    def create_html(self):
        with open(self.input_file, 'r') as f:
            lines = f.readlines()

        with open(self.output_file, "w") as f:
            f.write(self.prefix)
            for l in lines:
                tokens = self.sc.scan_line(l)
                f.write(self.create_html_line(tokens))
            f.write(self.sufix)
            f.close()



