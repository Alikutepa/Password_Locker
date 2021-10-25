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

