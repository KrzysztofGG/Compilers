# Gramatyka
### Zbiór tokenów
|Token|Nazwa|
|---|---|
|+|ADD_1|
|-|MINUS_1|
|<|MOVE_LEFT|
|>|MOVE_RIGHT|
|,|EXTRACT|
|.|SHOW|
|\*|MULTIPLY|
|/|DIVIDE|
|[|WHILE_BEGIN|
|]|WHILE_END|
|&|FOR_LOOP|
|?|IF|
|\||ELIF|
|:|ELSE|
|(|LPAREN|
|)|RPAREN|
|{|LBRACKET|
|}|RBRACKET|
|[1-9]+|NUMBER|




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
| `<whileLoop>` |
| `<forLoop>` |
| `<decisiveBlock>` |
| `<addSubOperation>` |
| `<multiDivOperation>` |
| `<numberSpecifier>` |
| `<decisiveBlock>` |
| `<elifBlock>` |
| `<elseBlock>` |






### Lista Produkcji:
| Symbol Nieterminaly | Produkcja |
| --- | --- |
| `<init>` | `<program>` |
| `<program>` | `<instruction>` \| `<instruction>` `<program>` |
| `<instruction>` | `<pointerOperation>`  \| `<valueOperation>`  \| `<readOperation>`  \| `<writeOperation>`  \| `<loop>` \| `<decisiveBlock>` | 
| `<valueOperation>` | `<addSubOperation>` \| `<multiDivOperation>` |
| `<addSubOperation>` | `<finalValueOperation>` \| `<finalValueOperation>` `<numberSpecifier>` |
| `<multiDivOperation>` | `<finalValueOperation>` `<numberSpecifier>` |
| `<pointerOperation>` | `<finalPointerOperation>` \| `<finalPointerOperation> ` `<numberSpecifier>`|
| `<loop>` | `<whileLoop>` \| `<forLoop>` |
| `<whileLoop>` | "[" `<program>` "]" |
| `<forLoop>` | "&" `<numberSpecifier>` `<block>` |
| `<block>` | "{" `<program>` "}" | 
| `<decisiveBlock>` | "?" `<numberSpecifier>` `<block>` `<elifBlock>`* `<elseBlock>`* |
| `<elifBlock>` | "\|" `<numberSpecifier>` `<block>` `<elifBlock>`* |
| `<elseBlock>` | ":" `<block>` |
| `<numberSpecifier>` | "(" `<positiveNumber>` ")" |
<!-- | `<positiveNumber>` | \[1-9\]+ |
| `<finalValueOperation>` | "+" \| "-" \| "\*" \| "/" |
| `<finalPointerOperation>` | ">"  \| "<" |
| `<readOperation>` | "," |
| `<writeOperation>` | "." | -->
