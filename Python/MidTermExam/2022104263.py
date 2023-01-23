#Q1
def addInteger(int1, int2):
    result = int1 + int2
    return result

#Q2
def addFloat(num1, num2):
    a = float(num1)
    b = float(num2)
    result = a + b
    return result

#Q3
def addFloatToString(num1, num2):
    a = float(num1)
    b = float(num2)
    c = a + b
    str1 = str(c)
    return str1

#Q4
def addFloatToStringList(num1, num2):
    a = float(num1)
    b = float(num2)
    c = a + b
    str1 = str(num1)
    str2 = str(num2)
    str3 = str(c)

    k = []
    k.append(str1)
    k.append(str2)
    k.append(str3)

    return k

#Q5
def calcGugudanToListInList(num):
    for i in [num]:
        list1 = []
        for j in [1,2,3,4,5,6,7,8,9]:
            list1.append([i,j,i*j])
    return list1

