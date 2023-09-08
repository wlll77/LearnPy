# 定义元组 元组与列表类似，不同之处在于元组的元素不能修改
# tuple = () 空元组
# 定义一个参数的元组，需要在结尾加上, 不然就是原始的数据类型
# name = ("carl",)
# print(name)

name = ("david",)
names = ("carl", "mary")
# print(names)

# 如何获取元组，通过下标获取
# print(names[0])

# for循环获取元组的值
# for i in names:
#     print(i)

# 元组的操作
# 元组相加
# name_new = names + name
# print(name_new)

# 删除整个元组：全部删除，连变量名字也删除了
# del name
# print(name)

# 元组的方法
# print(len(names))
# print(names * 3)
# print("carl" in names)
# print("karl" not in names)

# 元组的内置函数
nums =(1, 6, 14, 36)
# max
# print(max(nums))

# min
# print(min(nums))

# list (tuple) 把元组转化为数组
print(list(nums))


