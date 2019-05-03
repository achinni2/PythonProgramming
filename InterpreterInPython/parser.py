import constants
import ast
import token
from interface import implements, Interface
class Parser:
    LOWEST = 'LOWEST'
    EQUALS = 'EQUALS' # == 
    LESSGREATER = 'LESSGREATER' # > or < 
    SUM = 'SUM' # + 
    PRODUCT = 'PRODUCT' # * 
    PREFIX = 'PREFIX' # -X or !X 
    CALL = 'CALL' 
    errors = []
    def __init__(self,lexer,curToken=None,peekToken=None,prefixParserFns=None,infixParserFns=None):
        self.lexer = lexer 

    def new(self,lexer):
        self.lexer = lexer
        self.register_prefix(token.TokenType(constants.IDENT),self.parse_identifier())
        self.register_prefix(token.TokenType(constants.INT),self.parse_integer_literal())
        self.next_token()
        self.next_token()
        return self

    def errors(self):
        return self.errors

    prefixParserFn = lambda: ast.Expression
    infixParserFn = lambda ast.Expression: ast.Expression    

    precedences = {
        LOWEST : 1
        EQUALS : 2
        LESSGREATER : 3
        SUM : 4
        PRODUCT : 5
        PREFIX : 6
        CALL : 7
    }

    def get_precedence(self,operator):
        return self.precedences.get(operator,0)

    def peek_error(self,tokenType):
        msg = 'expected next token to be {}, got {} instead'.format(tokenType,self.peekToken.type)
        errors.append(msg)

    def next_token(self):
        self.curToken = self.peekToken
        self.peekToken = self.lexer.next_token()

    def parse_program(self):
        statements = []
        program = ast.Program(statements)
        while not self.cur_token_is(token.TokenType(constants.EOF)):
            stmt = self.parse_statement()
            if stmt != None:
                program.statements.append(stmt)
            self.next_token()
        return program

    def parse_statement(self):
        switcher = {
            constants.LET: self.parse_let_statement()
            constants.RETURN: self.parse_return_statement()
        }   
        return switcher.get(self.curToken.type.name,self.parse_expression_statement()) 

    def parse_let_statement(self):
        curTok = self.curToken
        stmt = ast.LetStatement(curTok)
        if not self.expect_peek(token.TokenType(constants.IDENT)):
            return None
        stmt.name = ast.Identifier(self.curToken,self.curToken.literal)
        if not self.expect_peek(token.TokenType(constants.ASSIGN)):
            return None
        while not self.curToken(token.TokenType(constants.SEMICOLON)):
            self.next_token()
        return stmt    

    def parse_return_statement(self):
        stmt = ast.ReturnStatement(self.curToken)
        self.next_token()
        # TODO ..we are skipping expressions until we encounter semicolons
        while not self.cur_token_is(token.TokenType(constants.SEMICOLON)):
            self.next_token()
        return stmt    

    def parse_expression_statement(self):
        stmt = ast.ExpressionStatement(self.curToken)
        stmt.expression = self.parse_expression('LOWEST')
        if self.peek_token_is is token.TokenType(constants.SEMICOLON):
            self.next_token()
        return stmt   

    def parse_expression(self,precedence):
        prefix = self.prefixParserFns[self.curToken.type]
        if prefix is None:
            return None
        leftExp = prefix()
        return leftExp    

    def parse_identifier(self):
        return ast.Identifier(self.curToken,self.curToken.literal)  
        
    def parse_integer_literal(self):
        lit = ast.IntegerLiteral(self.curToken)
        try:
            value = int(self.curToken.literal)
            print('The value of the integer literal is {}'.format(value))
        except ValueError:
            self.errors.append('could not parse the {} literal'.format(self.curToken.literal))    
        lit.value = value
        return lit    


    def cur_token_is(self,tokenType):
        return self.curToken.type == tokenType

    def peek_token_is(self,tokenType):
        return self.peekToken.type == tokenType

    def expect_peek(self,tokenType):
        if self.peek_token_is(tokenType):
            self.next_token()
            return True
        else:
            self.peek_error(tokenType)
            return False  

    def register_prefix(self,tokenType,prefixParserFn):
        self.prefixParserFns[tokenType] = prefixParserFn

    def register_infix(self,tokenType,infixParserFn):
        self.infixParserFns[tokenType] = infixParserFn         
