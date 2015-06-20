__author__ = 'Siuxoes'

from collections import Counter

def checkio(text):
    text = text.replace(" ", "")
    x = Counter(text).most_common(1)
    t  = str(x)
    import re
    regex = re.compile('[^a-zA-Z]')
    text = regex.sub("", t)
    print(text)

checkio("Hello World!")

