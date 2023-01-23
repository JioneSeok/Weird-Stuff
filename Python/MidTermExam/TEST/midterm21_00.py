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

print(mergeAndSortTwoListReverse([3, 4, 1, 3, 2], [6,2,2,4,3,1]))

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

#Q9
import random
intRandom = random.randrange(1,11)

def makeRandomTenIntegers(intRandom):
