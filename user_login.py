from save import SaveService
from security import verify_value


def login():
    db = SaveService()
    data = db.load()

    username = input("Username: ")
    password = input("Password: ")

    user = data.get(username)
    if not user or not verify_value(password, user["password"]):
        print("Invalid login credentials")
        return None

    if user["locked"]:
        print("ATM card locked to to multiple failed PIN attempts.")
        return None

    print(f"Welcome {username}")
    return username
