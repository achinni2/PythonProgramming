from interface import implements, Interface
import token
import constants

class Node(Interface):
    def token_literal(self):
        pass

class Statement(Interface):
    def __init__(self,node):
        self.node = node
    def statement_node(self):
        pass

class Expression(Interface):
    def __init__(self,node):
        self.node = node
    def expression_node(self):
        pass            

class Program(implements(Node)):
    def __init__(self,statements):
        self.statements = statements
    
    def token_literal(self):
        if len(self.statements) > 0:
            return self.statements[0].token_literal()
        else:
            return ''

class LetStatement(implements(Node,Statement)):
    def __init__(self,token,name,value):
        self.token = token # the token.LET token
        self.name = name
        self.value = value            
    
    def statement_node(self):
        pass

    def token_literal(self):
        return self.token.literal  


class Identifier(implements(Node,Expression)):
    def __init__(self,token,value):
        self.token = token
        self.value = value

    def expression_node(self):
        pass

    def token_literal(self):
        return self.token.literal

class Parser:
    def __init__(self, lexer, curToken, peekToken):
        self.lexer = lexer
        self.curToken = curToken
        self.peekToken = peekToken  

    def new(self,lexer):
        self.lexer = lexer
        self.next_token
        self.next_token
        return self
    
    def next_token(self):
        self.curToken = self.peekToken
        self.peekToken = self.lexer.next_token()

    def parse_program(self):
        statements = Statement[]
        program = Program(statements)
        while self.curToken.type != constants.EOF:
            stmt = self.parse_statement()
            if stmt != None:
                statements.append(stmt)

        




     



