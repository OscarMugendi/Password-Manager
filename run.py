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
    
def login(username,password):
    '''
    Creates login functionality
    '''
    
    login = User.login(username, password)
    if login != False:
        return User.login(username,password)
    
def search_account(username):
    return User.find_by_username(username)
    
    
def check_account(username,password):
    return Credentials.display_credentials()
    
    
def display_credentials():
    return Credentials.display_credentials()
    
### def main()

def main():
    '''
    Main function of my app.
    '''
    
    print("\n")
    # Our welcome page.
    print(
        '''
        Welcome to the Password Manager App.
        A simple tool to help you manage your passwords.
        To continue, you must either login or sign up.
        Use the following short codes to proceed:-
        
            su => Sign up
            lg => Log in
            ex => Exit
            dl => Delete account credentials
        '''
    )
    print("\n")
    short_code = input().lower()
    if short_code == "su": # Signup for a new account.
        print("Let us create a new account.")
        username = input('Username:')
        print("\n")
        password = input('Password:')
        print("\n")
        email = input('Email:')
        print("\n")
        
        save_account(create_account(username,password))
        print("\n")
        
        print(f"Congratulations {username}, your account has been created.")
        print(
            f'''
            User Info:-
            
            Username: {username}
            Password: {password}
            Email: {email}
            '''
        ) 
        print("Press 'ex' to exit from the application")
        print("\n")
        short_code = input().lower()
        if short_code == 'ex':
            print("Goodbye.")
            
        else:
            print(
            f'''
            User Info:-
            
            Username: {username}
            Password: {password}
            Email: {email}
            '''
            )
            print("\n")
            print("Instructions unclear, please refer to the short codes.")
            short_code = input().lower()
            if short_code == 'ex':
                print("Goodbye.")
                
            else:
                print("Instructions unclear, please refer to the short codes.")
            
        print("\n")
        
    elif short_code == "lg":
        print("\n")
        print("Please enter your account username.")
        username = input()
        print("\n")
        print("Please enter your password")
        password = input()
        print("\n")
        
        login = check_account(username,password)
        
        if login ==True:
            print
            print(f"Login successful. Welcome, {username}.")
            print("\n")
            
            while True:
                print(
                    '''
                    More short_codes:-
                        dc => Display Account Credentials.
                        ex => Log out and exit the application.
                    '''
                )
                
                short_code = input().lower()
                if short_code == "dc":
                    print("\n")
                    for credentials in display_credentials():
                        print(f"Username:{credentials.username} Password:{credentials.password} Email:{credentials.email}") 
                        print("\n")
                        
                elif short_code == "ex":
                    print("\n")
                    print("Goodbye.")
                    print("\n")
                    break
                
                else:
                    print("Instructions unclear, please refer to the short codes.")
            
        else:
            print("\n")
            print("Incorrect password")
            print("\n")
                
    elif short_code == "ex":
                print("\n")
                print("Goodbye.")
        
    else:
        print("Instructions unclear, pleaser refer to the short codes")
            
            
if __name__ == '__main__':
    main()