# main.py

from bank import Bank
from transaction import Transaction

def main():
    bank = Bank()

    print("Welcome to Simple Bank Application")
    
    while True:
        print("\nMain Menu")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Transfer Money")
        print("5. View Account Details")
        print("6. View Transaction History")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            name = input("Enter your name: ")
            initial_deposit = float(input("Enter initial deposit: "))
            pin = int(input("Set your 4-digit PIN: "))
            bank.create_account(name, initial_deposit, pin)

        elif choice == '2':
            account_number = input("Enter your account number: ")
            account = bank.find_account(account_number)
            if account:
                transaction = Transaction(account)
                amount = float(input("Enter amount to deposit: "))
                transaction.perform_deposit(amount)
            else:
                print("Account not found.")

        elif choice == '3':
            account_number = input("Enter your account number: ")
            account = bank.find_account(account_number)
            if account:
                transaction = Transaction(account)
                amount = float(input("Enter amount to withdraw: "))
                pin = int(input("Enter your PIN: "))
                transaction.perform_withdrawal(amount, pin)
            else:
                print("Account not found.")

        elif choice == '4':
            sender_account_number = input("Enter your account number: ")
            sender_account = bank.find_account(sender_account_number)
            if sender_account:
                transaction = Transaction(sender_account)
                recipient_account_number = input("Enter recipient's account number: ")
                recipient_account = bank.find_account(recipient_account_number)
                if recipient_account:
                    amount = float(input("Enter amount to transfer: "))
                    pin = int(input("Enter your PIN: "))
                    transaction.perform_transfer(amount, recipient_account, pin)
                else:
                    print("Recipient account not found.")
            else:
                print("Account not found.")

        elif choice == '5':
            account_number = input("Enter your account number: ")
            account = bank.find_account(account_number)
            if account:
                pin = int(input("Enter your PIN: "))
                details = account.get_account_details(pin)
                if details:
                    print("\nAccount Details:")
                    for key, value in details.items():
                        print(f"{key}: {value}")
            else:
                print("Account not found.")

        elif choice == '6':
            account_number = input("Enter your account number: ")
            account = bank.find_account(account_number)
            if account:
                pin = int(input("Enter your PIN: "))
                print("\nTransaction History:")
                account.view_transaction_history(pin)
            else:
                print("Account not found.")

        elif choice == '7':
            print("Thank you for using Simple Bank Application. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
