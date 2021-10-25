import unittest
from user import User

class TestUser(unittest.TestCase):

    '''
    This is a test class that defines test cases for the user class behaviours
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User('Juliana','Juliana@123')
    
    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.users_list=[]
    
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.username,'Juliana')  
        self.assertEqual(self.new_user.password,'Juliana@123')  
    
    def test_save_user(self):
        '''
        test_save_user to check if we can save our user object to our users_list
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.users_list),1)
 
        
    def test_user_exits(self):
        """ method to check if user exists in the users list"""
        self.new_user.save_user()
        check_user = User('Juliana', 'HakunaPassword')
        check_user.save_user()
        user_exists = User.user_exist('Juliana', 'HakunaPassword')
        self.assertTrue(user_exists)    

if __name__ == '__main__':
    unittest.main()  