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
    self.new_user = User('Juliana','Juliana@123') # create user object

def tearDown(self):
    '''
        tearDown method that does clean up after each test case has run.
        '''
    User.user_list=[]  
    
def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.username,'Juliana')  
        self.assertEqual(self.new_user.password,'Juliana@123') 
if __name__ == '__main__':
    unittest.main()        

         