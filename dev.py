
class OverdraftError(Exception):
    pass

class Account:
    def __init__(self,owner,initial_balance=0):
        self.owner=owner
        self.__balance=initial_balance
        self.transaction_history=[]

    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount
            self.transaction_history.append(f"Deposited: ${amount}")
            print(f"Successfully deposited ${amount}")
        else:
            print("Deposit amount be positive")
    def withdraw(self,amount):
        try:
            if amount>self.__balance:
                raise OverdraftError(f"Insufficient funds! Current balance: $ {self.__balance}")
            if amount<=0:
                print("Withdraw must be positive")
                return
            self.__balance-=amount
            self.transaction_history.append(f"Withdrew: ${amount}")

        except OverdraftError as e:
            print(f"Error: {e}")

    def get_balance(self):
        return f"Account balance for {self.owner}: ${self.__balance}"
    def show_history(self):
        print(f"\n--- Transaction History for {self.owner}---")
        for record in self.transaction_history:
            print(record)
my_acc=Account("Krishnaswamy", 500)
print(my_acc.get_balance())
my_acc.deposit(200)
my_acc.withdraw(100)
my_acc.withdraw(1000)
my_acc.show_history()