# Chico
# Matthew Rieckenberg
# Summer 2021

from sys import *
tokensList = []
numberStack = []
symbols = {}

def open_file(filename):
    data = open(filename,"r").read()
    #print(data)
    data += "\n"
    return data

def lex(fileContents):
    # Variables
    token = ""
    state = 0
    string = ""
    expression = ""
    number = ""
    isExpression = False # boolean default 0
    fileContents = list(fileContents)
    variableStarted = False
    variable = ""
    for char in fileContents:
        token += char
        if token == " ":
            if state == 0:
                token = "" # allows for whitespace
            else:
                token = " "
        elif token == "\n":
            if expression != "" and isExpression is True:
                tokensList.append("EXPR:"+expression)
                expression = ""
                isExpression = False

            elif expression != "" and isExpression is False:
                tokensList.append("NUM:"+expression)
                expression = ""
            token = ""
        elif token == "=" and state == 0:
            if variable != "":
                tokensList.append("VAR:"+variable)
                variable = ""
                variableStarted = False
            tokensList.append("EQUALS")
            token = ""
        elif token == "let" and state == 0:
            variableStarted = True
            variable += token
            token = ""
        elif variableStarted is True:
            variable += token
            token = ""
        elif token == "print" or token == "write":
            tokensList.append("PRINT")
            token = ""
        elif token == "0" or token == "1" or token == "2" or token == "3" or token == "4" or token == "5" or token == "6" or token == "7" or token == "8" or token == "9":
            expression += token
            token = ""
        elif token == "+" or token == "-" or token == "*" or token == "/" or token == "(" or token == ")": # math operators
            isExpression = True
            expression += token
            token = ""

        elif token == "\"":
            if state == 0:
                state = 1
            elif state == 1: # assume every letter is part of a string
                tokensList.append("STRING:"+string+"\"")
                string = ""
                state = 0
                token = ""
        elif state == 1:
            string += token
            token = ""
    #print(tokensList)
    # return ""
    return tokensList


def evaluateExpression(thisExpression):
    # thisExpression = "," + thisExpression
    # i = len(thisExpression)-1
    # num = ""
    # while i >= 0:
    #     if thisExpression[i] == "+" or thisExpression[i] == "-" or thisExpression[i] == "*" or thisExpression[i] == "/" or thisExpression[i] == "%":
    #         num = num[::-1]
    #         numberStack.append(num)
    #         numberStack.append(thisExpression[i])
    #         num = ""
    #     elif thisExpression[i] == ",": # end of expression
    #         num = num[::-1]
    #         numberStack.append(num)
    #         num = ""
    #     else:
    #         # if it's a number
    #         num += thisExpression[i]
    #     i += -1
    # print(numberStack)
    return eval(thisExpression) # Python's built-in method for this


# def doPrint(toPrint): # optimized print function
#     if toPrint[0:6] == "STRING":
#         toPrint = toPrint[8:-1] # get rid of quotation marks
#         #toPrint = toPrint[:-1]
#     elif toPrint[0:3] == "NUM":
#         toPrint = toPrint[4:]
#     elif toPrint[0:4] == "EXPR":
#         toPrint = toPrint(toPrint[5:])
#     print(toPrint)
#     # print("toPrint")

def assignVariable(variableName,variableValue):
    symbols[variableName[7:]] = variableValue # omits the "let" part



def parse(toks):
    i = 0
    while (i < len(toks)):
        if toks[i]+" "+toks[i+1][0:6] == "PRINT STRING" or toks[i] + " " + toks[i+1][0:3] == "PRINT NUM" or toks[i] + " " + toks[i+1][0:4] == "PRINT EXPR":
            if toks[i+1][0:6] == "STRING":
                print(toks[i+1][8:-1])
            elif toks[i+1][0:3] == "NUM":
                print(toks[i+1][4:])
            elif toks[i+1][0:4] == "EXPR":
                print(evaluateExpression(toks[i+1][5:]))
            i += 2
        if toks[i][0:3] + " " + toks[i+1][0:6] + " "+toks[i+2][0:6] == "VAR EQUALS STRING":
            assignVariable(toks[i],toks[i+2])
            i += 3
    print(symbols)

def run():
    fileData = open_file(argv[1]) # set to main.ch
    toks = lex(fileData)
    parse(toks)


# Calls
run()