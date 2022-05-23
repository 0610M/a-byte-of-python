import printing_functions as pf
from one_function import make_car
#import one_function
from one_function import make_car
from one_function import make_car as mc
import one_function as of
from one_function import *
'''消息'''

# def display_message():
#     print("这章我在学函数")
#
#
# display_message()

'''喜欢的图书'''

# def favorite_book(title):
#     print("我最喜欢%s这本书" % title)
#
#
# favorite_book("三体")

'''练习8-3 T恤'''

# def make_shirt(size, code):
#     print("我穿的是一件%s码的衣服，印着%s" % (size, code))
#
#
# make_shirt(size='M', code='你今天好帅')
#
# '''练习8-4 大号体恤'''
#
#
# def make_shirt(size='L', code='I love python'):
#     print("我穿的是一件%s码的衣服，印着%s" % (size, code))
#
#
# make_shirt()
# make_shirt(size='M')
# make_shirt(code='huhua')

'''练习8-5：城市'''

# def describe_city(city, country='china'):  # 没指定默认值的放在前面
#     print("%s is in %s" % (city, country))
#
#
# describe_city('shanxi')
# describe_city('harbin')
# describe_city('washton', 'America')

'''练习8-6：城市名'''

# def city_country(city, country):
#     message = city.title() + "," + country.title()
#     return message
#
#
# print(city_country('shanxi', 'china'))

'''专辑'''

# albums = []
#
# def make_album(singer, name, number=''):
#     album = {'singer_name': singer, 'sing_name': name}
#     albums.append(album)
#     if number:
#         album['nums'] = number
#     return albums
#
# while True:
#     print("请输入歌手和专辑名，输入q退出")
#     singer = input("singer:")
#     if singer == 'q':
#         break
#     name = input("album_name:")
#     make_album(singer, name)
#     if name == 'q':
#         break

# print(albums)
# singer1 = make_album('李荣浩', '年少有为', 10-1)
# print(singer1)
# singer2 = make_album('周杰伦', '稻香')
# print(singer2)
# singer3 = make_album('薛之谦', '认真的雪')
# print(singer3)

'''练习8-9'''
txt_list = ['你好呀', '今天开心吗', '每一天都要开心喔']
sent_messages = []


def show_messages(print_list):
    for list in print_list:
        print(list)


def send_messages(print_list, sent_messages):
    while print_list:
        new_list = print_list.pop()
        print("传到了" + new_list)
        sent_messages.append(new_list)


show_messages(txt_list)
send_messages(txt_list[:], sent_messages)  # 传副本

print(txt_list)
print(sent_messages)

'''练习8-12 三明治'''


def add(*food_list):
    for i in food_list:
        print("三明治里加的是这个%s" % i)


add('汉堡包', '三明治', '火腿')

'''练习8-13 用户简介'''


def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user_profile = build_profile('linlin', 'ma', location='taiyuan', field='chinese', habit='reading')
print(user_profile)

'''练习8-14 汽车'''


def make_car(boss, num, **car_info):
    car_info['boss'] = boss
    car_info['num'] = num
    for k, v in car_info.items():
        car_info[k] = v

    return car_info


car = make_car('subaru', 'outback', color='blue', tow_package='True')
print(car)

'''练习8-15 打印模型'''

unprinted_designs = ['mamama','huhuhu','hshshs']
completed_models = []
pf.print_model(unprinted_designs[:],completed_models)
pf.x_models(completed_models)

'''练习8-16 导入'''
#one_function.make_car('subaru', 'outback', color='blue', tow_package='True')
make_car('subaru', 'outback', color='blue', tow_package='True')
