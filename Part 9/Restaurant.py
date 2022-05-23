'''2022/3/30'''

'''练习9-4：就餐人数'''


class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"餐馆名字是：{self.restaurant_name}")
        print(f"餐馆菜系是：{self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name}开业啦！")

    def num(self):
        print(f"{self.number_served}人就餐")

    def set_number_served(self, number):
        self.number_served = number
        print(f"新增就餐人数{number}")

    def increment_number_served(self, number):
        self.number_served += number
        print(f"现在一共{self.number_served}人聚餐")


class IceCreamStand(Restaurant):
    # 先继承父类方法
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavours = ['apple', 'banana', 'peach']

    def show_flavors(self):
        for i in self.flavours:
            print(f"我们店的冰淇淋有{i}味道的")


# restaurant = Restaurant('好再来', '川菜')
# print(restaurant.restaurant_name)
# print(restaurant.cuisine_type)
# IceCreamStand = IceCreamStand("冰激凌小店", "ice")
# IceCreamStand.show_flavors()
# print("-----")
# restaurant.describe_restaurant()
# print("-----")
# restaurant.open_restaurant()
# print("-----")
# restaurant.num()
# restaurant.set_number_served(12)
# restaurant.increment_number_served(23)

'''练习9-2 三家餐馆'''

# restaurant1 = Restaurant('海底捞', '火锅')
# restaurant1.describe_restaurant()
# print("-----")
# restaurant2 = Restaurant('三晋饭庄', '山西菜')
# restaurant2.describe_restaurant()
# print("-----")
# restaurant3 = Restaurant('东港海逸', '粤菜')
# restaurant3.describe_restaurant()
# print("-----")
#


'''练习'''
