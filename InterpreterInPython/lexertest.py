import Lexer
input = 'let result = add(five, ten);'
lexer = Lexer.Lexer(input,'',0,0)
l = lexer.next_token()
m = lexer.next_token()
n = lexer.next_token()
print('Read the next token {} {}'.format(m.type.name,n.type.name))

