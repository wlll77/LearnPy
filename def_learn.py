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


def compare(num1, num2):
    if num1 > num2:
        print("{}大于{}".format(num1, num2))
    elif num1 == num2:
        print("{}等于{}".format(num1, num2))
    else:
        print("{}小于{}".format(num1, num2))


compare(3, 3)
