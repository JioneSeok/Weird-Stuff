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

#7-2 "sum"
def function7(list1,list2):
    list3 = list1 + list2
    a = 0
    for i in list3:
        a = a + i
    return a