#while
#不要写死循环

# while True:
#     print("这是while循环")
#     print("------------")

# num1 = 5
# num2 = 10
# while num1 < num2:
#     print("num1 < num2")
#     print("-----------")
#     print("现在的num1是{}".format(num1))
#     num1 += 1

"""
题目：计算1—100之前的数字的和
"""

# sum = 0
# num1 = 1
# while num1 < 101:
#     sum += num1
#     num1 += 1
# print("1-100的数字之和为：{}".format(sum))

# break终止循环
# a = 0
# while True:
#     print("a={}".format(a))
#     a += 1
#     if a == 5:
#         break

# continue 跳出循环

"""
例子：打印1-100能被2整除的数字
"""

# num1 = 1
# while num1 < 101:
#     if num1 % 2 == 0:
#         print("{}能被2整除".format(num1))
#     num1 += 1
#     if num1 % 2 != 0:
#         continue
#     print("被2整除才能运行此行")

"""
题目：随机数1-10，你拥有5次机会去猜这个数字，如果猜对了，打印:你猜对了，5次都猜错了的话，打印: 你的机会用完了
"""
import random
random_num = random.randint(1, 10)
try_num = 5
while try_num >0:
    num = int(input("你还有{}次机会，请输入你的数字：".format(try_num)))
    if random_num == num:
        print("你答对了")
        break
    try_num -= 1
    if try_num == 0:
        print("你的机会用完了")