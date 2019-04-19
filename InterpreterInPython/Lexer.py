import token
import constants
class Lexer:
   
    def __init__(self,input,position,readPosition,ch):
        self.input = input
        self.postion = position
        self.readPosition = readPosition
        self.ch = ch
      
    def read_char(self):
        if self.readPosition >= len(self.input):
            self.ch = 0
        else:
            self.ch = self.input[self.readPosition] 
            self.postion = self.readPosition
            self.readPosition += 1
        return self

    def New(self,input):
        self.input = input
        self.readChar() 

    def next_token(self):
        self.skip_white_space
        switcher = {
            '=': token.Token(constants.ASSIGN,self.ch),
            ';': token.Token(constants.SEMICOLON,self.ch),
            '(': token.Token(constants.LPAREN,self.ch),
            ')': token.Token(constants.RPAREN,self.ch),
            ',': token.Token(constants.COMMA,self.ch),
            '+': token.Token(constants.PLUS,self.ch),
            '{': token.Token(constants.LBRACE,self.ch),
            '}': token.Token(constants.RBRACE,self.ch),
             0 : token.Token(constants.EOF,'')
            }    
        return switcher.get(self.ch,self.next_letter())


    def next_letter(self):
        if is_letter(self.ch):
            ident = self.read_identifier()
            keyword = token.look_up_indent(ident)
            return token.Token(keyword,ident)  
        else:
            return token.Token(constants.ILLEGAL,self.ch)


    def read_identifier(self):
        pos = self.position
        while is_letter(self.ch):
             self.read_char()
        return self.input[pos:self.postion] 

    def is_letter(ch):
        return 'a' <= ch and ch <= 'z' or 'A' <= ch and ch <= 'Z' or ch == '_' 


    def skip_white_space(self):
        while self.ch == ' ' or self.ch == '\t' or self.ch == '\n' or self.ch == '\r':
            self.read_char()

       
 
