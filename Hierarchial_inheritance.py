
class BankAccount:
    def __init__(self, account_holder):
        self.account_holder = account_holder
        self.balance = 0

    def display_details(self):
        print("Account Holder:", self.account_holder)
        print("Balance:", self.balance)

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
            print("Remaining Balance:", self.balance)
        else:
            print("Insufficient balance")



class SavingsAccount(BankAccount):
    def __init__(self, account_holder, interest_rate):
        super().__init__(account_holder)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        self.balance = self.balance+self.balance * self.interest_rate / 100
        print("Balance after interest:", self.balance)



class CurrentAccount(BankAccount):
    def __init__(self, account_holder, overdraft_limit):
        super().__init__(account_holder)
        self.overdraft_limit = overdraft_limit

    def check_overdraft(self):
        print("The Overdraft Limit is:", self.overdraft_limit)





savings = SavingsAccount("ABC", 5)
savings.display_details()
savings.deposit(2000)
savings.withdraw(300)
savings.calculate_interest()

current = CurrentAccount("EFG", 5000)
current.display_details()
current.deposit(5000)
current.withdraw(500)
current.check_overdraft()
