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



     



