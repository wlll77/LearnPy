# if
# if True:
#     print("执行此代码")

# if 条件：
#   可以是单行或多行执行语句

# num1 = 10
# num2 = 5
# if num1 > num2:
#     print("num1 > num2")
#     num1 += 1
#     print(num1)

# elif (else if的缩写） 即再如果
# num = int(input("请输入一个数字："))
# if num >= 10:
#     print("{}大于等于10".format(num))
# if num > 9:
#     print("{}大于等于9".format(num))
# elif num >= 5:
#     print("{}大于等于5".format(num))
#
# # else
#
# num = int(input("请输入一个数字："))
# if num > 9:
#     print("{}大于等于9".format(num))
# elif num >= 5:
#     print("{}大于等于5".format(num))
# else:
#     print("{}小于5".format(num))


"""
 题目： 输入数字，判断是周几，如果不是1-7的数字，输出数字错误
"""
# day = int(input("请输入1-7的数字："))
#
# if 1 <= day <= 6:
#     print("今天是星期{}".format(day))
# elif day == 7:
#     print("今天是星期天")
# else:
#     print("输入的数字错误！")

"""
题目：登录验证
"""
username = "admin"
passwd = "123123"

username_input = input("请输入用户名：")
passwd_input = input("请输入密码：")

if username_input == username and passwd_input == passwd:
    print("登录成功")
elif username_input == username and passwd_input != passwd:
    print("密码错误")
elif username_input != username:
    print("用户未注册")
else:
    print("未知错误")