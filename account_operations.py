from account_base import Account

class AccountOperations(Account):
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.add_transaction("Deposit", amount)
            print(f"Deposited ${amount} successfully.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount, pin):
        if pin == self._pin:
            if 0 < amount <= self.balance:
                self.balance -= amount
                self.add_transaction("Withdrawal", -amount)
                print(f"Withdrew ${amount} successfully.")
            else:
                print("Invalid withdrawal amount.")
        else:
            print("Invalid PIN.")

    def transfer(self, amount, recipient_account, pin):
        if pin == self._pin:
            if 0 < amount <= self.balance:
                self.balance -= amount
                recipient_account.balance += amount
                self.add_transaction(f"Transfer to {recipient_account.account_number}", -amount)
                recipient_account.add_transaction(f"Transfer from {self.account_number}", amount)
                print(f"Transferred ${amount} to {recipient_account.account_number} successfully.")
            else:
                print("Invalid transfer amount.")
        else:
            print("Invalid PIN.")
