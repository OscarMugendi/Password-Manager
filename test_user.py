import unittest
from users import User

class TestUser(unittest.TestCase):
    def setUp(self):
        self.new_account = User("test_user","test_password") 
        
        
    def tearDown(self):
        '''
        Method for cleaning up after other tests.
        '''
        
        User.user_list = []