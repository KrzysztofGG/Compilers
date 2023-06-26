grammar bf2;

program
    : instruction | program instruction 
    ;
    
instruction
    :  pointerOperation  | valueOperation  | readOperation  | writeOperation  | loop | decisiveBlock 
    ;
valueOperation
    : addSubOperation | multiDivOperation
    ;
    
addSubOperation
    : finalValueOperation | finalValueOperation numberSpecifier
    ;

multiDivOperation
    : finalValueOperation numberSpecifier
    ;

pointerOperation
    : finalPointerOperation | finalPointerOperation numberSpecifier
    ;

loop
    : whileLoop | forLoop
    ;

whileLoop
    : '[' program ']'
    ;

forLoop
    : '&' numberSpecifier block
    ;

block
    : '{' program '}'
    ;

decisiveBlock
    : '?' numberSpecifier block elifBlock* elseBlock*
    ;

elifBlock
    : '|' numberSpecifier block elifBlock*
    ;

elseBlock
    : ':' block
    ;
    
numberSpecifier
    : '(' PositiveNumber ')'
    ;

PositiveNumber
    : [1-9]+
    ;

finalValueOperation
    : '+' | '-' | '*' | '/'
    ;

finalPointerOperation
    : '>' | '<'
    ;
    
readOperation
    : ','
    ;

writeOperation
   : '.'
    ;

WS: [ \t\r\n]+ -> skip;

