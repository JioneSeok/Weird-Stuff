class Server:

    def __init__(self):
        self.q = []

#1
    def makeOrder(self, orderNumber, orderList):
        a = []
        if self.q.count(orderNumber) == 0:
            self.q.append([orderNumber, orderList])
            a = [orderNumber, orderList]
            return a
        else:
            return -1

#2
    def getWaitingTime(self, orderNumber, makeTime):
        a = []
        count = 0
        for i in self.q:
            if i[0] == orderNumber:
                a.append(orderNumber)
                count += 1
        waitingTime = len(a)*makeTime
        if count > 0:
            return waitingTime
        else:
            return -1

#3
    def serveOrder(self):
        a = []
        a.append(self.q[0])
        del self.q[0]
        return a[0]

#4
    def getOrderNumber(self):
        return len(self.q)

#5
    def cancelOrder(self, orderNumber):
        a= []
        count = 0
        for i in self.q:
            if i[0] == orderNumber:
                a.append(i)
                self.q.remove(i)
                count += 1
        if count > 0:
            return a[0]
        else:
            return -1, -1

#6
    def makeOrderVIP(self, orderNumber):
        a = []
        num = []
        count = 0
        for i in self.q:
            num.append(i[0])

        for i in len(num):
            for j in num:
                if num[i] == orderNumber:
                    a.append(j)
                else:
                    a.insert(0, orderNumber)
                    count += 1
        if count > 0:
            self.q = num
            return a
        else:
            -1
        pass

#7 
    def giveService(self, orderNumber, serviceMenu):
        a = []
        count = 0
        for i in self.q:
            if i[0] == orderNumber:
                a.append(i)
                count = count + 1
            for j in range(len(a)):
                a[j].append(serviceMenu)
        if count > 0:
            return a
        else:
            return -1


a = Server()
a.makeOrder(1, 'a')
a.makeOrder(2, 'b')

result = a.makeOrder(1, 'c')
print(result)