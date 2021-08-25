# Chico
# Matthew Rieckenberg
# Summer 2021

# 6:52

from sys import *
tokensList = []

def open_file(filename):
    data = open(filename,"r").read()
    #print(data)
    data += "<EOF>"
    return data

def lex(fileContents):
    # Variables
    token = ""
    state = 0
    string = ""
    expression = ""
    number = ""
    isExpression = 0



    fileContents = list(fileContents)

    #print(fileContents)
    for char in fileContents:
        token += char
        #print(token)
        if token == " ":
            if state == 0:
                token = "" # allows for whitespace
            else:
                token = " "
        elif token == "\n" or token == "<EOF>":
            if expression != "":
                print(expression)
                expression = ""
            token = ""
        elif token == "print" or token == "write" or token == "printf":
            #print("**Found a print**")
            tokensList.append("PRINT")
            token = ""
        elif token == "0" or token == "1" or token == "3" or token == "4" or token == "5" or token == "6" or token == "7" or token == "8" or token == "9":
            expression += token
            token = ""
        elif token == "+":
            expression += token
            token = ""
            isExpression = 1

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
    #print(tokensList)
    #print(expression)
    return tokensList

def parse(toks):
    i = 0
    while (i < len(toks)):
        if toks[i]+" "+toks[i+1][0:6] == "PRINT STRING":
            print(toks[i+1][6:])
            i += 2


def run():
    fileData = open_file(argv[1]) # set to main.ch
    toks = lex(fileData)
    parse(toks)




# Calls
run()