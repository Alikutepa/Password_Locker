import unittest
from credentials import Credentials

class TestCredentials(unittest.TestCase):

    '''
    Test class that defines test cases for the contact class behaviours.
    '''

    def setUp(self):

        '''
        Set up method to run before each test cases.
        '''

        self.new_socials = Credentials('Facebook','Julie_Ali','Juliana@123')

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''

        Credentials.account_list=[]

    def test_init(self):

        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_socials.account_name,'Facebook')
        self.assertEqual(self.new_socials.username,'Julie Ali') 
        self.assertEqual(self.new_socials.password,'Juliana@123')

    def test_save_account(self):

        '''
        test_save_account test case to test if the account object is saved into
         the account list
        '''

        self.new_socials.save_account()
        self.assertEqual(len(Credentials.account_list),1)

    
    
    def test_delete_account(self):
        '''
        test_delete_account test case to test if the account object is removed from
         the account list
         '''
        self.new_socials.save_account() 
        test_account =  Credentials('Facebook','Julie Alie','Juliana@123')
        test_account.save_account()
        
        self.new_socials.delete_account()
        self.assertEqual(len(Credentials.account_list),1)
    
  
if __name__ == '__main__':
    unittest.main()  