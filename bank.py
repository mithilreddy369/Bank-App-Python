from account_operations import AccountOperations

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, name, initial_deposit, pin):
        account = AccountOperations(name, initial_deposit, pin)
        self.accounts[account.account_number] = account
        print(f"Account created successfully! Account Number: {account.account_number}")
        return account

    def find_account(self, account_number):
        return self.accounts.get(account_number, None)

    def add_account(self, account):
        self.accounts[account.account_number] = account