# class Hero:
#     level = 4
#     def __init__(self, name, blood, price):
#         self.name = name
#         self.blood = blood
#         self.price = price
#
#     def print_hero(self):
#         print("英雄的名字是：", self.name)
#         print("英雄的血量是：", self.blood)
#         print("英雄的金币是：", self.price)
#         print("大招的等级是：", Hero.level)
#
# hero =Hero("小黑子", 365, 300)
# hero.print_hero()


class Hero:
    level = 4
    def __init__(self, name, blood, price):
        self.name = name
        self.blood = blood
        self.price = price
        self.print_hero()

    def print_hero(self):
        print("英雄的名字是：", self.name)
        print("英雄的血量是：", self.blood)
        print("英雄的金币是：", self.price)
        print("大招的等级是：", Hero.level)

hero =Hero("小黑子", 365, 300)