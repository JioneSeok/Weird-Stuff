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
    



