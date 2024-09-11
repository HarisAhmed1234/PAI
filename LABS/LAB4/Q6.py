from datetime import datetime

class BankAccount:
    def __init__(self, account_number, customer_name, initial_balance=0.0, date_of_opening=None):
        self.account_number = account_number
        self.customer_name = customer_name
        self.balance = initial_balance
        self.date_of_opening = date_of_opening if date_of_opening else datetime.now().strftime("%Y-%m-%d")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def check_balance(self):
        print(f"Account Balance: ${self.balance:.2f}")

    def account_info(self):
        print(f"Account Number: {self.account_number}")
        print(f"Customer Name: {self.customer_name}")
        print(f"Balance: ${self.balance:.2f}")
        print(f"Date of Opening: {self.date_of_opening}")

if __name__ == "__main__":
    account = BankAccount(account_number="987654321", customer_name="Haris Messi", initial_balance=500.0)

    account.account_info()

    account.deposit(250.0)

    account.withdraw(100.0)

    account.check_balance()
