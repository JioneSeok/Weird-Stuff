#### ANSWER: START


#Q1
def calculateSecond(int1, int2, int3, int4):
    day = int1
    hour = int2
    minute = int3
    second = int4
    result = day*86400 + hour*3600 + minute*60 + second
    return result

#Q2
def reverseString(str):
    return str[::-1]

#Q3
def calcTwoCharactersFromString(iString, iCh1, iCh2):
    result = iString.count(iCh1) + iString.count(iCh2)
    return result

#Q4
def calcTwoCharactersFromStringV2(iString,iCh1, iCh2):
    if iCh1 == iCh2:
        return int(-1)
    else:
        result = iString.count(iCh1) + iString.count(iCh2)
        return result

#Q5
def calcTwoCharactersFromStringV3(iString, iChList):
    k = 0
    for i in iChList:
        k = k + iString.count(i)
    return k

#Q6
def mergeAndSortTwoList(iList1, iList2):
    a = iList1 + iList2
    c = []
    for i in a:
        if (c.count(i) == 0):
            c.append(i)
        else:
            continue
    return sorted(c)



#Q7
def mergeAndSortTwoListReverse(iList1, iList2):
    a = iList1 + iList2
    c = []
    for i in a:
        if (c.count(i) == 0):
            c.append(i)
        else:
            continue
    d = sorted(c)
    e = d[::-1]
    return e

#Q8
def searchMatchedCharacter(iList, iCh):
    a = len(iList)
    b = []
    for i in range(a):
        if iList[i][0].count(iCh) == 1:
            b.append(iList[i])
        else:
            continue
    c = sorted(b)
    return c

#### ANSWER: END

#### Self Scoring : Start ####

TotalScore = 0

try:
    if calculateSecond(1,1,1,2) == 90062:
        TotalScore += 5
        print("[Q01-PASSED.1] Score - ", TotalScore)
    else:
        print("[Q01-failed.1] Score - ", TotalScore)
    if calculateSecond(2,3,4,5) == 183845:
        TotalScore += 5
        print("[Q01-PASSED.2] Score - ", TotalScore)
    else:
        print("[Q01-failed.2] Score - ", TotalScore)
except:
    print("[Q01-failed.except] Score - ", TotalScore)

try:
    if reverseString("Hello World!!") == '!!dlroW olleH':
        TotalScore += 5
        print("[Q02-PASSED.1] Score - ", TotalScore)
    else:
        print("[Q02-failed.1] Score - ", TotalScore)
    if reverseString("Welcome to Hell!!") == '!!lleH ot emocleW':
        TotalScore += 5
        print("[Q02-PASSED.2] Score - ", TotalScore)
    else:
        print("[Q02-failed.2] Score - ", TotalScore)
except:
    print("[Q02-failed.except] Score - ", TotalScore)

try:
    if calcTwoCharactersFromString("You only live once", 'o', 'o') == 6:
        TotalScore += 5
        print("[Q03-PASSED.1] Score - ", TotalScore)
    else:
        print("[Q03-failed.1] Score - ", TotalScore)
    if calcTwoCharactersFromString("You only live once", 'o', 'Y') == 4:
        TotalScore += 5
        print("[Q03-PASSED.2] Score - ", TotalScore)
    else:
        print("[Q03-failed.2] Score - ", TotalScore)
except:
    print("[Q03-failed.except] Score - ", TotalScore)

try: 
    if calcTwoCharactersFromStringV2("You only live once", 'o', 'o') == -1:
        TotalScore += 5
        print("[Q04-PASSED.1] Score - ", TotalScore)
    else:
        print("[Q04-failed.1] Score - ", TotalScore)
    if calcTwoCharactersFromStringV2("You only live once", 'o', 'Y') == 4:
        TotalScore += 5
        print("[Q04-PASSED.2] Score - ", TotalScore)
    else:
        print("[Q04-failed.2] Score - ", TotalScore)
except:
    print("[Q04-failed.except] Score - ", TotalScore)

try:
    if calcTwoCharactersFromStringV3("You only live once", ['a', 'o', 'o']) == 6:
        TotalScore += 10
        print("[Q05-PASSED] Score - ", TotalScore)
    else:
        print("[Q05-failed.try] Score - ", TotalScore)
except:
    print("[Q05-failed.except] Score - ", TotalScore)

try:
    if mergeAndSortTwoList([1,1,2,3,5,8,13,24,34,55], [1,1,2,3,4,5,6,7,8,9,10,11,12]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 24, 34, 55]:
        TotalScore += 10
        print("[Q06-PASSED] Score - ", TotalScore)
    else:
        print("[Q06-failed.except] try - ", TotalScore)
except:
    print("[Q06-failed.except] Score - ", TotalScore)

try: 
    if mergeAndSortTwoListReverse([1,1,2,3,5,8,13,24,34,55], [1,1,2,3,4,5,6,7,8,9,10,11,12]) == [55, 34, 24, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]:
        TotalScore += 10
        print("[Q07-PASSED] Score - ", TotalScore)
    else:
        print("[Q07-failed.try] Score - ", TotalScore)
except:
    print("[Q07-failed.except] Score - ", TotalScore)

try:
    kingdoms = ['Bacteria', 'Protozoa','Chromista','Plantae','Fungi','Animalia']
    if searchMatchedCharacter(kingdoms, 'P') == ['Plantae', 'Protozoa']:
        TotalScore += 10
        print("[Q08-PASSED] Score - ", TotalScore)
    else:
        print("[Q08-failed.try] Score - ", TotalScore)
except:
    print("[Q08-failed.except] Score - ", TotalScore)

try:
    examResult = makeRandomTenIntegers()
    examResult.sort()
    if examResult == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
        TotalScore += 10
        print("[Q09-PASSED] Score - ", TotalScore)
    else:
        print("[Q09-failed.try] Score - ", TotalScore)
except:
    print("[Q09-failed.except] Score - ", TotalScore)

try:
    examResult = makeRandomIntegersExtended(20,1)
    examResult.sort()
    if examResult == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]:
        TotalScore += 10
        print("[Q10-PASSED] Score - ", TotalScore)
    else:
        print("[Q10-failed.try] Score - ", TotalScore)
except:
    print("[Q10-failed.except] Score - ", TotalScore)

#### Self Scoring : End ####

print("==>> FINAL SCORE: ", TotalScore)
