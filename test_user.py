import unittest
from users import User

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
        
        
if __name__ == '__main__':
    unittest.main()