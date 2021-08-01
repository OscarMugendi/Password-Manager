import unittest # Import unittest module.
from users import User # Import from users.py
from credentials import Credentials # Import from credentials.py

class TestUser(unittest.TestCase):
    def setUp(self):
        self.new_account = User("test_user","test_password") 
        
        
    def test_init(self):
        '''
        Test case to test if object has initialized.
        '''
        
        self.assertTrue(self.new_account.username,"test_user")
        self.assertEqual(self.new_account.password,"test_password")
        
    def tearDown(self):
        '''
        Method for cleaning up after other tests.
        '''
        
        User.users_list = []
        
    def test_save_account(self):
        '''
        Test to ensure new accounts can be saved to users_list.
        '''
        
        self.new_account.save_account()
        self.assertEqual(len(User.users_list),1)
        
        
    def test_login(self):
        '''
        Test for the login mechanism.
        '''
        
        self.new_account.save_account()
        test_user = User("test_user","test_password")
        test_user.save_account()
        
        found_credentials = User.login("test_user","test_password")
        self.assertEqual(found_credentials,Credentials.credentials_list)
        
        
if __name__ == '__main__':
    unittest.main()