from interface import implements, Interface
import token

class Node(Interface):
    def token_literal(self):
        pass
    def to_string(self):
        pass

class Statement(Interface):
    def __init__(self,node):
        self.node = node
    def statement_node(self):
        pass

class Expression(Interface):
    def __init__(self,Node: node):
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

    def to_string(self):
        out = bytearray()
        for stmt in self.statements:
            out.extend(stmt.to_string())
        return str(out)    


class LetStatement(implements(Node,Statement)):
    def __init__(self,token,name=None,value=None):
        self.token = token # the token.LET token
        self.name = name
        self.value = value            
    
    def statement_node(self):
        pass

    def token_literal(self):
        return self.token.literal  

    def to_string(self):
        out = bytearray()
        out.extend(self.token_literal + ' ')    
        out.extend(self.name.to_string())
        out.extend(' = ')
        if not self.value is None:
            out.extend(self.value.to_string())
        out.extend(' ; ')    
        return str(out)

class ReturnStatement(implements(Node,Statement)):
    def __init__(self,token,value=None):
        self.token = token # the token.RETURN token
        self.value = value            
    
    def statement_node(self):
        pass

    def token_literal(self):
        return self.token.literal  

    def to_string(self):
        out = bytearray()
        out.extend(self.token_literal + ' ')    
        if not self.value is None:
            out.extend(self.value.to_string())
        out.extend(' ; ')    
        return str(out)


class ExpressionStatement(implements(Node,Statement)):
    def __init__(self, token, expression=None):
        self.token = token # the first token of the expression
        self.expression = expression

    def statement_node(self):
        pass

    def token_literal(self):
        return self.token.literal  

    def to_string(self):
        if self.expression is not None:
            return self.expression.to_string()
        return ''      

class Identifier(implements(Node,Expression)):
    def __init__(self,token,value=None):
        self.token = token
        self.value = value

    def expression_node(self):
        pass

    def token_literal(self):
        return self.token.literal

    def to_string(self):
        return self.value  

class IntegerLiteral(implements(Node,Expression)):
    def __init__(self,token,value=None):
        self.token = token
        self.value = value

    def expression_node(self):
        pass

    def token_literal(self):
        return self.token.literal

    def to_string(self):
        return self.token.literal     
     



