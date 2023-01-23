class Database:

    def __init__(self):
        self.db = {}

#1
    def registNewCustomer(self, CustomerID, CustomerName):
        if self.db.get(CustomerID) == None:
            self.db[CustomerID] = CustomerName
            temp = {}
            temp[CustomerID] = CustomerName
            return temp
        else:
            return -1

#2
    def getCustomerNumber(self):
        lenDict = len(self.db)
        return lenDict

#3
    def getCustomerNameByID(self, CustomerID):
        temp = {}
        if self.db.get(CustomerID) != None:
            temp[CustomerID] = self.db[CustomerID]
            return temp
        else:
            return -1

#4
    def getCustomerIDByName(self, CustomerName):
        temp = {}
        count = 0
        for key, value in self.db.items():
            if value == CustomerName:
                temp[key] = value
                count = count + 1
        if count > 0:
            return temp
        else:
            return -1

#5
    def getAllCustomer(self):
        return self.db

#6
    def removeCustomerByID(self, CustomerID):
        if self.db.get(CustomerID) != None:
            del self.db[CustomerID]
            return self.db
        else:
            return -1

#7
    def removeCustomerByName(self, CustomerName):
        count = 0
        keys = []
        for key, value in self.db.items():
            if value == CustomerName:
                keys.append(key)
                count = count + 1
        if count > 0:
            for i in keys:
                self.db.pop(i)
            return self.db
        else:
            return -1

#8
    def getAllCustomerNameSorted(self):
        temp = []
        for key, value in self.db.items():
            if (value in temp) == False:
                temp.append(value)
        temp.sort()
        return temp

#9
    def getAllCustomerIDSorted(self):
        temp = []
        for key, value in self.db.items():
            if (key in temp) == False:
                temp.append(key)
        temp.sort()
        return temp

#10
    def getDuplicatedCustomerNames(self):
        duplicatedNames = []
        Name = []
        for key, value in self.db.items():
            if (value in Name) == False:
                Name.append(value)
            else:
                duplicatedNames.append(value)
        temp = {}
        for key,value in self.db.items():
            if value in duplicatedNames:
                temp[key] = value
        return temp


































myDB = Database()
    

print(myDB.registNewCustomer(2022105, 'b'))
print(myDB.registNewCustomer(2022104, 'a'))
print(myDB.registNewCustomer(2022104, 'a'))
print(myDB.getDuplicatedCustomerNames())


    