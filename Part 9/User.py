''''''

'''练习9-3 用户'''


class User:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = str(age)  # 转成字符串 字符串只能拼接字符串
        self.login_attempts = 0

    def describle_user(self):
        print("用户的名字是：" + self.last_name + " " + self.first_name)
        print("用户的年龄是：" + self.age)

    def greet_user(self):
        print("尊敬的" + self.last_name + self.first_name + "您好！")

    def increment__login_attempts(self, number):
        self.login_attempts += number
        print(f"登录次数为：{self.login_attempts}")

    def reset_login_attempts(self):
        self.login_attempts = 0
        print(f"登录次数已重置为{self.login_attempts}次")



# user1 = User('lin', 'ma', 24)
# user1.describle_user()
# user1.greet_user()
# Admin = Admin('lin', 'li', 23)
# Admin.privileges.show_privileges()
# print("--------")
# user2 = User('hua', 'li', 13)
# user2.describle_user()
# user2.greet_user()
# print("--------")
# user3 = User('mary', 'wang', 46)
# user3.describle_user()
# user3.greet_user()
# user3.increment__login_attempts(1)
# user3.increment__login_attempts(1)
# user3.increment__login_attempts(1)
# print("----------")
# user3.reset_login_attempts()
# print(user3.login_attempts)
