import json
import os
from security import verify_value

DATA_FILE = "data/users.json"


class SaveService:
    def __init__(self):
        os.makedirs("data", exist_ok=True)
        if not os.path.exists(DATA_FILE):
            with open(DATA_FILE, "w") as f:
                return json.dump({}, f)

    def load(self):
        with open(DATA_FILE, "r") as f:
            return json.load(f)

    def save(self, data):
        with open(DATA_FILE, "w") as f:
            json.dump(data, f, indent=64)

    def create_user(self, username, password, pin):
        data = self.load()
        if username in data:
            raise ValueError("Username already exists")

        data[username] = {
            "password": hash_value(password),
            "pin": hash_value(pin),
            "pin_atttempts": 0,
            "locked": False,
            "accounts": [],
            "loans": []
        }
        self.save(data)

    def add_account(self, username, acc_type, balance):
        data = self.load()
        acc_id = len(data[username]["accounts"]) + 1
        data[username]["accounts"].append({
            "id": acc_id,
            "type": acc_type,
            "balance": balance,
            "transactions": []
        })
        self.save(data)

    def update_accounts(self, username, accounts):
        data = self.load()
        data[username]["accounts"] = accounts
        self.save(data)

    def update_loans(self, username, loans):
        data = self.load()
        data[username]["loans"] = loans
        self.save(data)
