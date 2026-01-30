class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __str__(self):
        return f"{self.name} has a balance of {self.balance}"


class Loan:
    def __init__(self, account: Account, eligibility_threshold: int, multiplier: int = 30):
        self.account = account
        self.eligibility_threshold = eligibility_threshold
        self.max_amount = multiplier * account.balance

    def is_eligible(self):
        return self.account.balance >= self.eligibility_threshold

    def approve_loan(self, requested_amount):
        if not self.is_eligible():
            return False, "You are not eligible for a loan."
        if requested_amount > self.max_amount:
            return False, f"Requested amount exceeds your maximum eligible loan of {self.max_amount}."
        return True, "Loan approved!"


# --- Execution ---
account = Account(name="Peace", balance=20000)
loan = Loan(account=account, eligibility_threshold=10000)

try:
    requested_amount = int(
        input("Enter the loan amount you want to apply for: "))
except ValueError:
    print("Invalid input. Please enter a numeric amount.")
    exit()

eligible, message = loan.approve_loan(requested_amount)
print(f"{account.name}, {message}")


class CashWithdrawal:
    def __init__(self, account: Account, newBalance: int, withdrawAmount: int):
        self.account = account
        self.newBalance = newBalance
        self.withdrawAmount = withdrawAmount


withdrawal_amount = int(input("Enter the amount you want to withdraw: "))
new_balance = account.balance - withdrawal_amount

if new_balance < account.balance:
    print("Insufficient funds for this withdrawal.")
else:
    print(
        f"Successfully withdrew {withdrawal_amount}. New balance is {new_balance}.")


class CashDeposit:
    def __init__(self, account: Account, newBalance: int, depositAmount: int):
        self.account = account
        self.newBalance = newBalance
        self.depositAmount = depositAmount


deposit_amount = int(input("Enter the amount you want to deposit: "))
new_balance = account.balance + deposit_amount

if new_balance < account.balance:
    print("Invalid deposit amount.")
else:
    print(
        f"Successfully deposited {deposit_amount}. New balance is {new_balance}.")


class CheckBalance:
    def __init__(self, account: Account, balance: int):
        self.account = account
        self.balance = balance


print(f"Your current balance is: {account.balance}")


class CreateAccount:
    def __init__(self, user_name: str, password: str, email: str, deposit_amount: int = 0):
        self.user_name = user_name
        self.password = password
        self.email = email
        self.deposit_amount = deposit_amount


new_account = input(
    "Create your account by entering username, password, and email: ")
deposit_amount = input("Enter initial deposit amount: ")
print(f"Account created for {new_account}/n, new balance is {deposit_amount}.")
