# Chico
# Matthew Rieckenberg
# Summer 2021


# NUM at the end of the file doesn't work for some reason
# Why can't expressions be printed? Try video 3


from sys import *
tokensList = []

def open_file(filename):
    data = open(filename,"r").read()
    #print(data)
    data += "\n" # append newline to the end of the file
    return data

def lex(fileContents):
    # Variables at default
    token = ""
    state = 0
    string = ""
    expression = ""
    number = ""
    isExpression = False
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
        elif token == "\n":
            if expression != "" and isExpression is True:
                tokensList.append("EXPR:"+expression)
                expression = ""
            elif expression != "" and isExpression is False:
                tokensList.append("NUM:"+expression)
                expression = ""
            token = ""
        elif token == "print" or token == "write":
            tokensList.append("PRINT")
            token = ""
        elif token == "0" or token == "1" or token == "3" or token == "4" or token == "5" or token == "6" or token == "7" or token == "8" or token == "9":
            expression += token
            token = ""
        elif token == "+":
            isExpression = True
            expression += token
            token = ""
        elif token == "\"":
            if state == 0:
                state = 1
            elif state == 1: # assume every letter is part of a string
                tokensList.append("STRING"+string+"\"")
                string = ""
                state = 0
                token = ""
        elif state == 1:
            string += token
            token = ""
    print(tokensList) # for debugging
    return tokensList

def parse(toks):
    i = 0
    while (i < len(toks)):
        if toks[i]+" "+toks[i+1][0:6] == "PRINT STRING" or toks[i]+" "+toks[i+1][0:3] == "PRINT NUM" or toks[i]+" "+toks[i+1][0:4] == "PRINT EXPR":
            # indexes may be wrong; experiment with this
            if toks[i+1][0:6] == "STRING":
                print(toks[i+1][6:])
            elif toks[i+1][0:3] == "NUM":
                print(toks[i+1][4:])
            elif toks[i+1][0:4] == "EXPR":
                print(toks[i+1][5:])
            i += 2


def run():
    fileData = open_file(argv[1]) # set to main.ch
    toks = lex(fileData)
    parse(toks)




# Calls
run()
