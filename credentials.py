class Credentials:
    '''
    Generate new instances.
    '''
    credentials_list = [] # Empty list.
    
    def __init__(self,username,password,email):
        self.username = username
        self.password = password
        self.email = email
        
    def save_credentials(self):
        '''
        Method for saving our user's credentials.
        '''
        
        Credentials.credentials_list.append(self)
        
    def delete_credentials(self):
        '''
        Method for deleting our user's credentials.
        '''
        
        Credentials.credentials_list.remove(self)
        
    
    @classmethod
    def credentials_exist(cls,name):
        '''
        Method for checking for existence of credentials in an account.
        '''
        
        for credentials in cls.credentials_list:
            if credentials.username == name:
                return credentials
            
        return False
    
    @classmethod
    def display_credentials(cls):
        return cls.credentials_list