ILLEGAL = "ILLEGAL"
EOF     = "EOF"

# Identifiers + literals
IDENT = "IDENT" 
INT   = "INT"  

# Operators
ASSIGN   = "="
PLUS     = "+"

# Delimiters
COMMA     = ","
SEMICOLON = ";"
LPAREN = "("
RPAREN = ")"
LBRACE = "{"
RBRACE = "}"
# Keywords
LET = "LET"
FUNCTION = "FUNCTION"

# end 



class TokenType:
     def __init__(self, name):
         self.name = name
     def __str__(self):
         return self.name

class Token:
    def __init__(self, _type,literal):
        self.type = TokenType(_type)
        self.literal = literal

        