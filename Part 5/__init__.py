# alien_color = 'yellow' #'yellow','red'
# if 'green' in alien_color :
# #print("恭喜你，获得了5分！")
#     print("恭喜你，获得了5分！")
# elif 'yellow' in alien_color:
#     print("你获得了10分！")
# else:
#     print("你获得了15分！")

#人生的不同阶段
# age=4
# if age < 2 :
#     print("你还是幼儿呢！")
# elif age<4:
#     print("儿童啦")
# elif age<13:
#     print("青少年咯")
# elif age<20:
#     print("成年人")
# else:
#     print("你是老年人了")

# favorite_fruits=['apple','banana','orange']
# if 'apple' in favorite_fruits:
#     print(f"You really like apple!")
from pyasn1.compat.octets import null

# user_name=[]
# if len(user_name)==0:
#     print("we need to find some people")
# else:
#     for u_name in user_name:
#         if u_name=='admin':
#            print("Hello admin,would you like to see a status report?")
#         else:
#            print(f"Hello {u_name},thank you for logging in again")

# current_users = ['halo','gugui','FEFE','ses','ere']
# current_users_pro=[current_user.lower() for current_user in current_users]
# print(current_users_pro)
# new_users=['Halo','fefe','wew','rrt','rtrtr']
# for new_user in new_users:
#     if new_user.lower() in current_users_pro:
#         print("%s 已经被占用啦！"% new_user)
#     else:
#         print("%s 还没有人用过欧！" % new_user)

num_list=[1,2,3,4,5,6,7,8,9]
for i in num_list:
    if i == 1:
        print("1st")
    elif i == 2:
        print("2nd")
    elif i == 3:
        print("3rd")
    else:
        print("%dth" % i)
car = 'hallo'
print(car == 'hallo')
