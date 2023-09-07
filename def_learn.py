# def speak():
#     print("听到请回答~~")
#     print("收到，Over!")
#
# # speak()
# # speak()
#
# # 也可以用循环调用函数
#
# for i in range(2):
#     speak()

# def speak(name,voice):
#     print("{}发出了{}的声音".format(name,voice))
#
# speak("小狗","汪汪")


# def compare(num1, num2):
#     if num1 > num2:
#         print("{}大于{}".format(num1, num2))
#     elif num1 == num2:
#         print("{}等于{}".format(num1, num2))
#     else:
#         print("{}小于{}".format(num1, num2))
#
#
# compare(3, 2)

# 形参和实参 上面代码中的num1和num2为形参，3和2即为实参

# 以下是一个数字相加的函数
# def sum_and_cheng(a, b):
#     return a + b, a * b
#
#
# num1, num2 = sum_and_cheng(1, 2)
# print(num1,num2)
# print(num2)

# def speak():
#     return "miaomiaomiao" # 当程序执行到return的时候 代码就停止了
#     print("aaa")
#
#
# a = speak()
# print(a)


# 递归函数
# def recursion(n):
#     print(n)
#     print("------")
#     if n == 10:
#         return
#     recursion(n + 1)
#
# recursion(1)

# 默认参数用=赋值，默认参数放在后面
# def say(message, time=1):
#     print(message * time)
#
#
# say("hello")
#
# say("hello ", 5)

# 关键字参数
# def func(var1, var2=10, var3=20):
#     print("var1 is", var1, ",var2 is", var2, "and var3 is", var3)
#
#
# func(5)
# func(5, var2=20, var3=30)
# func(5, var2=30)
# func(5, var3=10)
# func(var3=10, var2=33, var1=78)

# 函数内部定义的变量，函数外部无法使用
#
# def func():
#     x = 20
#     print("x is", x)
#
# func()
# print("x is", x)

# 函数外部定义的变量，函数内部也可以使用
# x = 20
#
#
# def func():
#     print("x is", x)
#
#
# func()

# x = 50
#
#
# def func(x):
#     print("x is", x)
#     x = 20
#     print("change x to", x)
#
#
# func(x)
# print("x is still", x)

# 全局变量关键字，global

x = 50


def func():
    global x
    print("x is", x)
    x = 20
    print("change x to", x)


func()
print("x is still", x)