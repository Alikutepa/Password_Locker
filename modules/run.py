#!/usr/bin/env python3.9
from user import User
from credentials import Credentials
import random
import string

def create_user(username,password):
    '''
    Function to create a new user
    '''
    new_user = User(username,password)
    return new_user

def save_new_user(user):
    '''
    Function to save user
    '''
    user.save_user()

def create_social_account(account_name,username,password):
    '''
    Function to create a new account
    '''
    new_account= Credentials(account_name,username,password)
    return new_account

def save_social_account(socials):
    '''
    function to save a social account's credentials
    '''
    socials.save_account()

def delete_social_account(socials):
    '''
    function to delete saved social accounts
    '''
    socials.delete_account()     

def display_accounts():
    '''
    Function that returns all the saved 
    '''
    return Credentials.display_accounts()

def create_password(length=6):

    '''
    function that generates a password for you
    '''
    characters = string.ascii_letters +string.digits + string.punctuation
    return ''.join(random.choice(characters) for i in range(length))

def main():
    print("WELCOME TO PASSWORD LOCKER")
    print("What is your name?")
    print('\n')
    user_name= input()
    print('\n')
    print(f"Hello {user_name}! You can use these short codes to navigate through")
    print('\n')

    while True:

        print('cc - Create a new password locker account')
        print('lg - Log in into your created account')
        print('ex - Exit your password locker account')
        print('\n')

        short_code = input().lower()

        if short_code == 'cc':
            print('Create your password locker account')
            print("-"*10)

            print('Username...')
            username = input()

            print('Password...')
            password = input()

            save_new_user(create_user(username,password))

            print ('\n')
            print(f'Congratulations {username} your account has been created!')

            print ('\n')
            print('You can now log in using the username and password created')

            print('Username...')
            login_username = input()

            print('Password...')
            login_password = input()

            if username != login_username or password != login_password:
                print('Invalid Username or password!')
                print('Re-enter your username....')
                login_username = input()

                print('Re- enter your password....')
                login_password = input()

            else :
                 print ('\n')
                 print(f'Hello {login_username}. Welcome to your password locker account!')
                 print ('\n')
                 social_account()

        elif short_code == 'lg':
             
                print('Log in to your existing account')
                print('Username....')
                lg_username = input()

                print('Password....')
                lg_password = input()

                if lg_username != 'Juliana' and lg_password != 'Juliana@123':
                    print('The account does not exist, please create an account')
                else:
                    print(f'Hello {lg_username}. Welcome to your password locker account!')
                    print ('\n')
                    social_account()
        elif short_code == 'ex':

                print('Bye! You can come back later!')
                break
        else:
                print('Wrong short code! Try again')


def social_account():
    print('Now you can store your social accounts credentials here!')
  
    print('Use these short codes to navigate through')
    print ('\n')

    while True:
            print('asc - Add a new social account credentials')
            print('esc - Add an existing social account credentials')
            print('dsc - Display your available social accounts credentials')
            print('del - Delete a saved account credentials')
            print('ex - Exit from the account')

            short_code = input().lower()

            if short_code == 'asc':
                print('Add a new social account credentials')
                print("-"*10)

                print('Social Account Name ...')
                accountname = input()

                print('Username....')
                username= input()
                
                print ('\n')
                print('Use:')
                print('gp - To get the password generated for you')
                print('cp - To create your own password')

                short_code1 = input().lower()
                if short_code1 == 'gp':
                    password = create_password()
                    print(password)
                elif short_code1 == 'cp':
                    print('Password....')
                    password = input()
                else:
                    print('Invalid short code')      

                save_social_account(create_social_account(accountname,username,password))
                   
                # print ('\n')
                print(f'{accountname} account credentials have been saved and stored')
            
            elif short_code == 'esc':
                print('Add your existing account credentials')
                print("-"*10)

                print('Social Account Name ...')
                accountname = input()

                print('Username...')
                username = input()

                print('Password...')
                password = input()

                save_social_account(create_social_account(accountname,username,password))
                print(f'{accountname} account credentials have been saved and stored')
                
            elif short_code == 'dsc':
                if display_accounts():
                    print("This is a list of all your saved account credentials") 
                    print("-"*20)   

                    for social in display_accounts():
                        print(
                            f"{social.account_name} {social.username} {social.password}"
                        )
                    print('\n')    
                else:
                    print('\n')
                    print('You do not have any social account credentials saved')       
                    print('\n')

            elif short_code == 'del':
                print('Which account do you want to delete?')

                deleted_account = input()       
                 
                delete_social_account(deleted_account)

            elif short_code == 'ex':
                print('Bye! You can come back later.')    
            else:
                print('Wrong short code! Try again')

if __name__ == '__main__':

    main()
