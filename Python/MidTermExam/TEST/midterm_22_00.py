#1
def function1(int1, int2):
    result = int1 + int2
    return result



#2
def function2(str1):
    result = len(str1)
    return result



#3
def function3(float1):
    result = str(float1)
    return result



#4
def function4(str1, ch1):
    result = str1.count(ch1)
    return result



#5
def function5(str1, str2):
    if (str1 == str2):
        return True
    else:
        return False



#6
def function6(str1, ch1):
    if (str1.count(ch1) == 1):
        return True
    else:
        return False
    


#7
def function7(str1):
    if (str1 == str1.upper()):
        return True
    else:
        return False



#8
def function8(a):
    k = 1
    for i in a:
        k = k * i
    return k



#9
def function9(list1):
    b = sorted(list1, reverse = True)
    return b

print(function9(['a','b','c']))


