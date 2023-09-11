# 切片
# 操作基本表达式：object[start_index:end_index:step]
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
b = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
c = '0,1,2,3,4,5,6,7,8,9'


print(a[0:1:1])
print(a[0:1])

print(b[0:1:1])
print(c[0:1:1])

# 只有一个冒号的时候，step默认是1
print(a[0:5])

print(a[0:5:2])

# 当没有冒号的时候，start_index = end_index 即切取指定的start_index  即索引 = 下标
print(a[1])

# 当没有start_index 默认从端点取值
print(a[:3])

# 当没有end_index 默认取端点值
print(a[3:])
print(a[1::3])

print(a[::-1])


print(a[-1:-6:-1])

# 取偶数
print(a[::2])

# 取奇数
print(a[1::2])

# 可以多个切片一起用
print(a[0:6][::-1])