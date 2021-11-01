class Student:
    def __init__(self, user_name, password, first, last, tier='standard'): #__init__ built in, preferred initializer method for object
        self.user_name = user_name
        self.password = password
        self.first = first
        self.last = last
        self.name = first + " " + last
        self.__tier = tier

    def get_user_name(self):
        return self.user_name

    def get_first(self):
        return self.first

    def get_last(self):
        return self.last

    def get_name(self):
        return self.name

    def get_password(self):
        return self.password

    #will be either 'standard' or 'plus'
    def get_tier(self):
        return self.__tier

