import sys
import Lexer
import token
import constants
PROMPT = '>>'
class Repl:
   def start(self,input,output): 
        print(PROMPT)
        for line in input:
            l = Lexer.Lexer(line,'',0,0)
            tok = l.next_token()
            while tok.type.name != constants.EOF:
                print('token is {} {}'.format(tok.literal,tok.type.name))
                tok = l.next_token()


