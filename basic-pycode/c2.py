class amount:
    def __init__(self):
        self.balance=0
        print("hery!!! welcome to the bank")
    def deposite(self):
        amount=float(input("enter the amount to deposite\n"))
        self.balance += amount
        print(amount)
    def withdraw(self):
        amount=float(input("enter the amount to withdraw\n"))
        self.balance -= amount
        print(amount)
    def display(self):
        print("net available balance:\n",self.balance)    
s = amount()
s.deposite()
s.withdraw()
s.display()