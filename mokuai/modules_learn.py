"""
时间
"""
import time

# print(int(time.time()))  # 时间戳，自1970年1月1日0点0分0秒 距离现在的秒数

# print(time.strftime("%Y-%m-%d %H:%M:%S %A"))  时间格式化

# print(time.localtime())   # 元组

# 让程序休眠暂停
# print('111')
# time.sleep(3)
# print('222')


"""
时间模块 time的封装
"""

import datetime

# print(datetime.date.today()) #取当日的日期

# today = datetime.date.today()
# one_day = datetime.timedelta(days=1)  # 设置时间间隔
#
# # 昨天
# print(today - one_day)
#
# # 明天
# print(today + one_day)


"""
随机数模块
"""
import random

# print(random.randint(1, 23)) # 取范围内的随机整数

# print(random.random()) # 取0-1的随机浮点数

# print(random.choice('swkvjwc,sdw'))  # 随机取字符串中的一个字符


"""
os模块
"""
import os

# print(os.name)   # 系统名字，win：nt  linux/unix:posix

print(os.getcwd())  # 获取当前路径

# print(os.listdir()) # 获取当前路径下的文件

# os.chdir("")  # 改变文件夹

# os.mkdir(r"C:\Users\JS-WL\PycharmProjects\LearnPy\mokuai\test") # 创建目录

# os.remove(r"C:\Users\JS-WL\PycharmProjects\LearnPy\mokuai\test")  # 删除目录

# os.path.exists(r"C:\Users\JS-WL\PycharmProjects\LearnPy\test")  # 判断文件是否存在 ，返回值是布尔类型

"""
sys模块、re模块、math模块
"""

import sys
import re
import math

# print(math.ceil(17.1)) # 返回大于当前数值的正整数

# print(math.pow(2, 3))  # 求指数 2的三次方

# print(math.pi)  # 圆周率

# print(math.sqrt(81)) # 求平方根

# print(math.fabs(-10)) # 求绝对值

