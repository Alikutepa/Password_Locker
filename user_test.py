import unittest
from user import User

class TestUser(unittest.TestCase):
   '''
    This is a test class that defines test cases for the user class behaviours
    Args:
        unittest.Testcase: class that helps in creating test cases
    '''
def setUp(self):
    '''
        Set up method to run before each test cases.
        '''
    self.new_user = User('Juliana','Juliana@123')