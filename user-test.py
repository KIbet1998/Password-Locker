import unittest
from user import User
class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the contact class behaviours
    Args:
         unnitest.Testcase:Testcase class that helps in creating test cases
    '''
       def setUp(self):
        '''
        Set up method to run before a test case
        '''
        self.new_user = User('faith','1234')
    def test_init(self):
        '''
        test case to test if the object is initialized properly
        '''
                self.assertEqual(self.new_user.username,'faith')
        self.assertEqual(self.new_user,'password')
    def test_save_accounts(self):
        '''
        to test if the account is saved
        '''
        self.new_user.save_account()
        self.assertEqual(len(User.user_list))

        def tearDown(self):
        '''
        it cleans up after each testcase has run
        '''