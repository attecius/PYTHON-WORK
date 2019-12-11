#  i var account
#  wid Dep 
#  1000
#  1000

class account:
    def __init__(self):
        self.balance=0
        print("hey! welcome")
    def deposite(self):
        amount=float(input("enter amount deposite"))
        self.balance += amount
        print(amount)
    def withdraw(self):
        amount=float(input("enter amount to withdraw"))
        self.balance -=amount
        print(amount)
    def display(self):
        print(self.balance)        


s=account()
s.deposite()
s.withdraw()
s.display()
