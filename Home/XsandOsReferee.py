__author__ = 'Siuxoes'

def checkio(game_result):
    match = []
    for i in game_result:
        match.append(list(i))
    # rows
    for i in match:
        if len(set(i)) == 1 and i[0] != ".":
            return i[0]
    # cols
    match2 = zip(*match[::-1])
    for i in match2:
        if len(set(i)) == 1 and i[0] != '.':
            return i[0]
    # crosses
    if match[0][0] == match[1][1] == match[2][2] != ".":
        return match[0][0]
    if match[0][2] == match[1][1] == match[2][0] != ".":
        return match[2][0]
    return "D"

if __name__ == '__main__':
    assert checkio([
        u"X.O",
        u"XX.",
        u"XOO"]) == "X", "Xs wins"
    assert checkio([
        u"OO.",
        u"XOX",
        u"XOX"]) == "O", "Os wins"
    assert checkio([
        u"OOX",
        u"XXO",
        u"OXX"]) == "D", "Draw"