from save import SaveService
from services import Account, LoanAccount
from user_login import login
from security import verify_value
import user_login


def verify_pin(username):
    db = SaveService()
    data = db.load()
    user = data[username]

    pin = input("Enter your PIN: ")

    if not verify_value(pin, user["pin"]):
        user["pin_attempts"] += 1
        if user["pin_attempts"] >= 3:
            user["Locked"] = True
            print("ATM card locked due to multiple failed PIN attempts.")
        else:
            print("Incorrect PIN. Please try again.")
        db.save(data)
        return False

    user["pin_attempts"] = 0
    db.save(data)
    return True


def select_account(accounts):
    for acc in accounts:
        print(f"{acc['id']}.{acc['type']} (Balance: {acc['balance']})")
    acc_id = int(input("Select account:"))
    return next(a for a in accounts if a["id"] == acc_id)


def load_menu(username):
    db = SaveService()
    data = db.load()
    loans = data[username]["loans"]

    print("\n1.Apply loan \n2.Repay loan")
    choice = input("Select option: ")

    if choice == "1":
        amount = int(input("Enter loan amount: "))
        loan = LoanAccount(amount)
        loans.append({
            "amount": amount,
            "remaining": loan.remaining,
            "status": loan.status
        })
        db.update_loans(username, loans)
        print("Loan Approved")

    elif choice == 2:
        for i, loan in enumerate(loans):
            print(
                f"{i+1}.Remaining: {loan['remaining']} (Status: {loan['status']})")

        idx = int(input("Select loan to repay: ")) - 1
        repay = int(input("Enter repayment amount: "))
        loans[idx]["remaining"] -= repay
        if loans[idx]["remaining"] <= 0:
            loans[idx]["remaining"] = 0
            loans[idx]["status"] = "CLEARED"

        db.update_loans(username, loans)
        print("Repayment successful")


def user_menu(username):
    db = SaveService()
    data = db.load()
    accounts = data[username]["accounts"]

    if not accounts:
        acc_type = input("Create account type: ")
        balance = int(input("Initial deposit: "))
        db.add_account(username, acc_type, balance)
        accounts = db.load()[username]["accounts"]

        if not verify_pin(username):
            return

        acc_data = select_account(accounts)
        account = Account(
            acc_data["id"],
            acc_data["type"],
            acc_data["balance"],
            acc_data["transactions"]
        )

        while True:
            print("\n1.Balance 2.Deposit 3.Withdraw 4.Statement 5.Loans 6.Exit")
            choice = input("Choice: ")

            try:
                if choice == "1":
                    print("Balance", account.balance)

                elif choice == "2":
                    account.deposit(int(input("Enter deposit amount: ")))

                elif choice == "3":
                    account.withdraw(int(input("Enter withdrawal amount: ")))

                elif choice == "4":
                    account.print_statement()

                elif choice == "5":
                    load_menu(username)

                elif choice == "6":
                    break

                acc_data["balance"] = account.balance
                acc_data["transactions"] = account.transactions
                db.update_accounts(username, accounts)

            except Exception as e:
                print("Error:", e)


def main():
    db = SaveService()

    while True:
        print("\n1.Login 2.Register 3.Exit")
        choice = input("Select: ")

        if choice == "1":
            user = login()
            if user:
                user_menu(user)

            elif choice == "2":
                username = input("Enter username: ")
                password = input("Enter password: ")
                pin = input("4-digit PIN: ")
                db.create_user(username, password, pin)
                print("User registered successfully.")

        elif choice == "3":
            break


if __name__ == "__main__":
    main()
