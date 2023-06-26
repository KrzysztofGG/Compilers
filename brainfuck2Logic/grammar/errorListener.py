from antlr4.error.ErrorListener import ErrorListener

class ThrowingErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise Exception("Syntax error at line {0} column {1}: {2}".format(line, column, msg))
        # return super().syntaxError(recognizer, offendingSymbol, line, column, msg, e)