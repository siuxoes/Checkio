__author__ = 'Siuxoes'

def checkio(*args):
    if args:
        minimo = min(args)
        maximo = max(args)
        return abs(minimo-maximo)
    else:
        return 0

print(checkio(1, 2, 3))
print(checkio(5, -5))
print(checkio())