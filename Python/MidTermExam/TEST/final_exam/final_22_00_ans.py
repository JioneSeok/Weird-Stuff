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



score = 0

# problem 1
try:
    myDB = Database()

    solution = [True, True, True]
    answer = []

    res = myDB.registNewCustomer('0001', 'Apple')
    if res == {'0001': 'Apple'}:
        answer.append(True)

    res = myDB.registNewCustomer('0002', 'Tomato')
    if res == {'0002': 'Tomato'}:
        answer.append(True)

    res = myDB.registNewCustomer('0001', 'Apple')
    if res == -1:
        answer.append(True)

    if answer == solution:
        score += 6
        print("[1] SUCCESS")
    else:
        print("[1] FAIL")
except:
    print("[1] FAIL")

# problem 2
try:
    solution = 3
    answer = 0

    myDB = Database()

    myDB.registNewCustomer('0001', 'Apple')
    myDB.registNewCustomer('0002', 'Tomato')
    myDB.registNewCustomer('0009', 'Peach')

    answer = myDB.getCustomerNumber()
    # print(answer)

    if answer == solution:
        score += 6
        print("[2] SUCCESS")
    else:
        print("[2] FAIL")
except:
    print("[2] FAIL")

# problem 3
try:
    solution = {'0002': 'Tomato'}
    answer = 0

    myDB = Database()

    myDB.registNewCustomer('0001', 'Apple')
    myDB.registNewCustomer('0002', 'Tomato')
    myDB.registNewCustomer('0009', 'Peach')

    answer = myDB.getCustomerNameByID('0002')
    # print(answer)

    if answer == solution:
        answer = myDB.getCustomerNameByID('0010')
        if answer == -1:
            score += 6
            print("[3] SUCCESS")
        else:
            print("[3] FAIL")
    else:
        print("[3] FAIL")
except:
    print("[3] FAIL")


# problem 4
try:
    solution = {'0002': 'Tomato', '0004': 'Tomato'}
    answer = 0

    myDB = Database()

    myDB.registNewCustomer('0001', 'Apple')
    myDB.registNewCustomer('0002', 'Tomato')
    myDB.registNewCustomer('0004', 'Tomato')
    myDB.registNewCustomer('0009', 'Peach')

    answer = myDB.getCustomerIDByName('Tomato')
    # print(answer)

    if answer == solution:
        if myDB.getCustomerIDByName('XXX') == -1:
            score += 6
            print("[4] SUCCESS")
        else:
            print("[4] FAIL")
    else:
        print("[4] FAIL")
except:
    print("[4] FAIL")

# problem 5
try:
    solution = {'0001': 'Apple', '0002': 'Tomato',
                '0004': 'Tomato', '0009': 'Peach'}
    answer = 0

    myDB = Database()

    myDB.registNewCustomer('0001', 'Apple')
    myDB.registNewCustomer('0002', 'Tomato')
    myDB.registNewCustomer('0004', 'Tomato')
    myDB.registNewCustomer('0009', 'Peach')

    answer = myDB.getAllCustomer()
    # print(answer)

    if answer == solution:
        score += 6
        print("[5] SUCCESS")
    else:
        print("[5] FAIL")
except:
    print("[5] FAIL")

# problem 6
try:
    solution = {'0001': 'Apple', '0002': 'Tomato',
                '0004': 'Tomato'}
    answer = 0

    myDB = Database()

    myDB.registNewCustomer('0001', 'Apple')
    myDB.registNewCustomer('0002', 'Tomato')
    myDB.registNewCustomer('0004', 'Tomato')
    myDB.registNewCustomer('0009', 'Peach')

    answer = myDB.removeCustomerByID('0009')
    # print(answer)

    if answer == solution:
        if myDB.removeCustomerByID('0009') == -1:
            score += 6
            print("[6] SUCCESS")
        else:
            print("[6] FAIL")
    else:
        print("[6] FAIL")
except:
    print("[6] FAIL")

# problem 7
try:
    solution = {'0001': 'Apple', '0009': 'Peach'}
    answer = 0

    myDB = Database()

    myDB.registNewCustomer('0001', 'Apple')
    myDB.registNewCustomer('0002', 'Tomato')
    myDB.registNewCustomer('0004', 'Tomato')
    myDB.registNewCustomer('0009', 'Peach')

    answer = myDB.removeCustomerByName('Tomato')
    # print(answer)

    if answer == solution:
        if myDB.removeCustomerByName('Tomato') == -1:
            score += 6
            print("[7] SUCCESS")
        else:
            print("[7] FAIL")
    else:
        print("[7] FAIL")
except:
    print("[7] FAIL")

# problem 8
try:
    solution = ['Apple', 'Peach', 'Tomato']
    answer = 0

    myDB = Database()

    myDB.registNewCustomer('0001', 'Apple')
    myDB.registNewCustomer('0002', 'Tomato')
    myDB.registNewCustomer('0004', 'Tomato')
    myDB.registNewCustomer('0009', 'Peach')

    answer = myDB.getAllCustomerNameSorted()
    # print(answer)

    if answer == solution:
        score += 6
        print("[8] SUCCESS")
    else:
        print("[8] FAIL")
except:
    print("[8] FAIL")

# problem 9
try:
    solution = ['0001', '0002', '0004', '0009']
    answer = 0

    myDB = Database()

    myDB.registNewCustomer('0001', 'Apple')
    myDB.registNewCustomer('0009', 'Peach')
    myDB.registNewCustomer('0004', 'Tomato')
    myDB.registNewCustomer('0002', 'Tomato')

    answer = myDB.getAllCustomerIDSorted()
    # print(answer)

    if answer == solution:
        score += 6
        print("[9] SUCCESS")
    else:
        print("[9] FAIL")
except:
    print("[9] FAIL")


# problem 10
try:
    solution = {'0002': 'Tomato', '0004': 'Tomato',
                '0009': 'Peach', '0008': 'Peach'}
    answer = 0

    myDB = Database()

    myDB.registNewCustomer('0001', 'Apple')
    myDB.registNewCustomer('0002', 'Tomato')
    myDB.registNewCustomer('0004', 'Tomato')
    myDB.registNewCustomer('0009', 'Peach')
    myDB.registNewCustomer('0008', 'Peach')

    answer = myDB.getDuplicatedCustomerNames()
    #  print(answer)

    if answer == solution:
        score += 6
        print("[0] SUCCESS")
    else:
        print("[0] FAIL")
except:
    print("[0] FAIL")

print("\nTOTAL SCORE -->> ", score, "\n")


# 채점시 주의사항
# 1) 모든 문제에서 새롭게 Database 객체를 만들어서 사용할 것임
# 2) 모든 문제에서 registNewCustomer()를 사용하여 항목을 추가함. 따라서 메소드가 틀리면 연쇄적으로 오점 처리됨
