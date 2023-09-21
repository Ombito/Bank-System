class Bank_accounts:

    total_balance = 0

    def __init__(self, acc_number, acc_name, balance):
        self.acc_number = acc_number
        self.acc_name = acc_name
        self.balance = balance
        Bank_accounts.total_balance += balance
     
    @classmethod
    def total_bank_balance(cls):
        print(cls.total_balance)

    def deposit(self, amount):
        self.balance += amount
        Bank_accounts.total_balance += amount
    
    def check_balance(self):
        print(f"Hello Alvin, Your current balance is {self.balance}")

    def withdraw(self, amount):
        if amount > 0 and self.balance:
            self.balance -= amount
            print(f'Hello Alvin, you have successfully withdrawn {amount}')
        else:
            print("Insufficient funds")
    
class Savings_account(Bank_accounts):
    def add_interest(self):
        self.balance * 1.03


bin = Bank_accounts(2222, "Alvin", 0)
bin.deposit(20000)
bin.withdraw(2000)

mercy = Savings_account(2222, "Mercy", 70000)
print(mercy.add_interest())
print(bin.check_balance())git 