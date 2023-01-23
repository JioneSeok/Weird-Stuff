def calcCharacterFromString(sentence, character):
    a = str(character)
    b = str(sentence)
    numChs = b.count(a)
    if (numChs != 0):
        return numChs
    else:
        return 'error'

print(calcCharacterFromString('hello', 'l'))