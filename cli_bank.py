"""
cli_bank.py

CLI interface for bank operations using `Bank` class and `error_check`.

Allows creating accounts, logging in, and performing transactions in memory.
"""

import time as t
import error_check as ec
import bank_sql as sql

class Bank:
    """Represents a bank account with deposit, withdrawal, and balance operations."""

    def __init__(self, account_holder: str, age: int):
        """
        Initialize a new bank account.

        Args:
            account_holder (str): Customer's name.
            age (int): Customer's age.
        """
        self.account_holder = account_holder
        self.__balance = 0.0
        self.age = age
        print(f"\nAccount created for [{self.account_holder}]\n")

    def deposit(self, amount: float):
        """
        Deposit amount to account balance.

        Args:
            amount (float): Amount to deposit.

        Raises:
            ValueError: If amount is non-positive.
        """
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")
        self.__balance += amount
        print("Deposit successful!\n")

    def withdraw(self, amount: float):
        """
        Withdraw amount from account balance.

        Args:
            amount (float): Amount to withdraw.

        Raises:
            ValueError: If insufficient balance or invalid amount.
        """
        if amount <= 0 or amount > self.__balance:
            raise ValueError(f"Cannot withdraw ₹{amount}. Available: ₹{self.__balance}")
        self.__balance -= amount
        print("Withdrawal successful!\n")

    def get_balance(self) -> float:
        """Return current account balance."""
        return self.__balance

    def __str__(self) -> str:
        """Return a string representation of account details."""
        return f"""
    _________________________
    Account Holder's Details
        - Name: {self.account_holder}
        - Age: {self.age}
        - Balance: ₹{self.__balance}
    _________________________
    """

def main():
    """Main CLI loop: create accounts, login, and perform banking operations."""
    customers = {}
    print('Welcome to CLI Bank')

    while True:
        print("\n1. Create new A/c\n2. Login to existing A/c\n0. Exit")
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Enter a valid number (0-2).")
            continue

        if choice == 0:
            break

        if choice == 1:
            name = input("Enter your Name: ")
            try:
                age = int(input("Enter your Age: "))
            except ValueError:
                print("Age must be a number.")
                continue
            t.sleep(1)
            try:
                acc_no = int(input("Create A/c Number (1000–9999): "))
            except ValueError:
                print("Invalid account number.")
                continue
            t.sleep(1)

            if not ec.none_check(customers, acc_no):
                customers[acc_no] = Bank(name, age)
                sql.data_insert(acc_no, name, "", "")  # Optionally persist
                print("Account created and saved.")
            else:
                print(f"Account number [{acc_no}] already taken.")

        elif choice == 2:
            try:
                acc_no = int(input("Enter your A/c No: "))
            except ValueError:
                print("Invalid input.")
                continue

            if not ec.none_check(customers, acc_no):
                print(f"No account found for [{acc_no}].")
                continue

            account = customers[acc_no]
            while True:
                print("\n1.Deposit 2.Withdraw 3.Balance 4.Info 0.Logout")
                try:
                    op = int(input("Enter choice: "))
                except ValueError:
                    print("Invalid choice.")
                    continue

                if op == 0:
                    print("Logged out.")
                    break
                try:
                    if op == 1:
                        amt = float(input("Deposit amount: "))
                        account.deposit(amt)
                        sql.add_bal(acc_no, amt)
                    elif op == 2:
                        amt = float(input("Withdraw amount: "))
                        account.withdraw(amt)
                        sql.draw_bal(acc_no, amt)
                    elif op == 3:
                        print(f"Balance: ₹{account.get_balance()}")
                        sql.check_bal(acc_no)
                    elif op == 4:
                        print(account)
                        sql.ac_info(acc_no)
                    else:
                        print("Choose 0–4.")
                except ValueError as e:
                    print(e)

        else:
            print("Choose 0, 1, or 2.")

if __name__ == "__main__":
    main()
