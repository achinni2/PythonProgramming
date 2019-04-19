class Lexer:
    postion = 0
    readPosition = 0
    ch = ''
    def __init__(self,input):
        self.input = input
      
    def readChar(self):
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
