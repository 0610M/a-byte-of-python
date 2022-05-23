# people = {'first_name':'lin','last_name':'ma','age':12,'city':'herbin',}
# print(people['last_name'])
# print(people['first_name'])
# print(people['city'])
# print(people['age'])
#
# nums={'aa':12,
#       'ww':21,
#       'er':34,
#       'tt':45,
#       'yu':89,
#       }
# print(nums)

# py_dicts={
#     'if':'如果',
#     'age':'年龄',
#     'name':'姓名',
#     'min':'最小',
#     'max':'最大',
#     "sort":'排序',
# }
#
# for k,v in py_dicts.items():
    # print("key : "+k)
    # print("value : "+v)
    #print(k + ":" +v)
# print("if:"+py_dicts['if'])
# print("age:"+py_dicts['age'])
# print("name:"+py_dicts['name'])
# print("min:"+py_dicts['min'])
# print("max:"+py_dicts['max'])

'''river'''

# river_list = {
#     'changjiang':'china',
#     'songhuajiang':'heilongjiang',
#     'huanghe':'shanxi',
# }

# for r_name,city in river_list.items():
#     print(f"The {r_name.title()} runs through {city.title()}")
#
# for r_name in river_list.keys():
#     print(r_name)
# for r_name in river_list:
#         print(r_name)

# for city in river_list.values():
#     print(city)

# all_list={
#     'lele':'da',
#     'lili':'erer',
#     'gugu':'ewr'
# }
# people_list=['lili','huahua','gugu']
#
# for i in people_list:
#     if i in all_list:
#         print("感谢 %s 参与调查" % i)
#     else:
#         print("欢迎 %s 参与调查" % i)

#人们
# people_list=[
#     {
#         'fruit':'apple'
#     },
#     {
#         'name':'dada'
#     },
#     {
#         'age':12
#     }
# ]
# for i in people_list:
#     print(i)
#
# pets = [
#     {
#         'name':'wawa',
#         'host':'malinlin'
#     },
#     {
#         'name': 'gugu',
#         'host': 'huihui'
#     }, {
#         'name':'keke',
#         'host':'malin'
#     },
# ],
pets = []
pets.append({'name' : 'jiji','host':'gugu'})
print(pets)
#
# for i in pets:
#     print(i)
#
# favorite_places = {
#     'lili' : ['herbin','shanci','taiyuan'],
#     'lala' : ['shasnfong'],
#     'huhu' : ['qinhuangdao']
# }
# for k,v in favorite_places.items():
#    print("------")
#    print("\n喜欢的地方是：",end="")
#    print(v)

#数字
# nums = {
#     'xiaoming' : [12,11,11],
#     'xiaowang' : [23,33,44]
# }
#
# for name,num in nums.items():
#     print(name+"喜欢的数字是：")
#     print(num)

#城市
cities = {
    'taiyuan' : {
        'country' : 'china',
        'population' : '10000',
        'fact' : '很漂亮!'
    }
}
for city,city_info in cities.items():
    print(f"城市名字叫做:{city}")
    country = city_info['country']
    people_num = city_info['population']
    fact = city_info['fact']
    print(f"\t属于{country}")
    print(f"\t人数有{people_num}")
    print(f"\t值得介绍的特点是：{fact}")

    print(f"城市名字叫做{city}\n\t属于{city_info['country']}\n\t人口{city_info['population']}人\n\t值得介绍的特色是{city_info['fact']}")