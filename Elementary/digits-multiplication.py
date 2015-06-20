__author__ = 'Siuxoes'

def checkio(number):
    result = 1
    string = str(number)
    for x in string:
        if x == "0":
            x="1"
        result *= int(x)
    return result

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1