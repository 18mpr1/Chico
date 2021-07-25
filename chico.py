#####################################################################
# Constraints
#####################################################################

DIGITS = '0123456789'

#####################################################################
# Error
#####################################################################

class Error:
    def __init__(self,errorName,details):
        self.errorName = errorName
        self.details = details

    def asString(self):
        result = f'{self.errorName}:{" "+self.details}'
        return result

class IllegalCharError(Error):
    def __init__(self,details):
        super().__init__('Illegal character!', details)



#####################################################################
# Tokens
#####################################################################

TT_INT = 'TT_INT'
TT_FLOAT = 'FLOAT'
TT_PLUS = 'PLUS'
TT_MINUS = 'MINUS'
TT_MUL = 'MUL'
TT_DIV = 'DIV'
TT_LPAREN = 'LPAREN'
TT_RPAREN = 'RPAREN'


class Token:
    def __init__(self,type,value=None):
        self.type = type
        self.value = value

    def __repr__(self):
        if self.value:
            return f'{self.type}:{self.value}'
        return f'{self.type}'

#####################################################################
# Lexer
#####################################################################

class Lexer:
    def __init__(self,text):
        self.text = text
        self.pos = -1
        self.currentChar = None
        self.advance()

    def advance(self):
        self.pos += 1
        self.currentChar = self.text[self.pos] if self.pos < len(self.text) else None

    def makeTokens(self):
        tokens = []
        while self.currentChar != None:
            if self.currentChar in ' \t':
                self.advance()
            elif self.currentChar in DIGITS:
                tokens.append(self.makeNumber())
            elif self.currentChar == '+':
                tokens.append(Token(TT_PLUS))
                self.advance()
            elif self.currentChar == '-':
                tokens.append(Token(TT_MINUS))
                self.advance()
            elif self.currentChar == '*':
                tokens.append(Token(TT_MUL))
                self.advance()
            elif self.currentChar == '/':
                tokens.append(Token(TT_DIV))
                self.advance()
            elif self.currentChar == '(':
                tokens.append(Token(TT_LPAREN))
                self.advance()
            elif self.currentChar == ')':
                tokens.append(Token(TT_RPAREN))
                self.advance()
            else:
                char = self.currentChar
                self.advance()
                return [],IllegalCharError("'"+char+"'")

        return tokens, None

    def makeNumber(self):
        numStr = ''
        dotCount = 0

        while self.currentChar != None and self.currentChar in DIGITS + '.':
            if self.currentChar == '.':
                if dotCount == 1: break
                dotCount += 1
                numStr += '.'
            else:
                numStr += self.currentChar

        if dotCount == 0:
            return Token(TT_INT, int(numStr))
        else:
            return Token(TT_FLOAT, float(numStr))

#####################################################################
# Run
#####################################################################

def run(text):
    lexer = Lexer(text)
    tokens, error = lexer.makeTokens()
    return tokens, error