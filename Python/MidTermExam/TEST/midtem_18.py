#2
def isSentenceWithArticle(s):
    if s[0] + s[1] + s[2] +s[3] == 'The ' or 'the ':
        return 'True'
    elif s[0] + s[1] + s[2] == 'An ' or 'an ':
        return 'True'
    elif s[0] + s[1] == 'A ' or 'a ':
        return 'True'
    else:
        return 'False'

print(isSentenceWithArticle("apple"))

#3
