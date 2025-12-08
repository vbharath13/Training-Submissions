class BankAccount:
    # CLASS ATTRIBUTE (common to all accounts)
    bank_name = "Python National Bank"
    min_balance = 0

    def __init__(self, owner, balance=0):
        # INSTANCE ATTRIBUTES (unique to each object)
        self._owner = owner
        self._balance = balance

    # -------------------------------
    # PROPERTY DECORATORS
    # -------------------------------
    @property
    def owner(self):
        """Getter for owner"""
        return self._owner

    @owner.setter
    def owner(self, name):
        """Setter with validation"""
        if not name.strip():
            raise ValueError("Owner name cannot be empty.")
        self._owner = name

    @property
    def balance(self):
        """Getter for balance (no setter: balance changes via transactions only)."""
        return self._balance

    # -------------------------------
    # INSTANCE METHODS
    # -------------------------------
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self._balance += amount
        print(f"💰 Deposited ${amount}. New balance: ${self._balance}")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if self._balance - amount < BankAccount.min_balance:
            raise ValueError("Insufficient funds!")
        self._balance -= amount
        print(f"🏧 Withdrew ${amount}. New balance: ${self._balance}")

    def show_details(self):
        print(f"🏦 {BankAccount.bank_name}")
        print(f"Account Owner: {self.owner}")
        print(f"Current Balance: ${self.balance}")

    # -------------------------------
    # CLASS METHOD
    # -------------------------------
    @classmethod
    def change_bank_name(cls, new_name):
        cls.bank_name = new_name
        print(f"🏦 Bank name updated to: {cls.bank_name}")

    # -------------------------------
    # STATIC METHOD
    # -------------------------------
    @staticmethod
    def validate_amount(amount):
        """Static utility: checks if amount is valid."""
        return amount > 0


# -------------------------------------------
#  DEMO / TESTING THE BANK ACCOUNT SYSTEM
# -------------------------------------------

try:
    # Create account instance
    acc = BankAccount("Bharath", 500)

    acc.show_details()
    print()

    # Transactions
    acc.deposit(200)
    acc.withdraw(100)
    print()

    # Using static method
    print("Valid amount?", BankAccount.validate_amount(50))

    # Using class method
    BankAccount.change_bank_name("Python Federal Bank")
    acc.show_details()

except ValueError as e:
    print("❌ Error:", e)
