            
class Bank:
    def __init__(self,bank_name):
        self.bank_name = bank_name
        self.accounts = []
    
    def add_account(self,account):
        self.accounts.append(account)
        self.accounts.sort(key=lambda x: x.account_holder)
        self.display_accounts()
    
    def display_accounts(self):
        print("\n========== BANK ACCOUNTS ==========")
        print("Bank:", self.bank_name)
        if len(self.accounts) == 0:
            print("No accounts available.")
            return
        
        for account in self.accounts:
            print(f"Account Holder: {account.account_holder}, Balance: ${account.get_balance():.2f}")
            
    def remove_account(self,account_holder):
        for account in self.accounts:
            if account.account_holder == account_holder:
                self.accounts.remove(account)
                self.display_accounts()
                return
        print("Account not found.")


class BankAccount :
    def __init__(self,account_holder,initial_balance=0):
        self.account_holder = account_holder
        self._balance = initial_balance
    def deposit(self,amount):
        self._balance += amount
    def withdraw(self,amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
        else:
            print("Invalid withdrawal amount or insufficient funds.")
    def get_balance(self):
        return self._balance

class SavingsAccount(BankAccount):
    def __init__(self,account_holder,initial_balance=0,interest_rate=0.02):
        
        super().__init__(account_holder,initial_balance)
        self.interest_rate = interest_rate
        
    def deposit(self,amount):
        self._balance += amount    

    def add_interest(self):
        interest = self.get_balance() * self.interest_rate
        self.deposit(interest)
        
    def withdraw(self, amount):
        if 0 < amount <= self.get_balance():
            self._balance -= amount
        else:
            print("INVALID WITHDRAWAL AMOUNT OR INSUFFICIENT FUNDS.")
            
    def display_account_info(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: ${self.get_balance():.2f}")
        print(f"Interest Rate: {self.interest_rate}")  
        
    def sent_massage(self) :
        print(f"Dear {self.account_holder}, your current balance is ${self.get_balance():.2f}.")     
    
class CurrentAccount(BankAccount):
    def __init__(self,account_holder,initial_balance=0,overdraft_limit=0):
        super().__init__(account_holder,initial_balance)
        self.overdraft_limit = overdraft_limit
        
    def deposit(self, amount):
        self._balance += amount

    
    def add_interest(self):
        print("Current accounts do not earn interest.")
        
    def withdraw(self, amount):
        if 0< amount <= (self.get_balance() + self.overdraft_limit):
            self._balance -= amount       
        else :
            print("INVALID WITHDRAWAL AMOUNT OR INSUFFICIENT FUNDS.")
            
    def display_account_info(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: ${self.get_balance():.2f}")
        print(f"Overdraft Limit: ${self.overdraft_limit:.2f}")
        print("Current accounts do not earn interest.")
    
    def sent_massage(self) :
        print(f"Dear {self.account_holder}, your current balance is ${self.get_balance():.2f}.")   
    
class FixedDepositAccount(BankAccount):
    def __init__(self,account_holder,initial_balance=0,interest_rate=0.05,term_years=1):
        super().__init__(account_holder,initial_balance)
        self.interest_rate = interest_rate
        self.term_years = term_years 
        
    def deposit(self,amount):
        print("Deposits are not allowed in a fixed deposit account after the initial deposits.")    
        
    def add_interest(self):
        interest = self.get_balance() * self.interest_rate * self.term_years
        self._balance += interest
        
    def withdraw(self,amount):
        print("Withdrawals are not allowed from a fixed deposit account before maturity.")
        
    def display_account_info(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: ${self.get_balance():.2f}")
        print(f"Interest Rate: {self.interest_rate}")
        print(f"Term: {self.term_years} years")
        
    def sent_massage(self) :
        print(f"Dear {self.account_holder}, your current balance is ${self.get_balance():.2f}.")    
            
class CheckingAccount(BankAccount):
    def __init__(self,account_holder,initial_balance=0,overdraft_limit=0):
        super().__init__(account_holder,initial_balance)
        self.overdraft_limit = overdraft_limit
            
    def withdraw(self,amount):
        if 0 < amount <= (self.get_balance() + self.overdraft_limit):
            self._balance -= amount
        else:
            print("Invalid withdrawal amount or insufficient funds.")
    
    def display_account_info(self):
        print("Account Holder:", self.account_holder)
        print("Balance: $", self.get_balance())
        print("Overdraft Limit: $", self.overdraft_limit)        



Bank = Bank("My Bank")
Bank.add_account(SavingsAccount("Abhijeet", 10000, 0.03))
Bank.add_account(CurrentAccount("Aditya", 50000, 10000))
Bank.add_account(FixedDepositAccount("Prathamesh", 100000, 0.05, 3))

print("="*30)
Bank.display_accounts()

print("============== Detail of Accounts Information ==============")
Abhijeet_acc = Bank.accounts[0]
Aditya_acc = Bank.accounts[1]
Prathamesh_acc = Bank.accounts[2]

Abhijeet_acc.display_account_info()
print("="*20)
Aditya_acc.display_account_info()
print("="*20)
Prathamesh_acc.display_account_info()

print("=============== Acount Testing Transactions ===============")

print("Adding interest to Abhijeet's Savings Account:")
Abhijeet_acc.add_interest()
Abhijeet_acc.sent_massage()

print("\nWithdrawing $60000  (User Overdraft)....")
Aditya_acc.withdraw(65000)
Aditya_acc.sent_massage()

print("\nAttempting to withdraw $50000 from prathamesh's fixed deposit account (should not be allowed):")
Prathamesh_acc.withdraw(50000)

print("\nAdding interest to Prathmesh's Fixed Deposit Account:")
Prathamesh_acc.add_interest()
Prathamesh_acc.sent_massage()
