import json
import os
from services import Account


class Save:
    def __init__(self, filename="user_data.json"):
        self.filename = filename
        os.makedirs("data", exist_ok=True)

    def save_user(self, user: Account):
        user_data = {
            "name": user.name,
            "balance": user.balance
        }
        with open(os.path.join("data", self.filename), 'w') as file:
            json.dump(user_data, file)
        print(f"User data for {user.name} saved successfully.")

    def load_user(self) -> Account:
        try:
            with open(os.path.join("data", self.filename), 'r') as file:
                user_data = json.load(file)
                return Account(name=user_data["name"], balance=user_data["balance"])
        except FileNotFoundError:
            print("No saved user data found.")
            return None
        except json.JSONDecodeError:
            print("Error decoding user data.")
            return None
