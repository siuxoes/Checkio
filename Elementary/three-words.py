__author__ = 'Siuxoes'

def checkio(words):
    wordsSplited = words.split(" ")
    if len(wordsSplited) < 3:
        return False
    else:
        cont = 0
        for x in wordsSplited:
            if cont != 3:
                if x.isnumeric():
                    cont = 0
                else:
                    cont += 1
            if cont == 3:
                return True
    return False



texto = "Hola holita hola"
print(checkio(texto))