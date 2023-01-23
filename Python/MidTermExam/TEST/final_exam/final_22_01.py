class Server:

    def __init__(self):
        self.q = []

#1
    def makeOrder(self, orderNumber, orderList):
        existAlready = False
        for i in self.q:
            if i[0] == orderNumber:
                existAlready = True
        if existAlready == True:
            return -1
        else:
            tmp = []
            tmp.append(orderNumber)
            tmp.append(orderList)
            self.q.append(tmp)
            return tmp

#2
    def getWaitingTime(self, orderNumber, timePerProduct):
        existingOrder = False
        waitingTime = 0
        for i in self.q:
            waitingTime = waitingTime + len(i[1])*timePerProduct
            if i[0] == orderNumber:
                existingOrder = True
                break
        if existingOrder == True:
            return waitingTime
        else:
            return -1

#3
    def serveOrder(self):
        orderNumber = self.q[0][0]
        orderList = self.q[0][1]
        del self.q[0]
        return orderNumber, orderList

#4
    def getOrderNumber(self):
        for i in self.q:
            getOrderNumber = len(self.q)
        return getOrderNumber

#5
    def TcancelOrder(self, orderNumber):
        orderAlready = False
        for i in self.q:
            if i[0] == orderNumber:
                orderAlready = True
        if orderAlready == True:
            for i in self.q:
                del i[0]
            return i[0][1], self.q
        else:
            return -1, -1
    
#5
    def cancelOrder(self, orderNumber):
        count = -1
        for i in self.q:
            if i[0] == orderNumber:
                count = count + 1 
                break
            
        if count == -1:
            return -1, -1
        else:
            orderNumber = self.q[count][0]
            orderList = self.q[count][1]
            del self.q[count]
            return orderNumber, orderList

#6
    def makeOrderVIP(self, orderNumber, orderList):
        existAlready = False
        for i in self.q:
            if i[0] == orderNumber:
                existAlready = True
        if existAlready == True:
            return -1
        else:
            tmp = []
            tmp.append(orderNumber)
            tmp.append(orderList)
            self.q.insert(0,tmp)
            
            a = []
            for i in self.q:
                a.append(i[0])
            return a

#7
    def giveService(self, orderNumber, serviceList):
        count = 0
        orderIndex = -1
        for i in self.q:
            if i[0] == orderNumber:
                orderIndex = count
                break
            count = count + 1
        if orderIndex == -1:
            return -1, -1
        else:
            orderNumber = self.q[orderIndex][0]
            self.q[orderIndex][1].append(serviceList)
            orderList = self.q[orderIndex][1]
            return orderNumber, orderList

#8
    def getOrderItems(self):
        count = 0
        for i in self.q:
            count = count + len(i[1])
        return count










myDB = Server()
myDB.makeOrder(123, 'pizza')
myDB.makeOrder(124, 'hamburger')
print(myDB.getOrderItems())