def main_menu():
    print("Welcome to Terminal Teller!")
    print("What would you like to do?")
    print("1. Get Balance")
    print("2. Withdraw")
    print("3. Deposit")
    print("4. My API")
    print("5. Exit")
    return input("Your choice: ")

def my_key(api_key):
    print("Your API key is {}".format(api_key))

def user_api():
    return input("what is your api? ")

def show_balance(balance):
    print()
    print("Your balance is: ", balance)
    print()

def get_amount():
    print()
    amount = input('How much money? ')
    print()
    return float(amount)

def login_menu():
    print("Welcome to Terminal Teller!")
    print("What would you like to do?")
    print("1. Creat Account")
    print("2. Log In")
    print("3. Exit")
    return input("Your choice: ")

def get_username():
    print()
    return input("Your username: ")

def get_pin():
    print()
    return input("Your pin: ")

def get_deposit():
    print()
    deposit = input("Amount to deposit: ")
    return float(deposit)

def error():
    print()
    print("Account does not exist!")
    print()

def bad_input():
    print()
    print("Incorrect input")
    print()

def logout_message():
    print()
    print("Thanks for using Terminal Teller")