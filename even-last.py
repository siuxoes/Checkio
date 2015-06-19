__author__ = 'Siuxoes'

def checkio(array):
    if len(array) == 0:
        return 0
    else:
        suma = sum(array[::2])
        total = suma * array[len(array)-1]
        return total

array = [1, 2, 3, 4]

print(checkio(array))