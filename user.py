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
    def delete_account(self):
        '''
        deletes saved account
        '''
        User.user_list.remove(self)






