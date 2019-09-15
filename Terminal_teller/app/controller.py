from .account import Account
from . import view


def run():
    while True:
        choice = view.login_menu()
        if choice == '1': # create account
            username = view.get_username()
            pin = view.get_pin()
            balance = view.get_deposit()
            new_account = Account()
            new_account.username = username
            new_account.pin = pin
            new_account.balance = balance
            new_account.api_key = new_account.generate_api_key()
            new_account.save()
            mainmenu(new_account)
        elif choice == '2': # login
            api = view.user_api()
            account = Account.api_authenticate(api)
            if not account:
                view.error()
            else:
                mainmenu(account)
        elif choice == '3': # Exit
            return
        else:
            view.bad_input()

def mainmenu(account):
    while True:
        
        choice = view.main_menu()
        if choice == '1': # Get Balance
            view.show_balance(account.balance)

        elif choice == '2': # Withdraw
            amount = view.get_amount()
            account.withdraw(amount)
            account.save()

        elif choice == '3': # Deposit
            amount = view.get_amount()
            account.deposit(amount)
            account.save()

        elif choice == '4': # Get api
            api_key = account.get_api()
            view.my_key(api_key)
            account.save()

            

        elif choice == '5': # Exit
            view.logout_message()
            account.save()
            return
        else:
            view.bad_input()

