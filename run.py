#!/usr/bin/env python3.6

from users import User
from credentials import Credentials

def create_account(username, password):
    '''
    Used for creating new account
    '''
    
    new_account = User(username, password)
    return new_account


def save_account(account):
    '''
    Saves the new account.
    '''
    
    account.save_account()
    
    
def create_credentials(username,password,email):
    '''
    Create credentials for a user account.
    '''
    
    new_credentials = Credentials(username,password,email)
    return new_credentials

    
def save_credentials(credentials):
    '''
    Saves new credentials.
    '''
    
    credentials.save_account()
    

def delete_credentials(credentials):
    '''
    Deletes a user account.
    '''
    
    credentials.delete_account()