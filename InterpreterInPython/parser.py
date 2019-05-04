import constants
import token
import ast
from interface import implements, Interface
class Parser:
    def __init__(self, lexer, curToken, peekToken):
        self.lexer = lexer
        self.curToken = curToken
        self.peekToken = peekToken    

    def new(self,lexer):
        self.lexer = lexer
        self.next_token()
        self.next_token()
        return self

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
        }   
        return switcher.get(self.curToken.type.name,None) 

    def parse_let_statement(self):
        curTok = self.curToken
        stmt = ast.LetStatement(curTok,curTok.type.name,curTok.literal)
        if not self.expect_peek(token.TokenType(constants.IDENT)):
            return None
        stmt.name = ast.Identifier(self.curToken,self.curToken.literal)
        if not self.expect_peek(token.TokenType(constants.ASSIGN)):
            return None
        while not self.curToken(token.TokenType(constants.SEMICOLON)):
            self.next_token()
        return stmt    

    def cur_token_is(self,tokenType):
        return self.curToken.type == tokenType

    def peek_token_is(self,tokenType):
        return self.peekToken.type == tokenType

    def expect_peek(self,tokenType):
        if self.peek_token_is(tokenType):
            self.next_token()
            return True
        else:  
            return False  





