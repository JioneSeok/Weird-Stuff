#1
def function1(str1, str2):
    return str1 + str2

#2
def function2(str1, str2):
    return len(str1) + len(str2)

#3
def function3(str1, int1):
    return str1 * int1


#4
def function4(str1, ch1):
    if (str1.count(ch1) == 1):
        return True
    else:
        return False

#5
def function5(int1, int2):
    k = 0
    while (int1 <= int2):
        k = k + int1
        int1 = int1 + 1
    return k

#5-1
def function5(a,b):
    sum = 0
    for i in range(a, b+1):
        sum = sum + i
    return sum


#6
def function6(list1, str1):
    if list1.count(str1) == 0:
        return False
    else:
        return True

#7 "sum"
def function7(list1):
    a = len(list1)
    b = 0
    for i in range(a):
        b = b + list1[i]
    return b

#7-1 "sum"
def function7(list1):
    a = 0
    for i in list1:
        a = a + i
    return a
#8
def function8(list1):
    k = 0
    for i in list1:
        if (i % 2 == 0):
            k = k + i
        else:
            k = k
    return k
print(function8([1,2,3,4,6]))

#9
def function9(list1, str1):
    if list1.count(str1) == 1:
        list1.remove(str1)
        return list1
    else:
        return False

print(function9(['hello','hi'],'hello'))
