import unittest # Import unittest module.
from credentials import Credentials # Import from credentials.py

class TestCredentials(unittest.TestCase):
    def setUp(self):
        '''
        Method that runs before other tests.
        '''
        
        self.new_credentials = Credentials("test_user","test_password","test_user@test_site.com")
        
        
    def test_init(self):
        '''
        Method for testing initialization.
        '''
        self.assertEqual(self.new_credentials.username,"test_user")
        self.assertEqual(self.new_credentials.password,"test_password")
        self.assertEqual(self.new_credentials.email,"test_user@test_site.com")
        
        
    def tearDown(self):
        '''
        tearDown method for cleaning up after ourselves.
        '''
        
        Credentials.credentials_list = []
        
        
    def test_save_credentials(self):
        '''
        Used to test our ability to save user credentials
        '''
        
        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)
        
        
    def test_delete_credentials(self):
        '''
        Test for the delete functionality.
        '''
        
        self.new_credentials.save_credentials()
        test_credentials = Credentials("test_user","test_password","test_user@test_site.com")
        test_credentials.save_credentials()
        self.new_credentials.delete_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)
        
    def test_credentials_exist(self):
        '''
        Boolean test for existence of credentials in an account.
        '''
        
        self.new_credentials.save_credentials()
        test_credentials = Credentials("test_user","test_password","test_user@test_site.com")
        test_credentials.save_credentials()
        
        credentials_exist = Credentials.credentials_exist("test_user")
        self.assertTrue(credentials_exist)
        
        
if __name__ == '__main__':
    unittest.main()