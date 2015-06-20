__author__ = 'Siuxoes'


def checkio(words_set):
    word_list = sorted(list(words_set), key=len)
    return any([word_list[i] in word_list[j][-len(word_list[i]):]
                for i in range(len(word_list))
                for j in range(i + 1, len(word_list))])


#  print(checkio({"hello", "lo", "he"}))
print(checkio({"hello","la","hellow","cow"}))
