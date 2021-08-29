# Chico
# Matthew Rieckenberg
# Summer 2021

# https://youtube.com/playlist?list=PLZQftyCk7_SdoVexSmwy_tBgs7P0b97yD

############################################################################################################################################################
# Constants
############################################################################################################################################################

DIGITS = '0123456789'


############################################################################################################################################################
# Errors
############################################################################################################################################################

class Error:
    def __init__(self, positionStart, positionEnd, errorName, details):
        self.positionStart = positionStart
        self.positionEnd = positionEnd
        self.errorName = errorName
        self.details = details

    def as_string(self):
        result = f'{self.errorName}: {self.details}\n'
        result += f'File {self.positionStart.fileName}, line {self.positionStart.line + 1}'
        return result


class IllegalCharError(Error):
    def __init__(self, positionStart, positionEnd, details):
        super().__init__(positionStart, positionEnd, 'Illegal Character', details)


############################################################################################################################################################
# Position
############################################################################################################################################################

class Position:
    def __init__(self, index, line, column, fileName, fileText):
        self.index = index
        self.line = line
        self.column = column
        self.fileName = fileName
        self.fileText = fileText

    def advance(self, currentChar):
        self.index += 1
        self.column += 1

        if currentChar == '\n':
            self.line += 1
            self.column = 0

        return self

    def copy(self):
        return Position(self.index, self.line, self.column, self.fileName, self.fileText)


############################################################################################################################################################
# Tokens - tokens will use all caps
############################################################################################################################################################

TT_INT = 'INT'
TT_FLOAT = 'FLOAT'
TT_PLUS = 'PLUS'
TT_MINUS = 'MINUS'
TT_MUL = 'MUL'
TT_DIV = 'DIV'
TT_LPAREN = 'LPAREN'
TT_RPAREN = 'RPAREN'


class Token:
    def __init__(self, type, value=None):
        self.type = type
        self.value = value

    def __repr__(self):
        if self.value: return f'{self.type}:{self.value}'
        return f'{self.type}'


############################################################################################################################################################
# Lexer
############################################################################################################################################################

class Lexer:
    def __init__(self, fn, text):
        self.fn = fn
        self.text = text
        self.position = Position(-1, 0, -1, fn, text)
        self.currentChar = None
        self.advance()

    def advance(self):
        self.position.advance(self.currentChar)
        self.currentChar = self.text[self.position.index] if self.position.index < len(self.text) else None

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
                pos_start = self.position.copy()
                char = self.currentChar
                self.advance()
                return [], IllegalCharError(pos_start, self.position, "'" + char + "'")

        return tokens, None

    def makeNumber(self):
        numberString = ''
        dotCount = 0

        while self.currentChar != None and self.currentChar in DIGITS + '.':
            if self.currentChar == '.':
                if dotCount == 1:
                    break
                dotCount += 1
                numberString += '.'
            else:
                numberString += self.currentChar
            self.advance()

        if dotCount == 0:
            return Token(TT_INT, int(numberString))
        else:
            return Token(TT_FLOAT, float(numberString))


############################################################################################################################################################
# Run
############################################################################################################################################################

def run(fn, text):
    lexer = Lexer(fn, text)
    tokens, error = lexer.makeTokens()

    return tokens, error