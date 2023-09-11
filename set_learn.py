# 集合（set）是一个无序的 不重复 元素序列
# 集合的定义方法
# a = set() #空集合
# a = {"a", "b"}   #有数据的时候定义

# 集合会把重复的值去掉
# set = {'a', 'a'}
# print(set)

# a = {'a', 'b'}
# in 和 not in
# print(a)
# print('a' in a)
# print('c' not in a)

# 将字符串转成集合 用set()
# a = "abc"
# print(set(a))
# print(type(set(a)))

# 将数组转成集合用set()  会去重
# list = ['a', 'c', 'b', 'c']
# print(set(list))

a = {'a', 'c', 'b'}
b = {'a', 'd'}
# a-b  集合a中包含，集合b中不包含的元素
# print(a-b)

# a | b 取并集
# print(a|b)

# a & b 取交集
# print(a & b)

# a ^ b 不同时包含于a 和 b的元素
# print(a ^ b)

# 集合的方法
# add()  添加
# a.add('e')
# print(a)

# update 添加  添加集合
# a.update({'g', 'f', 'c'})
# print(a)

# remove() 移除单个元素
# a.remove('a')
# print(a)

# clear 移除所有的元素
# a.clear()
# print(a)

# len()
# print(len(a))

# intersection() 取交集
# print(a.intersection(b))

# union() 取并集
# print(a.union(b))

#