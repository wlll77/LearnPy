# 字符串
# var1 = "hello world"
# print(var1)


# 加法
# var1 = "hello "
# var2 = "world"
# print(var1 + var2)

# 乘法
# print(var1 * 3)

# in 和 not in
# var = "h" in var1
# var3 = "h" not in var1
# print(var)
# print(var3)
# print("{} world".format(var1))

# 格式化
# %d 格式化int型

num = 2
print("我有 %d 只苹果" % num)

# %s 格式化字符串型
# %f 格式化浮点数型

username = "wlll"
years = 26
weight = 80.8
print("我的名字叫 %s，我今年%d岁了，我的体重是%.2fkg" % (username, years, weight))

# capitalize 第一个字母变成大写
# count 统计出现的次数
# endwith 是否以...字符结尾
# startwith 是否以...字符开头
# index 获取从左往右第一个指定字符串的位置
# isalnum 是否是字符串
# isalpha 必须是英文字符
# isdigit 必须是纯数字
# islower 全部小写
# isupper 全部大写
# upper 转大写
# lower 转小写
# replace 替换


print(username.capitalize())
print(username.count("l"))
print(username.endswith("ll"))
print(username.startswith("w"))
print(username.index("l"))
print(username.isalnum())
print(username.isalpha())
print(username.isdigit())
print(username.upper())
message1 = "hahaha,jintian qifei lou!"
print(message1.replace("ha", "he"))
