class TokenType:
     def __init__(self, name):
         self.name = name
     def __str__(self):
         return self.name

class Token:
    def __init__(self, _type,literal):
        self.type = TokenType(_type)
        self.literal = literal

        