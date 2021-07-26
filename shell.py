#https://youtu.be/Eythq9848Fg
import chico

"""
file = open("notice.txt")
lines = file.readlines()
print('\n')
for line in lines:
    print(line,end='')
print('\n')
"""


while True:
    text = input('Chico > ')
    result, error = chico.run('<stdin>',text)

    if error: print(error.as_string())
    else: print(result)


