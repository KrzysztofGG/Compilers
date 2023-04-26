# Gramatyka

### Zbiór symboli nieterminalnych:

| Symbol Nieterminalny |
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

### Lista Produkcji:
| Symbol Nieterminaly | Produkcja |
| --- | --- |
| `<init>` | `<program>` |
| `<program>` | `<instruction>` \| `<instruction>` `<program>` |
| `<instruction>` | `<pointerOperation>` <br> \| `<valueOperation>` <br> \| `<readOperation>` <br> \| `<writeOperation>` <br> \| `<loop>` |
| `<pointerOperation>` | ">" <br> \| "<" |
| `<valueOperation>` | "+" <br> \| "-" |
| `<readOperation>` | "," |
| `<writeOperation>` | "." |
| `<loop>` | "[" `<instruction>` "]" |
