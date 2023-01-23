class MyClass:
    countObject = 0
#1
    def __init__(self, givenStr):
        self.Str = givenStr
        MyClass.countObject = MyClass.countObject + 1
#2
    def getId(self):
        return self.Str
#3
    def setId(self, givenStr):
        self.Str = str(givenStr)

#4
    def getNumberOfObject():
        return MyClass.countObject

#5
    def storeWordlistAsDictionary(self, givenList):
        sortList = givenList.sort()
        v = []
        dict = {}
        for i in sortList:
            v.append(sortList.count(i))
        for key, value in sortList, v:
            dict[key] = value
            self.Dict[key] = dict[key]
        return dict

#6






class1 = MyClass("Harry Potter")
class2 = MyClass("Hermione Granger")

print(class1.getId())
print(class2.getId())

print(MyClass.getNumberOfObject())

a = MyClass(['a','a','a','b','b'])
print(a.storeWordlistAsDictionary(['a','a','a','b','b']))

