# 🏦 CLI Bank System

A simple Python-based banking system featuring:

* A **MySQL-backed backend** (`bank_sql.py`) for persistent storage of customer data.
* A **command-line interface** (`cli_bank.py`) implementing features like account creation, deposits, withdrawals, balance checks, and fund transfers.
* Clean modular code and **Google-style docstrings** for maintainability.

---

## 🔧 Features

### MySQL layer (`bank_sql.py`)

* `data_insert`: create accounts with zero balance.
* `data_sel`, `check_bal`, `ac_info`, `all_info`: query account existence, balance, and details.
* `add_bal`, `draw_bal`: deposit and withdraw money.
* `transfer`: move funds between accounts securely.

### In‑memory CLI (`cli_bank.py`)

* `Bank` class encapsulates account operations.
* Interactive menus to create new accounts, log in, and perform transactions.
* Automatically logs actions to both in-memory and MySQL backends.

---

## 📦 Requirements

* Python 3.x
* `mysql-connector-python` (install via `pip`)
* MySQL server with a `bank` database and `customers` table:

```sql
CREATE DATABASE bank;
USE bank;
CREATE TABLE customers (
  ac_no INT PRIMARY KEY,
  name VARCHAR(100),
  phone_no VARCHAR(20),
  address VARCHAR(255),
  bal DECIMAL(12,2)
);
```

---

## ⚙️ Setup & Installation

1. Clone or download the repository.

2. Install dependencies:

   ```bash
   pip install mysql-connector-python
   ```

3. Adjust MySQL credentials (host, user, password, database) in `bank_sql.py` if needed.

4. Ensure the `customers` table exists (create it if necessary).

---

## 🚀 Usage

Run the CLI shell:

```bash
python cli_bank.py
```

### Main Menu Options:

1. **Create new A/c** – set up in-memory and MySQL account (auto-saves).
2. **Login to existing A/c** – access account for:

   * Deposit
   * Withdrawal
   * Balance inquiry
   * Account info display
3. **Exit** – close the program.

Operations update both the in-memory object and the SQL database.

---

## 📚 Project Structure

```
.
├── bank_sql.py        # MySQL persistence layer with account handling
├── cli_bank.py        # Interactive CLI + in-memory `Bank` class
├── error_check.py     # Helper for checking account existence
└── README.md          # This documentation
```

---

## 🔄 Data Persistence

* In-memory accounts are stored in a Python `dict` during runtime.
* All transactions are also **persisted in MySQL**, ensuring durability.

---

## 🔒 Security & Best Practices

* Uses parameterized SQL queries to prevent injection.
* Input validation and exception handling improve robustness.
* Docstrings and modular organization facilitate future extensions.

---

## 🧰 Useful Links & References

* Example banking CLI with MySQL backend on GitHub ([github.com][1], [github.com][2])
* Real‑Python guide to great Python README structure ([realpython.com][3])

---

## 💡 License & Contributions

Feel free to fork, modify, and enhance this project. Contributions are welcome! No specific license is declared—consider this open-source and free to use.


[1]: https://github.com/Rahul-Dahale/Bank_Management_System?utm_source=chatgpt.com "Bank Management System using python and Mysql - GitHub"
[2]: https://github.com/SaiRamana-IITH/Banking-Project-using-MySQL-and-Python?utm_source=chatgpt.com "GitHub - SaiRamana-IITH/Banking-Project-using-MySQL-and-Python"
[3]: https://realpython.com/readme-python-project/?utm_source=chatgpt.com "Creating Great README Files for Your Python Projects - Real Python"
