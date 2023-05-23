class BF2Scanner:
    basic_operators = {'+', '-', '>', '<', '.', ',', '[', ']'}
    operator_dict = {'+': "add",
             '-': "sub",
             '>': "right",
             '<': "left",
             ',': "read",
             '.': "write",
             '[': "begin_while_loop",
             ']': "end_while_loop"}
    
    complex_operators = {'*', '/'}
    complex_operators_dict = {'*': "multi",
                            '/': "div"}
    brackets = {'(', ')'}
    
    def check_type(self, char):
        token_name = ""
        if char in self.basic_operators:
            token_name = self.operator_dict[char]
        elif char in self.complex_operators:
            token_name = self.complex_operators_dict[char]
        elif char in self.brackets:
            token_name = "bracket"
        elif char == '{':
            token_name = "left_brace"
        elif char == '}':
            token_name = "right_brace"
        elif char == '&':
            token_name = "for_loop"
        elif char == '?':
            token_name = "if"
        elif char == '|':
            token_name = "elif"
        elif char == ':':
            token_name = "else"
        elif char.isdigit():
            token_name = "number"
        else:
            token_name = "skippable"
        
        return token_name

    def scan(self, str):
        tokens = []

        token_name = self.check_type(str[0])
        token = ""
        for char in str:
            new_token_name = self.check_type(char)

            if new_token_name in self.operator_dict.values() or new_token_name in self.complex_operators_dict.values():
                tokens.append((token_name, token))
                token_name = new_token_name
                token = ""
            else:
                if new_token_name != token_name:
                    tokens.append((token_name, token))
                    token_name = new_token_name
                    token = ""
            token += char

        if len(token) > 0:
            tokens.append((token_name, token))

        return tokens 
    
# sc = BF2Scanner()
# print(sc.scan(">+++[+]-(5).<?(3){++--}|(2){+-}:{+}&(7){+-.}*(2)"))



        
            






