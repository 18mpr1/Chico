# Chico
# Matthew Rieckenberg
# Summer 2021

from sys import *

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
            token = "" # allows for whitespace
        elif token == "print":
            print("**Found a print**")
            token = ""
        elif token == "\"":
            if state == 0:
                state = 1
            elif state == 1: # assume every letter is part of a string
                print("**Found a string**")
                string = ""
                state = 0
        elif state == 1:
            string += char
            token = ""


def run():
    fileData = open_file(argv[1]) # set to main.ch
    lex(fileData)




# Calls
run()