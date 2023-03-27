import re

class Scanner:

    operators = {'+', '-', '*', '/', '=', '<', '>', ';', '.'}
    data_type = {'int', 'double', 'float', 'char', 'string'}
    keywords = {'for', 'if', 'elif'}
    right_brackets = {'(', '[', '{'}
    left_brackets = {')', ']', '}'}

    def check_type(self, char):
        token_name = ""
        if char in self.operators:
            token_name = "operator"
        elif char.isspace():
            token_name == "space"
        elif char in self.left_brackets:
            token_name = "left_bracket"
        elif char in self.right_brackets:
            token_name = "right_bracket"
        elif char =='\"' or char == '\'': 
            token_name = "string"
        elif char.isdigit():
            token_name = "integer"
        elif char.isalpha():
            token_name = "special"

        else:
            token_name = "ERROR"
        
        return token_name

    def error_message(self, char, index):
        error_message = f'Invalid symbol: {char} at index: {index}'
        print(error_message)

    def handle_idf_name(self, str):
        new_token_name = ""
        if str in self.keywords:
            new_token_name = "keyword"
        elif str in self.data_type:
            new_token_name = "data_type"
        else:
            new_token_name = "special"

        return new_token_name


    def scan_line(self, str):
        tokens = []

        whitespace = re.compile(r"\s")
        token_name = self.check_type(str[0])
        token = ""
        reading_string = False

        for i, char in enumerate(str):#enumerate(whitespace.sub("", str)):
            new_token_name = self.check_type(char)
                
            if new_token_name == "string":
                reading_string = not reading_string
                token_name = new_token_name

            if new_token_name != token_name and not reading_string:
                if new_token_name == "ERROR":
                    self.error_message(char, i)
                else:
                    if token_name == "special":
                        token_name = self.handle_idf_name(token)
                    tokens.append((token_name, token))
                    token_name = new_token_name
                    token = ""
            token += char

        if len(token) > 0:
            if token_name == "special":
                token_name = self.handle_idf_name(token)
            tokens.append((token_name, token))

        return tokens    
