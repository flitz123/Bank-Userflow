from user_login import login
from services import Account, Loan, CashWithdrawal, CashDeposit, CheckBalance


def main():
    print("Welcome to the Banking System")
    print("1. Check Balance")
    print("2. Withdraw Cash")
    print("3. Deposit Cash")
    print("4. Apply for Loan")
    print("5. Create Account")
    choice = input("Please select an option (1-5): ")

    if choice == '1':
        balance_check = CheckBalance(account=Account(
            name="Peace", balance=20000), balance=20000)
        print(f"Your current balance is: {balance_check.balance}")
    elif choice == '2':
        withdrawal_amount = int(
            input("Enter the amount you want to withdraw: "))
        new_balance = 20000 - withdrawal_amount
        if new_balance < 0:
            print("Insufficient funds for this withdrawal.")
        else:
            print(
                f"Successfully withdrew {withdrawal_amount}. New balance is {new_balance}.")
    elif choice == '3':
        deposit_amount = int(input("Enter the amount you want to deposit: "))
        new_balance = 20000 + deposit_amount
        print(
            f"Successfully deposited {deposit_amount}. New balance is {new_balance}.")
    elif choice == '4':
        account = Account(name="Peace", balance=20000)
        loan = Loan(account=account, eligibility_threshold=10000)
        requested_amount = int(
            input("Enter the loan amount you want to apply for: "))
        eligible, message = loan.approve_loan(requested_amount)
        print(f"{account.name}, {message}")
    elif choice == '5':
        name = input("Enter your name: ")
        initial_deposit = int(input("Enter initial deposit amount: "))
        new_account = Account(name=name, balance=initial_deposit)
        print(
            f"Account created for {new_account.name} with balance {new_account.balance}.")
    else:
        print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
