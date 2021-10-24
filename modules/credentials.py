class Credentials:
  '''
    class that generates new instances of account names and their credentials
    '''

  account_list=[]

  def __init__(self,account_name,username,password):
        '''
        __init__ method that helps us define properties for our objects.
        '''
        self.account_name=account_name
        self.username=username
        self.password=password


  def save_account(self):

        '''
        save_account method saves accounts objects into the contact_list
        '''
        Credentials.account_list.append(self)

  def delete_account(self):
        '''
        deletes save accounts from the account list
        '''
        Credentials.account_list.remove(self)