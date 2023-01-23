class Database:

    def __init__(self):
        self.db = {}

#1
    def registNewCustomer(self, customerID, customerName):
        tmp = {}
        if self.db.get(customerID) == None:
            tmp[customerID] = customerName
            self.db[customerID] = tmp[customerID]
            return tmp
        else:
            return -1

#2
    def getCustomerNumber(self):
        return len(self.db)

#3
    def getCustomerNameByID(self, customerID):
        ID = []
        dict = {}
        count = 0
        for key, value in self.db.items():
            ID.append(key)
        if ID.count(customerID) == 0:
            return -1
        else:
            dict[customerID] = self.db[customerID]
            return dict

#4
    def getCustomerIDByName(self, customerName):
        count = 0
        keys = []
        dict = {}
        for key, value in self.db.items():
            if value == customerName:
                keys.append(key)
                count += 1
        if count > 0:
            for i in keys:
                dict[i] = self.db[i]
            return dict
        else:
            return -1
        
#5
    def getAllCustomer(self):
        return self.db

#6
    def removeCustomerByID(self, customerID):
        count = 0
        ID = []
        for key, value in self.db.items():
            if key == customerID:
                ID.append(key)
        for i in ID:
            del self.db[i]
            
        if len(ID) > 0:
            return self.db
        else:
            return -1

#7
    def removeCustomerByName(self, customerName):
        keys = []
        for key, value in self.db.items():
            if value == customerName:
                keys.append(key)
        if len(keys) > 0:
            for i in keys:
                del self.db[i]
            return self.db
        else:
            return -1

#8
    def getAllCustomerNameSorted(self):
        Name = []
        for key, value in self.db.items():
            if (value in Name) == False:
                Name.append(value)
        Name.sort()
        return Name

#9
    def getAllCustomerIDSorted(self):
        ID = []
        tmp = {}
        for key, value in self.db.items():
            ID.append(key)
        ID.sort()
        return ID

#10
    def getDuplicatedCustomerNames(self):
        Name = []
        Duplicated = []
        dict = {}
        for key, value in self.db.items():
            if (value in Name) == False:
                Name.append(value)
            else:
                Duplicated.append(value)
        for key, value in self.db.items():
            if value in Duplicated:
                dict[key] = self.db[key]
        return dict



a = Database()
a.registNewCustomer(103, 'a')
a.registNewCustomer(104, 'a')
a.registNewCustomer(105, 'b')
a.registNewCustomer(106, 'c')

result = a.getAllCustomerNameSorted()
print(result)