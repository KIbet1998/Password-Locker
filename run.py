import random
from user import User
#create a contact
def create_accounts(username,password):

    '''
    Function to create new account
    '''
    new_account = User(username,password)
    return new_account
   #save contacts
def save_accounts(account):
    '''
    method to save the user account
    '''
    account.save_account()
def del_account(account):
    '''
    funcion to delete account
    '''
    account.delete_account()

def display_account():
    '''
    returns all saved accounts
    '''
    return User.display_account()
def main():
    print("Welcome to Your password locker.What is your name?")
    username = input()

    print(f"Hello {username}. What would you like to do?")
    print('\n')
    while True:
        print("Use these short codes: ca - create a new account,da - display account, fa - find contact, ex - exit password locker,del - delete account")
        short_code = input().lower()
        # print('\n')
        if short_code == 'ca':
            print("New User")
            username =input()
            print("New password")
            password = input()
            save_accounts(create_accounts(username,password))
            print('\n')
            print(f"new Account {username} {password} created")
            print('\n')


        elif short_code == 'da':

            if display_account():
                print("Here is a list of all your accounts and passwords")
                print('\n')
                for account in display_account():
                    print(f"{account.username} {account.password}")
                    print('\n')
            else:
                print('\n')
                print("You dont seem to have any account saved yet")
                print('\n')

if __name__=='__main__':
    main()

