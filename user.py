class User:
    '''
    class that generates new instace of user
    '''
    def __init__(self,username,password):
        '''
        creates properties of instance of user class
        '''
        self.username = username
        self.password = password
    user_list = []
    def save_account(self):
        '''
        save_account method saves a new user objects to the user list
        '''
        User.user_list.append(self)
    @classmethod
    def delete_account(self,username):
        '''
        deletes saved account
        '''
        for user in User.user_list:
            if user.username == username:

                User.user_list.remove(user)

    @classmethod
    def display_account(cls):
        '''
        returns the user list
        '''
        return cls.user_list






