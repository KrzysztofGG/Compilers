from bf2Scanner import BF2Scanner

class BF2Translator:

    sc = BF2Scanner()
    # basic_operators = {'+', '-', '>', '<', '.', ',', '[', ']'}
    skippable = {'{', '}', '(', ')'}

    match = {'+': "++*ptr;\n",
             '-': "--*ptr;\n",
             '>': "++ptr;\n",
             '<': "--ptr;\n",
             ',': "*ptr=getchar();\n",
             '.': "putchar(*ptr);\n",
             '[': "while (*ptr){\n",
             ']': "}\n"}

    prefix = "#include \"stdio.h\"\n\nint main(){\n\tchar tape[20000] = {0};\n\tchar *ptr = tape;\n"

    indent = 1

    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file
        with open(self.input_file, 'r') as f:
            self.tokens = self.sc.scan(f.read())
    
    def translate(self):

        with open(self.output_file, 'w') as f:
            f.write(self.prefix)

        for i, (token_name, token_value) in enumerate(self.tokens):
            if token_value in self.sc.brackets or token_name == "skippable" or token_name == "number":
                continue
            
            if token_value in self.sc.basic_operators:
                self.handle_basic_operation(token_value, i)
            elif token_value in self.sc.complex_operators:
                self.handle_complex_operation(token_value, i)
            elif token_value in ('?', '|', ':'):
                self.handle_decisive_block(token_value, i)
            elif token_value in ('{', '}'):
                self.handle_braces(token_value)
            elif token_value == '&':
                self.handle_for_loop(i)
        
        self.write_to_file("}\n")


    def handle_basic_operation(self, token, index):

        if token == ']':
            self.indent -= 1

        output = "\t"*self.indent
        if index < len(self.tokens) - 4 and self.tokens[index + 1][1] == '(':
            output += "for(int i=0; i<{num}; ++i)".format(num=self.tokens[index + 2][1]) + "{\n"
            output += "\t"*(self.indent + 1) + self.match[token]
            output += "\t"*self.indent + '}\n'
        else:
            if token == '[':
                self.indent += 1
            output += self.match[token]
        self.write_to_file(output)
    

    def handle_complex_operation(self, token_value, index):

        output = "\t"*self.indent
        if token_value == '*':
            output += "*ptr *= {num};".format(num=self.tokens[index + 2][1])
        elif token_value == '/':
            output += "*ptr /= {num};".format(num=self.tokens[index + 2][1])
        output += "\n"

        self.write_to_file(output)
    

    def handle_decisive_block(self, token_value, index):

        output = "\t"*self.indent
        if token_value == '?':
            output += "if(*ptr == {num})".format(num=self.tokens[index + 2][1])
        elif token_value == '|':
            output += "else if(*ptr == {num})".format(num=self.tokens[index + 2][1])
        elif token_value == ':':
            output += "else"
        
        self.write_to_file(output)
    
    def handle_braces(self, token_value):
        output = ""
        if token_value == '{':
            output += "{\n"
            self.indent += 1
        elif token_value == '}':
            self.indent -= 1 
            output += "\t"*self.indent + "}\n"
        self.write_to_file(output)
    
    def handle_for_loop(self, index):

        output = "\t"*self.indent 
        output += "for(int i=0; i<{num}; ++i)".format(num=self.tokens[index + 2][1])

        self.write_to_file(output)
    def write_to_file(self, data):
        with open(self.output_file, 'a') as f:
            f.write(data)