class Person:
    def __init__(self, name, id, email, password):
        self.__name = name
        self.__id = id
        self.__email = email
        self.__password = password
        self.hide_password_condition = False

    def __str__(self):
        return f'name: {self.__name}\tId: {self.__id}\tEmail: {self.__email}\tPassword: {self.__password}'

    def show(self):
        print(f'name: {self.__name}\tId: {self.__id}\tEmail: {self.__email}\tPassword: {self.hide_password()}')

    def login(self, email, password):
        if email == self.__email and password == self.__password:
            print(f'Your information is:')
            print(f'Name: {self.__name}')
            print(f'Id: {self.__id}')
            print(f'Email: {self.__email}')
            print(f'Password: {self.__password}')
        else:
            print('This username and/or password is incorrect.')

    def forget_password(self, email, new_password, new_password_again):
        if email == self.__email and new_password == new_password_again:
            self.__password = new_password
            print(f'Your new information is:')
            print(f'Name: {self.__name}')
            print(f'Id: {self.__id}')
            print(f'Email: {self.__email}')
            print(f'Password: {self.__password}')
            print('Password successfully changed.')
        else:
            print('The entered email and/or passwords do not match.')

    def hide_password(self):
        if self.hide_password_condition:
            return '*' * len(self.__password)
        else:
            return self.__password

    def hide_password_control(self, condition):
        if condition == 'Hide':
            self.hide_password_condition = True
        else:
            self.hide_password_condition = False
    
# ---------------------------------------------
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
# ---------------------------------------------
    @property
    def id(self):
     return self.__id
    @id.setter
    def id(self,id):
        self.__id=id
# ---------------------------------------------

    @property
    def Email(self):
        return self.__email
    @Email.setter
    def Email(self,Email):
        self.__email=Email
# ---------------------------------------------
    @property
    def passowrd(self):
        return self.__Password
    @passowrd.setter
    def password(self,password):
        self.__Password=password
# ---------------------------------------------
