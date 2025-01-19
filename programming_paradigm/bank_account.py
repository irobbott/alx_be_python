class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize the account with an optional initial balance."""
        self.account_balance = initial_balance

    def deposit(self, amount):
        """Add the specified amount to the account balance."""
        if amount > 0:
            self.account_balance += amount
        else:
            print("Invalid deposit amount. Must be positive.")

    def withdraw(self, amount):
        """Deduct the amount from the account balance if funds are sufficient."""
        if amount <= 0:
            print("Invalid withdrawal amount. Must be positive.")
            return False
        if amount > self.account_balance:
            return False
        self.account_balance -= amount
        return True

    def display_balance(self):
        """Display the current account balance."""
        print(f"Current Balance: ${self.account_balance:.2f}")
