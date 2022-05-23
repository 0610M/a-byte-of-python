''''''

'''练习9-14 彩票'''
from random import *

ticket_nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e']
numbers = sample(ticket_nums, k=4)
print("中奖号码是" + str(numbers))

i = 1
while True:
    my_ticket = sample(ticket_nums, k=4)
    if my_ticket != numbers:
        i += 1
        continue
    else:
        print("第" + str(i) + "次才中奖！")
        break
