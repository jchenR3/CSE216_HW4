from pyTPS_Transaction import pyTPS_Transaction

class pyTPS:

    def __init__(self):
        self.transactions = []
        self.mostRecentTransaction = -1
        self.performingDo = False
        self.performingUndo = False

    def isPerformingDo(self):
        return self.isPerformingDo
    
    def isPerformingUndo(self):
        return self.isPerformingUndo
    
    def hasTransactionToRedo(self):
        if(len(self.transactions) > 0 and self.mostRecentTransaction == -1):
            return True
        elif((self.mostRecentTransaction > -1) and (self.mostRecentTransaction < (len(self.transactions)-1))):
            return True
        return False
    
    def hasTransactionToUndo(self):
        return self.mostRecentTransaction >= 0
    
    def getSize(self):
        return len(self.transactions)
    
    def getRedoSize(self):
        return (len(self.transactions) - self.mostRecentTransaction-1)
    
    def getUndoSize(self):
        return self.mostRecentTransaction+1
    
    def addTransaction(self, transaction):
        if((self.mostRecentTransaction < 0) or (self.mostRecentTransaction < (len(self.transactions)-1))):
            for i in range(len(self.transactions), self.mostRecentTransaction-1):
                del self.transactions[i]
        self.transactions.append(transaction)
        self.doTransaction()

    def doTransaction(self):
        if(self.hasTransactionToRedo()):
            self.isPerformingDo = True
            transaction = self.transactions[self.mostRecentTransaction+1]
            transaction.doTransaction()
            self.mostRecentTransaction+=1
            self.isPerformingDo = False
    
    def undoTransaction(self):
        if self.hasTransactionToUndo():
            self.performingUndo = True
            transaction = self.transactions[self.mostRecentTransaction]
            transaction.undoTransaction()
            self.mostRecentTransaction -= 1
            self.performingUndo = False

    def clearAllTransactions(self):
        self.transactions = []
        self.mostRecentTransaction = -1

    def toString(self):
        result = f"--Number of Transactions: {len(self.transactions)}\n"
        result += f"--Current Index on Stack: {self.mostRecentTransaction}\n"
        result += "--Current Transaction Stack:\n"
      
        for i in range(self.mostRecentTransaction + 1):
            transactions = self.transactions[i]
            result += f"----{transactions.toString()}\n"
        return result