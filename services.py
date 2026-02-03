from datetime import datetime


class Account:
    def __init__(self, acc_id, acc_type, balance, transactions=None):
        self.acc_id = acc_id
        self.acc_type = acc_type
        self.balance = balance
        self.transactions = transactions or []

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Invalid deposit amount")
        self.balance += amount
        self._record("DEPOSIT", amount)

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Invalid withdrawal amount")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        self._record("WITHDRAW", amount)

    def _record(self, tx_type, amount):
        self.transactions.append({
            "type": tx_type,
            "amount": amount,
            "balance_after": self.balance,
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

    def print_statement(self):
        print("\n======BANK STATEMENT======")
        print(f"Account ID: {self.acc_id}")
        print(f"Account Type: {self.acc_type}")
        for tx in self.transactions:
            print(
                f"{tx['time']} | {tx['type']} | {tx['amount']} | Balance: {tx['balance_after']}")
        print("--------------------------\n")
        print(f"Current Balance: {self.balance}")
        print("==========================\n")


class LoanAccount:
    def __init__(self, amount, interest_rate=0.1):
        self.amount = amount
        self.remaining = int(amount * (1 + interest_rate))
        self.status = "ACTIVE"

    def repay(self, amount):
        if amount <= 0:
            raise ValueError("Invalid repayment amount")
        self.remaining -= amount
        if self.remaining <= 0:
            self.remaining = 0
            self.status = "CLEARED"
