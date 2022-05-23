''''''

'''练习9-13 骰子'''
from random import randint


class Die:
    def __init__(self,sides=6):
        self.sides = sides

    def roll_die(self):

        for i in range(1, 11):
            number = randint(1, self.sides)
            print("第" + str(i) + "次数字为" + str(number))


die = Die()
die.roll_die()
print("-----")
die1 = Die(10)
die1.roll_die()
print("-----")
die2 = Die(20)
die2.roll_die()
