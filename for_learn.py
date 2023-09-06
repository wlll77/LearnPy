# for循环

# username = "lisiyuan"
# for i in username:
#     print(i)

# for i in range(10):
#     print("i的值为{}".format(i))

# range是一个数组
# range(10)  == [0,1,2,3,4,5,6,7,8,9]
# range(1,10) == [1,2,3,4,5,6,7,8,9]
# range(1,10) == [1,3,5,7,9]
# range(10,1,-1) == [10,9,8,7,6,5,4,3,2]
# range(10,1,-2) == [10,8,6,4,2


# break
# for i in range(10):
#     print("i的值为{}".format(i))
#     if i == 3:
#         break

# continue
# for i in range(10):
#     if i < 5 :
#         continue
#     print("i的值为{}".format(i))

"""
题目：打印九九乘法表
"""
for i in range(1,10):
    for j in range(1,i + 1):
        print("{}x{}={} ".format(j, i, i*j), end='')
    print("")