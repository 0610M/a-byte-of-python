''''''
from User import User #要把类导入进来


class Admin(User):
    def __init__(self, first_name, last_name, age):
        super().__init__(first_name, last_name, age)
        self.privileges = Privileges()


class Privileges():
    def __init__(self):
        privileges = ['can add post', 'can delete post', 'can ban user']
        self.privileges = privileges

    def show_privileges(self):
        for i in self.privileges:
            print("管理员有" + i + "权限")
