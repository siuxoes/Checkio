__author__ = 'Siuxoes'

def checkio(numbers_array):
    n_array = sorted(numbers_array, key=abs)
    return n_array

print(checkio((-20, -5, 10, 15)))

