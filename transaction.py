from account_operations import AccountOperations

class Transaction:
    def __init__(self, account):
        self.account = account

    def perform_deposit(self, amount):
        self.account.deposit(amount)

    def perform_withdrawal(self, amount, pin):
        self.account.withdraw(amount, pin)

    def perform_transfer(self, amount, recipient_account, pin):
        self.account.transfer(amount, recipient_account, pin)
