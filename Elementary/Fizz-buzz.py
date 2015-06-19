__author__ = 'Siuxoes'

def checkio(number):
    if number % 3 == 0 and number % 5 == 0:
        return "Fizz Buzz"
    elif number % 5 == 0:
        return "Buzz"
    elif number % 3 == 0:
        return "Fizz"
    else:
        return str(number)

print(checkio(6)) # Fizz expected

array = [1, 3, 4, 5]
print(len(array))