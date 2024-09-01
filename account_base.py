import uuid
from datetime import datetime

class Account:
    def __init__(self, name, initial_deposit, pin):
        self.account_number = self.generate_account_number()
        self.name = name
        self.balance = initial_deposit
        self._pin = pin  # Protected attribute
        self.transactions = []  # To store transaction history
        self.add_transaction("Account Created", initial_deposit)

    def generate_account_number(self):
        return str(uuid.uuid4()).split('-')[0]  # Generates a unique account number

    def get_account_details(self, pin):
        if pin == self._pin:
            details = {
                "Account Number": self.account_number,
                "Name": self.name,
                "Balance": self.balance
            }
            return details
        else:
            print("Invalid PIN.")
            return None

    def add_transaction(self, transaction_type, amount):
        transaction = {
            "Type": transaction_type,
            "Amount": amount,
            "Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Balance": self.balance
        }
        self.transactions.append(transaction)

    def view_transaction_history(self, pin):
        if pin == self._pin:
            for transaction in self.transactions:
                print(transaction)
        else:
            print("Invalid PIN.")
