__author__ = 'Siuxoes'

def count_words(text, words):
    counter = 0
    for i in words:
        if text.lower().find(i) != -1:
            counter += 1
    return counter

texto = "How aresjfhdskfhskd you?"
words = {"how", "are", "you", "hello"}

print(count_words(texto, words)) # should print 3