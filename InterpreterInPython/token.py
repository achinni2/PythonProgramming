class TokenType:
     def __init__(self, name):
         self.name = name
     def __str__(self):
         return self.name

class Token:
    def __init__(self, _type,literal):
        self.type = TokenType(_type)
        self.literal = literal

keywords = {
    "fn":     TokenType('FUNCTION'),
	"let":    TokenType('LET'),
	"true":   TokenType('TRUE'),
	"false":  TokenType('FALSE'),
	"if":     TokenType('IF'),
	"else":   TokenType('ELSE'),
	"return": TokenType('RETURN'),
    ",":      TokenType('COMMA')
}

def look_up_indent(indent):
    return keywords.get(indent,TokenType('IDENT'))

        
