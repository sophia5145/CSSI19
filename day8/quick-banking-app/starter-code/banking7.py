class BankAccount(object):
    def __init__(self,label,balance):
        self.label = label
        self.balance = balance
    
    def __str__(self):
        return self.label +":" + str(self.balance)

    def withdraw(self,balance):
        if balance < 0:
            print "Cannot withdraw negative amounts"
        elif balance > self.balance:
            print " Cannot withdraw morethan you have"   
        else:
            self.balance = self.balance - balance

    def deposit(self,balance):
        if balance < 1:
            print "cannot deposit negative amount"
        else:
            self.balance = self.balance + balance               
             


