__author__ = 'Siuxoes'

import statistics
def checkio2(data):
    return statistics.median(data)

def checkio(data):
    dataSorted = sorted(data)
    elementos = len(data)
    centro = 0
    if elementos % 2 != 0:
        centro = int((elementos/2)) + 1
        return dataSorted[centro-1]
    else:
        centro = int(elementos / 2)
        print(centro)
        return (dataSorted[centro-1]+dataSorted[centro]) / 2


print(checkio([1, 3, 2, 4, 5]))
print(checkio([1, 300, 2, 200, 1]))
print(checkio([3,6,20,99,10,15]))