# Gramatyka

### Zbiór symboli nieterminalnych:

| Symbol Nieterminalny terminal symbol |
| --- |
| `<init>` |
| `<program>` |
| `<instruction>` |
| `<pointerOperation>` |
| `<valueOperation>` |
| `<readOperation>` |
| `<writeOperation>` |
| `<loop>` | 

There are a total of 8 non-terminal symbols in the Brainfuck grammar.

### Produkcja:
| Non-terminal symbol | Production rule |
| --- | --- |
| `<init>` | `<program>` |
| `<program>` | `<instruction>` <br> \| `<instruction>` `<program>` |
| `<instruction>` | `<pointerOperation>` <br> \| `<valueOperation>` <br> \| `<readOperation>` <br> \| `<writeOperation>` <br> \| `<loop>` |
| `<pointerOperation>` | ">" <br> \| "<" |
| `<valueOperation>` | "+" <br> \| "-" |
| `<readOperation>` | "," |
| `<writeOperation>` | "." |
| `<loop>` | "[" `<instruction>` "]" |
