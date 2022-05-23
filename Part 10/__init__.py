''''''
import json

'''练习10-1 Python文件读取'''
# file_name = 'E:\\Code\\python\\a byte of python\\Part 10-1\\python.txt'
# with open(file_name) as file_object:
#     contents = file_object.read()
# print(contents)
# print("-----------------------------")
# with open(file_name) as file_object:
#     for line in file_object:
#         print(line.strip())
# print("-----------------------------")
# with open(file_name) as file_object:
#     lines = file_object.readlines()
#     for line in lines:
#         print(line.strip())

'''练习10-2 c语言学习笔记'''
# file_name = 'E:\\Code\\python\\a byte of python\\Part 10-1\\python.txt'
# with open(file_name) as file_object:
#     for line in file_object:
#         new_line = line.replace('Python','C')
#         #print(line.strip().replace('Python', 'C'))
#         print(new_line.strip())

'''练习10-3 访客'''
# file_name = 'E:\\Code\\python\\a byte of python\\Part 10-1\\guest'
# name = input("请您输入自己的名字:\n")
# with open(file_name, 'w') as file_object:
#     file_object.write(name)

'''练习10-4 访客名单'''
# file_name = 'E:\\Code\\python\\a byte of python\\Part 10-1\\guest_book.txt'
# flag = True
# while flag:
#     name = input("尊敬的客人 请您输入自己的姓名(输入q退出):\n")
#     if name == 'q':
#         flag = False
#         print("您已经退出！")
#         break
#     else:
#         with open(file_name, 'a') as file_object:
#             file_object.write(f"欢迎{name}来访！\n")

'''练习10-5 调查'''
# file_name = 'E:\\Code\\python\\a byte of python\\Part 10-1\\answer.txt'
# flag = True
#
# while flag:
#     answer = input("请说出你为什么喜欢编程(按q可以退出): \n")
#     if answer=='q':
#         flag=False
#         print("谢谢您的配合")
#         break
#     else:
#         with open(file_name,'a') as file_object:
#             file_object.write(answer+"\n")

'''练习10-6 加法运算'''
# print("请输入两个数字，我将计算他们的和")
# first_num = input("请输入第一个数: ")
# second_num = input("请输入第二个数: ")
# try:
#     first = int(first_num)
#     second = int(second_num)
# except ValueError:
#     print("你输入的不是整数！")
# else:
#     answer = first + second
#     print("最后结果是： " + str(answer))


'''练习10-7 加法计算器'''
# print("请输入两个数字，我将计算他们的和")
#
# while True:
#     first_num = input("请输入第一个数: ")
#     if first_num == 'q':
#         break
#     second_num = input("请输入第二个数: ")
#     if second_num == 'q':
#         break
#
#     try:
#         first = int(first_num)
#         second = int(second_num)
#     except ValueError:
#         print("你输入的不是整数！")
#     else:
#         answer = first + second
#         print("最后结果是： " + str(answer))

'''练习10-8 猫和狗'''

# def read_file(name):
#     try:
#         with open(name, encoding="utf-8") as file_object:
#             # lines = file_object.readlines()
#             # for line in lines:
#             #     print("猫猫的名字是: " + line.strip())
#             line = file_object.read()
#             print(line)
#     except FileNotFoundError:
#         #print("没有找到你所说的文件哦！")
#         pass
#
#
# read_file('cats.txt')
# read_file('dog.txt')

# while True:
#     file_name = input("请输入要查找的文件名: ")
#     read_file(file_name)
#     if file_name == 'q':
#         break

'''练习10-10-1 常见单词'''
# file_name = 'test.txt'
# with open(file_name) as file_object:
#     lines = file_object.read()
#     print(lines.lower().count('the '))

'''练习10-11 喜欢的数'''
# number = input("请输入你喜欢的数字")
# file_name = 'number.json'
# with open(file_name, 'w') as f:
#     json.dump(number, f)
# with open(file_name, 'r') as f:
#     number = json.load(f)
#     print("最喜欢的就是" + number)

'''练习10-12'''

# def get_favorite_number():
#     try:
#         file_name = 'favorite_number.json'
#         with open(file_name) as f:
#             favorite_number = json.load(f)
#
#     except FileNotFoundError:
#         favorite_number = input("请输入你最喜欢的数字")
#         file_name = 'favorite_number.json'
#         with open(file_name, 'w') as f:
#             json.dump(favorite_number, f)
#         print("我会记得你的数字的！")
#     else:
#         print("我知道你最爱的数字是" + favorite_number)
#
#
# get_favorite_number()

'''练习10-13 验证用户'''
import json


def get_stored_username():
    file_name = 'username.json'
    try:
        with open(file_name) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    file_name = 'username.json'
    username = input("请输入你的名字")
    with open(file_name,'w', encoding='gbk') as f:
        json.dump(username, f)
    return username


def greet_user():
    username = get_stored_username()
    if username:
        answer = input("请判断你的名字是否正确！" + username)
        if answer == 'y':
            print("欢迎" + username + "回来！")
        if answer == 'n':
            username = get_new_username();
            print("欢迎" + username + "回来！")
    else:
        username = get_new_username()
        print("欢迎" + username + "回来！")


greet_user()
