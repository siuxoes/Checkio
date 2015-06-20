__author__ = 'Siuxoes'
import re
def checkio(data):
    if len(data) >= 10:
        if re.search(r'\d', data) and re.search(r'[A-Z]', data) and re.search(r'[a-z]', data):
            return True
    else:
        return False

print(checkio('A1213pokl'))