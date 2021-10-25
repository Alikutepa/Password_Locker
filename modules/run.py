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