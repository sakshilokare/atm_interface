import random
import sys

class Transaction:
    def __init__(self, amount, transaction_type):
        self.amount = amount
        self.transaction_type = transaction_type

    def __repr__(self):
        return f"{self.transaction_type.capitalize()} {self.amount}"

class User:
    def __init__(self, user_id, pin, balance=0):
        self.user_id = user_id
        self.pin = pin
        self.balance = balance
        self.atm = ATM(balance)

    def is_valid_login(self, user_id, pin):
        return self.user_id == user_id and self.pin == pin

class ATM:
    def __init__(self, balance=0):
        self.balance = balance
        self.transaction_history = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(
                Transaction(amount, "deposited"))
            return True
        else:
            print("Invalid deposit amount.")
            return False

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(
                Transaction(amount, "withdrawn"))
            return True
        else:
            print("Invalid withdrawal amount.")
            return False

    def transfer(self, target_atm, amount):
        if amount > 0 and amount <= self.balance:
            self.withdraw(amount)
            target_atm.deposit(amount)
            self.transaction_history.append(
                Transaction(amount, "transferred to another account"))
            return True
        else:
            print("Invalid transfer amount.")
            return False

    def display_transaction_history(self):
        print("Transaction history:")
        for transaction in self.transaction_history:
            print(transaction)

    def quit(self):
        print("Thank you for using the ATM. Goodbye!")
        sys.exit()

def main():
    users = {
        1: User(1, 1234, 1000),
        2: User(2, 2345, 2000),
        3: User(3, 3456, 3000)
    }

    while True:
        print("\nWelcome to the ATM!")
        print("1. Log in")
        print("2. Quit")

        try:
            choice = int(input("Enter your choice (1-2): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 2.")
            continue

        if choice == 1:
            user_id = int(input("Enter your user ID: "))
            pin = int(input("Enter your PIN: "))

            if user_id in users and users[user_id].is_valid_login(user_id, pin):
                print("Login successful!")
                user_atm = users[user_id].atm
                while True:
                    print("\nATM Menu:")
                    print("1. Check balance")
                    print("2. Deposit")
                    print("3. Withdraw")
                    print("4. Transfer")
                    print("5. Transaction history")
                    print("6. Log out")
                    print("7. Quit")

                    try:
                        choice = int(input("Enter your choice (1-7): "))
                    except ValueError:
                        print("Invalid input. Please enter a number between 1 and 7.")
                        continue

                    if choice == 1:
                        print(f"Your current balance is ${user_atm.balance:.2f}")
                    elif choice == 2:
                        try:
                            amount = float(input("Enter the deposit amount: "))
                        except ValueError:
                            print("Invalid input. Please enter a number.")
                            continue
                        if user_atm.deposit(amount):
                            print(f"${amount:.2f} has been deposited.")
                    elif choice == 3:
                        try:
                            amount = float(input("Enter the withdrawal amount: "))
                        except ValueError:
                            print("Invalid input. Please enter a number.")
                            continue
                        if user_atm.withdraw(amount):
                            print(f"${amount:.2f} has been withdrawn.")
                    elif choice == 4:
                        try:
                            target_atm = ATM()
                            amount = float(input("Enter the transfer amount: "))
                        except ValueError:
                            print("Invalid input. Please enter a number.")
                            continue
                        if user_atm.transfer(target_atm, amount):
                            print(f"${amount:.2f} has been transferred to another account.")
                    elif choice == 5:
                        user_atm.display_transaction_history()
                    elif choice == 6:
                        print("Logged out.")
                        break
                    elif choice == 7:
                        user_atm.quit()
                    else:
                        print("Invalid choice. Please enter a number between 1 and 7.")
            else:
                print("Invalid user ID or PIN. Please try again.")
        elif choice == 2:
            print("Thank you for using the ATM. Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please enter a number between 1 and 2.")

if __name__ == "__main__":
    main()