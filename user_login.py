user = {
    "user_name": "amani_mumo",
    "password": "mumo!123",
    "email": "peacemumo107@gmail.com"
}


def login():
    print("Enter your credentials to login.")


user_input = {
    "user_name": input("Enter your username: "),  # Prompt for username
    "password": input("Enter your password: "),  # Prompt for password
    "email": input("Enter your email: ")         # Prompt for email
}

try:
    if user_input["user_name"] == user["user_name"]:
        print("Username is correct")
    else:
        print("Username is incorrect")

    if user_input["password"] == user["password"]:
        print("Password is correct")
    else:
        print("Password is incorrect")

    if user_input["email"] == user["email"]:
        print("Email is correct")
    else:
        print("Email is incorrect")

except KeyError as e:
    print(f"KeyError: {e}. Please ensure all keys are correct.")
