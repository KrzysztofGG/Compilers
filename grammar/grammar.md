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


### Lista Produkcji:
| Symbol Nieterminaly | Produkcja |
| --- | --- |
| `<init>` | `<program>` |
| `<program>` | `<instruction>` \| `<instruction>` `<program>` |
| `<instruction>` | `<pointerOperation>`  \| `<valueOperation>`  \| `<readOperation>`  \| `<writeOperation>`  \| `<loop>` |
| `<pointerOperation>` | ">"  \| "<" |
| `<valueOperation>` | "+"  \| "-" |
| `<readOperation>` | "," |
| `<writeOperation>` | "." |
| `<loop>` | "[" `<program>` "]" |
