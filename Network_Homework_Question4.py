class BankAccount:
    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0.0
​
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New balance is ${self.balance:.2f}")
        else:
            print("Deposit amount must be positive")
​
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}. New balance is ${self.balance:.2f}")
        else:
            print("Invalid withdrawal amount or insufficient funds")
​
    def get_balance(self):
        return self.balance
​
​
class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, interest_rate):
        super().__init__(account_number, account_holder)
        self.interest_rate = interest_rate
​
    def apply_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.balance += interest
        print(f"Applied ${interest:.2f} interest. New balance is ${self.balance:.2f}")
​
    def print(self):
        print(f"Current balance: ${self.balance:.2f}, Interest rate: {self.interest_rate}%")
​
​
# Create an instance of BankAccount
account = BankAccount("32465323", "Soha Darwish")
​
# Perform a deposit of $1000
account.deposit(1000)
​
# Perform a withdrawal of $500
account.withdraw(500)
​
# Print the current balance after each operation
print(f"Current balance: ${account.get_balance():.2f}")
​
# Create an instance of SavingsAccount
savings_account = SavingsAccount("32356423", "Soha Darwish", 5.0)
​
# Perform a deposit to SavingsAccount to apply interest on
savings_account.deposit(1000)
​
# Apply interest
savings_account.apply_interest()
​
# Print the current balance and interest rate
savings_account.print()