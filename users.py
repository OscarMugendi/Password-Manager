class User:
    '''
    A class used to create new accounts.
    '''
    
    users_list = [] # Empty list.
    
    def __init__(self,username,password):
        '''
        Init method that establishes the properties of our accounts.
        
        Args:
            username: User's name
            password: User's password
        '''
        
        self.username = username
        self.password = password
        
        
    def save_account(self):
        '''
        Method for saving new accounts.
        '''
        User.users_list.append(self)