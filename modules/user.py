class User:

  user_list=[]# Empty contact list
  def save_user(self):
    '''
    save user method saves user objects into user list
    '''
    User.user_list.append (self)
  def _init_(self, user_name, password):
    '''
        __init__ method helps define our objects properties
        Args:
            username: login's username for a new user
            password: login's password for a new user
        '''
    self.user_name = user_name
    self.password = password  

  def signIn(self,user_name,password):
       for user in User:
           if(user.user_name == user_name and user.password == password):
               return user

       return None

  def signUp(self,user_name,password):
        print(user_name)
        for user in User :
            if user.user_name==user.user_name :
                return "username exists"
        new_user = User(user.user_name, password)
        User.append(new_user)

        return "User created successfully"+new_user.user_name   
         
  @classmethod
    
  def user_exist(cls, username, password):
        '''
        this methods will check if user actually exiss from the list
        '''
        for user in cls.user_list:
            if user.username == username and user.password == password:
                return True # this returns a boolean value as the argument
            
        return False