# Chico
# Matthew Rieckenberg
# Summer 2021

from sys import *
tokensList = []

def open_file(filename):
    data = open(filename,"r").read()
    #print(data)
    return data

def lex(fileContents):
    # Variables
    token = ""
    state = 0
    string = ""



    fileContents = list(fileContents)

    #print(fileContents)
    for char in fileContents:

        # variables
        token += char


        #print(token)
        if token == " ":
            if state == 0:
                token = "" # allows for whitespace
            else:
                token = " "
        elif token == "\n":
            token = ""
        elif token == "print":
            #print("**Found a print**")
            tokensList.append("print")
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
    #print(tokensList)
    return tokensList

def parse(toks):
    i = 0
    while (i < len(toks)):
        if toks[i]+" "+toks[i+1][0:6] == "print STRING":
            print(toks[i+1][6:])
            i += 2


def run():
    fileData = open_file(argv[1]) # set to main.ch
    toks = lex(fileData)
    parse(toks)




# Calls
run()