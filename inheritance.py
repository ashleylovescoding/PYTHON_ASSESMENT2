class BankAccount:
    def __init__(self,account_holder,balance=0):
        self.account_holder = account_holder
        self.balance = balance
    def deposit(self,amount):
        self.balance += amount
        return self.balance
    def display_balance(self):
        print(f"account_holder: {self.account_holder}, balance: {self.balance}")

class SavingsAccount(BankAccount):
    def __init__(self,account_holder,balance=0):
        super().__init__(account_holder,balance)
    def add_interest(self,rate):
        interest=self.balance*(rate/100)
        self.balance += interest
        return self.balance
account1 =BankAccount("Ashley",6000)
account1.deposit(100)
account1.display_balance()

savings= SavingsAccount("Ashley",6000)
savings.deposit(1000)
savings.add_interest(2)
savings.display_balance()



