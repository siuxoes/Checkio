__author__ = 'Siuxoes'

def check_pangram(text):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabetList = []
    for x in alphabet:
        alphabetList.append(x)
    text = text.replace(" ", "")
    text = text.replace(".", "")
    text = text.lower()
    import re
    regex = re.compile('[^a-zA-Z]')
    text = regex.sub("", text)
    contList = []
    if len(text) < len(alphabet):
        return False
    else:
        for x in text:
            if x not in contList:
                contList.append(x)
    if len(alphabetList) == len(contList):
        return True
    else:
        return False


print(check_pangram("The quick brown fox jumps over the lazy dog."))
