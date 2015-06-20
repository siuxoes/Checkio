__author__ = 'Siuxoes'

def checkio(first, second):
    firstSplitted = first.split(',')
    secondSplitted = second.split(',')
    list3 = []
    for x in firstSplitted:
        if x in secondSplitted:
            list3.append(x)
    list3 = sorted(list3)
    return ",".join(list3)

print(checkio("hello,world", "hello,earth"))