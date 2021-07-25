#https://youtu.be/Eythq9848Fg
import chico

while True:
    text = input('Chico > ')
    result, error = chico.run('<stdin>',text)

    if error: print(error.asString())
    else: print(result)


