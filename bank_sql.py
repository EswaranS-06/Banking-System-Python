"""
bank_sql.py

Module for managing bank customer data using MySQL.

Provides functions to create accounts, retrieve information,
deposit, withdraw, transfer funds, and list all customers.
"""

import mysql.connector as sql

# -- Database Connection Setup --
mydb = sql.connect(
    host='localhost',
    user='root',
    password='2726',
    database='bank'
)

def all_info():
    """Fetch and print all customer records from the database."""
    mc = mydb.cursor()
    mc.execute('SELECT * FROM customers')
    for ac_no, name, phone, address, bal in mc.fetchall():
        print(f"""
        _________________________
        Account Holder's Details
            - Name: {name}
            - A/c no: {ac_no}
            - Balance: ₹{bal}
            - Phone no: {phone}
            - Address: {address}
        _________________________
        """)

def data_insert(ac, name, phone, address):
    """
    Create a new customer account with zero balance.

    Args:
        ac (int): Unique account number.
        name (str): Customer's name.
        phone (str): Customer's phone number.
        address (str): Customer's address.

    Returns:
        bool: False if account exists, otherwise True.

    """
    mc = mydb.cursor()
    mc.execute('SELECT ac_no FROM customers WHERE ac_no = %s', (ac,))
    if mc.fetchone():
        print('Account exists. Choose a different number.')
        return False

    mc.execute(
        'INSERT INTO customers (ac_no, name, phone_no, address, bal) VALUES (%s,%s,%s,%s,%s)',
        (ac, name, phone, address, 0.0)
    )
    mydb.commit()
    print(f"{mc.rowcount} account created — A/c no: {ac}")
    return True

def data_sel(ac):
    """
    Check if an account number exists.

    Args:
        ac (int): Account number to check.

    Returns:
        bool: True if account exists, otherwise False.
    """
    mc = mydb.cursor()
    mc.execute('SELECT ac_no FROM customers WHERE ac_no = %s', (ac,))
    if mc.fetchone():
        return True
    print('Account not found—create a new account.')
    return False

def add_bal(ac, dep):
    """
    Deposit funds to an account.

    Args:
        ac (int): Account number.
        dep (float): Amount to deposit.

    Raises:
        ValueError: If deposit amount is non-positive.
    """
    if dep <= 0:
        raise ValueError("Deposit amount must be positive.")
    mc = mydb.cursor()
    mc.execute('SELECT bal FROM customers WHERE ac_no = %s', (ac,))
    cu_bal = mc.fetchone()[0]
    mc.execute('UPDATE customers SET bal = %s WHERE ac_no = %s', (cu_bal + dep, ac))
    mydb.commit()
    print("Amount credited successfully.")

def draw_bal(ac, draw):
    """
    Withdraw funds from an account.

    Args:
        ac (int): Account number.
        draw (float): Amount to withdraw.

    Raises:
        ValueError: If insufficient balance or negative withdrawal.
    """
    if draw <= 0:
        raise ValueError("Withdrawal amount must be positive.")
    mc = mydb.cursor()
    mc.execute('SELECT bal FROM customers WHERE ac_no = %s', (ac,))
    cu_bal = mc.fetchone()[0]
    if cu_bal < draw:
        raise ValueError("Insufficient balance.")
    mc.execute('UPDATE customers SET bal = %s WHERE ac_no = %s', (cu_bal - draw, ac))
    mydb.commit()
    print("Amount debited successfully.")

def check_bal(ac):
    """
    Print current balance of an account.

    Args:
        ac (int): Account number.
    """
    mc = mydb.cursor()
    mc.execute('SELECT bal FROM customers WHERE ac_no = %s', (ac,))
    bal = mc.fetchone()[0]
    print(f"\nYour Account Balance: ₹{bal}\n")

def ac_info(ac):
    """
    Print detailed account information.

    Args:
        ac (int): Account number.
    """
    mc = mydb.cursor()
    mc.execute('SELECT ac_no, name, phone_no, address, bal FROM customers WHERE ac_no = %s', (ac,))
    ac_no, name, phone, address, bal = mc.fetchone()
    print(f"""
    _________________________
    Account Holder's Details
        - Name: {name}
        - A/c no: {ac_no}
        - Balance: ₹{bal}
        - Phone no: {phone}
        - Address: {address}
    _________________________
    """)

def transfer(ac, tac, fund):
    """
    Transfer funds from one account to another.

    Args:
        ac (int): Sender's account number.
        tac (int): Receiver's account number.
        fund (float): Amount to transfer.

    Returns:
        str: Result message.

    Raises:
        ValueError: For insufficient balance or invalid recipient.
    """
    mc = mydb.cursor()
    mc.execute('SELECT bal FROM customers WHERE ac_no = %s', (ac,))
    sender_bal = mc.fetchone()
    if not sender_bal:
        raise ValueError("Sender account not found.")
    sender_bal = sender_bal[0]

    mc.execute('SELECT bal FROM customers WHERE ac_no = %s', (tac,))
    receiver_bal = mc.fetchone()
    if not receiver_bal:
        raise ValueError("Recipient account not found.")
    receiver_bal = receiver_bal[0]

    if sender_bal < fund:
        raise ValueError(f"Insufficient balance: ₹{sender_bal}")

    mc.execute('UPDATE customers SET bal = %s WHERE ac_no = %s', (sender_bal - fund, ac))
    mc.execute('UPDATE customers SET bal = %s WHERE ac_no = %s', (receiver_bal + fund, tac))
    mydb.commit()
    return f"Transferred ₹{fund} from {ac} to {tac}."
