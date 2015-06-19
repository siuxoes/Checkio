__author__ = 'Siuxoes'

import datetime

def days_diff(date1, date2):
    days = (datetime.datetime(*date2) - datetime.datetime(*date1)).days
    if days < 0:
        return -days
    return days

print(days_diff((1982,4,19), (1982,4,22)))