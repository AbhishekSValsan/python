class Account:
    def __init__(self, name, balance):
        self._name = name
        self._balance = balance

    def __add__(self, other):
        if (other, Account):
            return self._balance + other._balance
        return 

    def display(self):
        print(f"Account holder: {self._name}, Balance: {self._balance}")

class savings_account(Account):
    def calculate_interest(self):
        return self._balance * 0.05
    
class current_account(Account):
    def calculate_interest(self):
        return self._balance * 0.02
    
savings = savings_account("Ravi", 10000)

current = current_account("Anjali", 15000)
savings.display()
print("Savings Account Interest(5%):", savings.calculate_interest())
current.display()
print("Current Account Interest:(2%):", current.calculate_interest())

print("Total Balance (ALICE + BOB): ", savings + current)
