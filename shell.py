import chico

while True:
    text = input('Chico > ')
    result, error = chico.run('<stdin>', text)

    if error: print(error.as_string())
    else: print(result)