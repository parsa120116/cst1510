class BankAccount:
    """A simple bank account with an owner and a balance."""

    def __init__(self, owner, balance=0):
        """Store the owner and the starting balance (0 if not given)."""
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        """Add money to the account."""
        if amount <= 0:
            print("Deposit refused: the amount must be more than 0.")
            return
        self.balance += amount
        print(f"Deposited {amount:.2f}. New balance: {self.balance:.2f}")

    def withdraw(self, amount):
        """Take money out, but only if there is enough."""
        if amount > self.balance:
            print(f"Withdrawal of {amount:.2f} refused: not enough money "
                  f"(balance is {self.balance:.2f}).")
            return
        self.balance -= amount
        print(f"Withdrew {amount:.2f}. New balance: {self.balance:.2f}")

    def show_balance(self):
        """Print the owner and the current balance."""
        print(f"{self.owner}'s balance: {self.balance:.2f}")


account = BankAccount("Parsa")
account.show_balance()

account.deposit(100)
account.deposit(50.5)
account.withdraw(30)
account.withdraw(500)          # should fail: not enough money
account.deposit(-20)           # should fail: not a real deposit
account.withdraw(120.5)
account.show_balance()

savings = BankAccount("Sara", 1000)
savings.show_balance()
