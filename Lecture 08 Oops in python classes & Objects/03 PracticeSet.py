# Let's Practice with shradha didi
# Create Account class with 2 attributes - balance & account no.Create methods for debit, credit & printing the balance.


class Account:

    def __init__(self,bal,account_no):
        self.bal = bal
        self.account_no = account_no

    def credit(self, amount):
        self.bal += amount
        print(f"Rs. {amount} was credited")
        print(f"Total Balance = {self.check_bal()}")
    
    def debited(self, amount):
        self.bal -= amount
        print(f"Rs. {amount} was debited")
        print(f"Total Balance = {self.check_bal()}")

    def check_bal(self):
        return self.bal
account = Account(2000,12323432)
print(f"Account balance {account.bal} and account no {account.account_no}")

account.credit(2000)
account.debited(3000)
account.credit(20000)
account.debited(30000)



