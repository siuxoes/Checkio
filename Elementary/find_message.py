__author__ = 'Siuxoes'


def find_message(text):
    result = [l for l in text if l.isupper()]
    return "".join(result)

def find_message2(text):  # Another way to do it
    result = ""
    for x in text:
        if x.isupper():
            result += x
    return result

text = "How are you? Eh, ok. Low or Lower? Ohhh."

print(find_message(text))  # should print HELLO
print(find_message2(text))  # should print HELLO

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert find_message("How are you? Eh, ok. Low or Lower? Ohhh.") == "HELLO", "hello"
    assert find_message("hello world!") == "", "Nothing"
    assert find_message("HELLO WORLD!!!") == "HELLOWORLD", "Capitals"
