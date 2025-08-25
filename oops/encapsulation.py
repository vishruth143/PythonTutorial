# Encapsulation in Python
# Encapsulation is the bundling of data (attributes) and methods (functions) that operate
# on that data into a single unit or class. It restricts direct access to some of an object's components,
# which can prevent the accidental modification of data. In Python, encapsulation is implemented using
# access specifiers: public, protected, and private.

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner          # public
        self._balance = balance     # protected
        self.__pin = 1234           # private

    def deposit(self, amount):
        self._balance += amount
        print(f"Deposited {amount}, New Balance: {self._balance}")
        return self._balance

    def get_balance(self, pin):
        if pin == self.__pin:
            return self._balance
        else:
            return "Access Denied!"

# Usage
acc = BankAccount("Alice", 1000)

print(acc.owner)         # ✅ Public: Alice
print(acc._balance)      # ⚠️ Accessible, but not recommended
# print(acc.__pin)       # ❌ AttributeError (private)
print(acc.get_balance(1234))   # ✅ Access via method → 1000
acc.deposit(10)
print(acc.get_balance(1234))