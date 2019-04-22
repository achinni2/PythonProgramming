import token
import constants
class Lexer():
   
    def __init__(self,input,ch,readPosition,position):
        self.input = input
        self.ch = ch
        self.position = position
        self.readPosition = readPosition

      
    def read_char(self):
        if self.readPosition >= len(self.input):
            self.ch = ''
        else:
            self.ch = self.input[self.readPosition] 
            self.postion = self.readPosition
            self.readPosition += 1

    def peek_char(self):
        if self.readPosition >= len(self.input):
            return ''
        else:
            return self.input[self.readPosition]    

    def new(self,input):
        self.input = input
        self.read_char()
        return self

    def next_token(self):
        self.skip_white_space()
        switcher = {
            ';': token.Token(constants.SEMICOLON,self.ch),
            '(': token.Token(constants.LPAREN,self.ch),
            ')': token.Token(constants.RPAREN,self.ch),
            ',': token.Token(constants.COMMA,self.ch),
            '{': token.Token(constants.LBRACE,self.ch),
            '}': token.Token(constants.RBRACE,self.ch),
            '+': token.Token(constants.PLUS,self.ch),
            '-': token.Token(constants.MINUS,self.ch),
            '/': token.Token(constants.SLASH,self.ch),
            '*': token.Token(constants.ASTERISK,self.ch),
            '<': token.Token(constants.LT,self.ch),
            '>': token.Token(constants.GT,self.ch),
            '' : token.Token(constants.EOF,self.ch)
            }     
        if self.ch not in switcher.keys():
            return self.next_element()
        tok = switcher.get(self.ch)
        self.read_char()
        return tok



    def next_element(self):
        if self.is_letter():
            ident = self.read_identifier()
            keyword = token.look_up_indent(ident)
            return token.Token(keyword,ident)  
        elif self.is_number():
            ident = self.read_number()
            keyword = constants.INT
            return token.Token(keyword,ident)
        elif self.ch == '!':
            if self.peek_char() == '=':
               char = self.read_char()
               tok = str(char)+str(self.ch)
               self.read_char()
               return token.Token(constants.NOT_EQ,tok)
            else:
               self.read_char() 
               return token.Token(constants.BANG,self.ch)   
        elif self.ch == '=':
            if self.peek_char() == '=':
                char = self.read_char()
                tok = str(char)+str(self.ch)
                self.read_char()
                return token.Token(constants.EQ,str(char)+str(self.ch))
            else:
                self.read_char()
                return token.Token(constants.ASSIGN,self.ch)    
        else:
            return token.Token(constants.ILLEGAL,self.ch)


    def read_identifier(self):
        pos = self.position
        while self.is_letter():
             self.read_char()
        return self.input[pos:self.postion] 

    def read_number(self):
        pos = self.position
        while self.is_number():
            self.read_char()
        return self.input[pos:self.position]      

    def is_number(self):
        return '0' <= self.ch and self.ch <= '9'     

    def is_letter(self):
        return 'a' <= self.ch and self.ch <= 'z' or 'A' <= self.ch and self.ch <= 'Z' or self.ch == '_' 


    def skip_white_space(self):
        while self.ch == ' ' or self.ch == '\t' or self.ch == '\n' or self.ch == '\r':
              self.read_char()
