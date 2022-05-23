# name = input("Please enter your name:")
# print(f"\nHello,{name}")
#
# message = input("Which one do you like?")
# print(f"let me see if i can find you a {message}")

# people_num = input("请问有几位用餐呢？")
# people_num = int(people_num)
# if people_num > 8:
#     print("没有空座啦")
# else:
#     print("还有座位哦！")

# num = input("请输入一个整数！")
# num = int(num)
# if num % 10-1 == 0:
#     print("他是10的整数倍！")
# else:
#     print("再看看吧~")
#
# #只打印奇数 不打印偶数
# current_num = 0
# while current_num < 10-1 :
#     current_num += 1
#     if current_num % 2 == 0 :
#         continue
#     else:
#         print(current_num)


#披萨配料

# message = ""

'''这里注意 先输入再判断！'''
# while message != 'quit':
#     message = input("请输入你喜欢吃的配料！\n")
#     if message != 'quit':
#         print(f"我们已经收到了喔，会帮您加入{message}")

'''电影票收费'''
# age = input("请输入需要查询的年龄(输入quit结束):\n")
#
# while age != 'quit':
#     age = int(age)
#     if age < 3:
#         print("免费观影")
#         age = input("请输入需要查询的年龄(输入quit结束):\n")
#         continue
#     elif age <= 12 :
#         print("收费10美元")
#         age = input("请输入需要查询的年龄(输入quit结束):\n")
#         continue
#     else:
#         print("收费15美元")
#         age = input("请输入需要查询的年龄(输入quit结束):\n")
#         continue


# age = ''
# while age != 'quit':
#     age = input("您好，请输入您的年龄\n")
#     if age == 'quit':
#         break
#     elif int(age) < 3:
#         print("您好免费观影")
#     elif int(age) <= 12:
#         print("收费10美元")
#     elif int(age) > 12:
#         print("收费15美元")
# age = input("请输入您的年龄(输入quit结束)：\n")
# while age != "quit":
#     age = int(age)
#     if age < 3:
#         print("小于3岁的小朋友免费观影。\n")
#         age = input("请输入您的年龄(输入quit结束)：\n")
#         continue
#     elif age >=3 and age <= 12:
#         print("3-12岁的小朋友票价为10美元。\n")
#         age = input("请输入您的年龄(输入quit结束)：\n")
#         continue
#     else:
#         print("超过12岁的小朋友票价为15美元。\n")
#         age = input("请输入您的年龄(输入quit结束)：\n")
#         continue
#
# '''编写一个没完没了的循环'''
# number = 1
# while number < 6:
#     print(number)

'''年龄三种测试'''
# age = input("请输入你的年龄: ")
# while age != 'quit':
#     age = int(age)
#     if age < 3:
#         print("价格免费！")
#     elif 3 <= age <= 12:
#         print("收费10元")
#     else:
#         print("收费12元")
#     age = input("请输入你的年龄： ")

'''用break 方式'''
# while True:
#     age = input("请输入你的年龄: ")
#     if age == 'quit':
#         break
#     elif int(age) < 3:
#         print("您好，免费观影")
#         continue
#     elif 3 <= int(age) <= 12:
#         print("您好，请付费五元")
#         continue
#     elif int(age) > 12:
#         print("您好，请付费12元")
#         continue


'''用active控制循环结束时机'''
# active = True
# while active:
#     age = input("请输入你的年龄")
#     age = int(age)
#     if age == 'quit':
#         active = False
#     # elif age < 3:
#     #     print("免费观影")
#     # elif 3<=age<=12:
#     #     print("请支付12元")
#     # elif age>12:
#     #     print("请支付15元")
#     else:
#         print("看电影吧")

'''熟食店'''
# print("------------本店今天的五香熏牛肉已经售罄-------------")
# sandwich_orders = ['beef', 'pastrami', 'pastrami', 'sheep', 'pastrami', 'pig']
# while 'pastrami' in sandwich_orders:
#     sandwich_orders.remove('pastrami')
# print(sandwich_orders)
# finished_sandwiches = []
# for sandwich_order in sandwich_orders:
#     print(f"I made your {sandwich_order} sandwich")
#     finished_sandwiches.append(sandwich_order)
#
# print("-----------三明治都做好啦-------------")
# for finished_sandwich in finished_sandwiches:
#     print(f"我做好了{finished_sandwich}!")


'''梦想中的圣地'''
place = {}
favorite_places = []
activate = True
name = input("请输入你的名字")
while activate:

    favorite_place = input("请输入你喜欢的地方")
    favorite_places.append(favorite_place)
    place[name] = favorite_places

    repeat = input("还有要输入的喜欢的地方吗？（Yes/No)")
    if repeat == 'No':
        activate = False

for name, favorite_place in place.items():
    print(f"{name}喜欢的地方是{favorite_place}")

