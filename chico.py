# Chico
# Matthew Rieckenberg
# Summer 2021

from sys import *
tokensList = []

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
    isExpression = 0 # boolean default 0
    fileContents = list(fileContents)
    for char in fileContents:
        token += char
        if token == " ":
            if state == 0:
                token = "" # allows for whitespace
            else:
                token = " "
        elif token == "\n":
            if expression != "" and isExpression == 1:

                tokensList.append("EXPR:"+expression)
                expression = ""
                isExpression = 0

            elif expression != "" and isExpression == 0:
                tokensList.append("NUM:"+expression)
                expression = ""
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
                #print("**Found a string**")
                tokensList.append("STRING:"+string+"\"")
                string = ""
                state = 0
                token = ""
        elif state == 1:
            string += token
            token = ""
    print(tokensList)
    return tokensList

def doPrint(toPrint): # optimized print function
    if toPrint[0:6] == "STRING":
        toPrint = toPrint[8:] # get rid of quotation marks
        toPrint = toPrint[:-1]
    elif toPrint[0:3] == "NUM":
        toPrint = toPrint[4:]
    elif toPrint[0:4] == "EXPR":
        toPrint = toPrint[5:]
    print(toPrint)


def parse(toks):
    i = 0
    while (i < len(toks)):
        if toks[i]+" "+toks[i+1][0:6] == "PRINT STRING" or toks[i] + " " + toks[i+1][0:3] == "PRINT NUM" or toks[i] + " " + toks[i+1][0:4] == "PRINT EXPR":
            if toks[i+1][0:6] == "STRING":
                doPrint(toks[i+1][8:-1])
            elif toks[i+1][0:3] == "NUM":
                doPrint(toks[i+1][4:])
            elif toks[i+1][0:4] == "EXPR":
                doPrint(toks[i+1][5:])
            i += 2


def run():
    fileData = open_file(argv[1]) # set to main.ch
    toks = lex(fileData)
    parse(toks)


# Calls
run()