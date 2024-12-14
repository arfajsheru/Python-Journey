# Example of Encapsulation in python 

class BankAccount: 
    def __init__(self,name, account_holder, balance):
        self.account_holder = account_holder
        self.name = name
        self.__balance = balance

        print(f"Account name: {name}\nAccount number is: {account_holder}")


    def get_balance(self):
        return f"The curren balance for {self.account_holder} is {self.__balance}"

    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
            return f"Successfully deposited {amount}. Update balance is {self.__balance}"
        else: 
            return f"Deposit amount must be positive"

    def withraw(self,amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return f"Successfully withraw {amount}. Remaining balance is {self.__balance}"
        elif amount > self.__balance:
            return "Insufficient funds."
        else:
            return "Withraw amount must be positive."



account = BankAccount("Arfaj","12345",2000)
print(account.get_balance)
print(account.deposit(1000))
print(account.withraw(40000))


try:
    print(account.__balance)  # This will raise an AttributeError
except AttributeError:
    print("Cannot access private attribute directly!")

print(account.get_balance())
        