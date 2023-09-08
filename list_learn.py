# 定义数组 [] , 多个值用,隔开
# 取数组中的数据，下标从0开始
# for循环取数组中的数据

names = ['小红', '小美', '小黄']

# print(names[0])
# print("-------")
#
# for name in names:
#     print(name)

# 获取数组的长度/数量 len
# n = len(names)
# print(n)
#
# for i in range(len(names)):
#     print(i, " ", end='')
#     print(names[i])
#     print()

# 数组替换 数组变量名[0]=值
# names[2] = "小明"
# print(names)

# 数组元素删除
# del names[1]
# print(names)

# 数组中存放哪些数据类型,python支持的数据类型

user_info = ['wl', 28, 80.8, ['公司', 5, 200]]
# print(user_info)
# for i in user_info:
#     print(i)

# 查看数据的类型 type()
# print(type(user_info[3][0]))

# 数组的操作运算符
# 数组相加,用+进行数组组合
a = ['a', 'b', 'c']
b = ['d', 'e', 'f']
# c = a + b
# d = b + a
# print(c)
# print(d)

# 数组相乘，只支持一个数组和一个int型进行组合
# print(a * 4)

# 判断一个元素是否在数组中 in ，返回布尔值
# c = 'd' in a
# d = ['公司', 5, 200] in user_info
# print(d)

# append 在数组的最后增加一个对象

# names.append('小花')
# names.append('小白')

# extend 增加一个可以循环的元素，数组直接加到目标数组里了
name_ex = ['小光', '小兰']
# names.extend(name_ex)
# print(names)


# clear 清空列表
# names.clear()

# copy 复制一个数组 等同于 =
# names_new = names.copy()
# print(names_new)

# count 统计元素在数组中出现的次数
nums = [1, 1, 1, 2, 333, 4, 55, 666, 8, 9, 00, 00, 19, 19, 19]
#
# print(nums.count(3))

# index 返回一个元素在数组中第一次匹配的下标 数据不在数组里面，程序报错
# print(nums.index(4))

# insert 根据位置进行插入，插队
# names.insert(1, '小梅')
# print(names)

# pop 删除元素，参数为下表，返回值为删除的元素 如果下表不存在，程序报错
# names.pop(1)
# print(names)
# print(names.pop(1))

# remove 删除具体的元素,如果元素不存在，程序报错
# names.remove('小黄')
# print(names)

# reverse 反转数组中的值
# nums.reverse()
# print(nums)

# sort 排序,默认是正序;reverse=True的时候是倒序；key
# nums.sort()
# nums.sort(reverse=True)
# print(nums)
# students = [['wang', 'j', 14], ['li', 'a', 19], ['xinbaji', 'x', 22]]
#
#
# def cmp(i):
#     return i[2]
#
#
# students.sort(key=cmp)
# print(students)

# python ord函数 返回英文字母的十进制值
# print(ord('a'))
# print(ord('b'))
# print(ord('c'))
# print(ord('z'))


# max min 数组中的数据类型需要是一致的
print(max(nums))
print(min(nums))
zimu = ['a', 'c', 'd', 'r']
print(max(zimu))
print(min(zimu))