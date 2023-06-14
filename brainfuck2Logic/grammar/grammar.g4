grammar bf2;

program
    : instruction | instruction program
    ;
    

INSTRUCTION
    :  pointerOperation  | valueOperation  | readOperation  | writeOperation  | loop | decisiveBlock | 
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
    : "[" program "]"
    ;

forLoop
    : "&" numberSpecifier block
    ;

block
    : "{" program "}"
    ;

decisiveBlock
    : "?" numberSpecifier block elifBlock* elseBlock*
    ;

elifBlock
    : "|" numberSpecifier block elifBlock*
    ;

elseBlock
    : ":" block
    ;
    
numberSpecifier
    ; "(" positiveNumber ")"
    ;

positiveNumber
    : [1-9]+
    ;

finalValueOperation
    : "+" | "-" | "*" | "/"
    ;

finalPointerOperation
    : ">" | "<"
    ;
    
readOperation
    : ","
    ;

writeOperation
   : 
    "."
    ;
