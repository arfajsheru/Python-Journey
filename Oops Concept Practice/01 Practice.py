# 1. ATM System Simulation
# Design a class ATM that allows a user to:
# Check their balance.
# Withdraw money (with a daily withdrawal limit).
# Deposit money.
# Print a transaction history.
# Add functionality to handle multiple accounts using a dictionary. Implement proper exception handling for invalid operations (e.g., insufficient balance, invalid input).


class ATM:
    def __init__(self):
        self.accounts = {}

    def create_account(self,account_number, initial_balance = 0):
        if account_number in self.accounts:
            print("Account already exists.")
            return
        self.accounts[account_number] = {
            "balance": initial_balance,
            "history": []
        }
        print(f"Account {account_number} created with balance {initial_balance}.")

    def check_balance(self, account_number):
        if account_number not in self.accounts:
            print("Account does not exist.")
            return
        balance = self.accounts[account_number]["balance"]
        print(f"Balance for account {account_number}: {balance}")

    def deposit(self, account_number, amount):
        if account_number not in self.accounts:
            print("Account does not exits")
            return
        
        if amount <= 0:
            print("Invalid deposit amount.")
            return
        
        self.accounts[account_number]["balance"] += amount
        self.accounts[account_number]["history"].append(f"Deposited: {amount}")
        print(f"Deposited {amount} into account {account_number}.")

    def withdraw(self, account_number, amount):
        if account_number not in self.accounts:
            print("Account does not exits")
            return
        
        if amount <= 0:
            print("Invalid deposit amount.")
            return
        
        self.accounts[account_number]["balance"] -= amount
        self.accounts[account_number]["history"].append(f"Withdrawn: {amount}")
        print(f"Deposited {amount} into account {account_number}.")

    def printn_history(self, account_number):
        if account_number not in self.accounts:
            print("Account does not exits")
            return
        
        history = self.accounts[account_number]["history"]
        if not history:
            print("No transactions yet.")        
            return
        print(f"Transaction histroy for account {account_number}")
        for record in history:
            print(record)

atm = ATM()

atm.create_account("1234", 1000)
atm.check_balance("1234")
atm.deposit("1234",1200)
atm.withdraw("1234",2000)
atm.deposit("1234",1200)
atm.withdraw("1234",200)
atm.check_balance("1234")
atm.printn_history("1234")