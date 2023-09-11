# 字典和数组表现形式的区别
# 一个学生的成绩，语文90 数学80 英语92

# subjects = ["语文", "数学", "英语"]
# scores = [90, 80, 92]
#
# for i in range(len(subjects)):
#     print("{}的成绩是{}分".format(subjects[i], scores[i]))

# 用字典表示学生成绩 key:value 多个元素用,隔开
info = {"语文": 90, "数学": 80, "英语": 92}
# print(type(info))
# print(info)

# key,value的类型要求
# key 一般是字符串和数字； value 支持任意python支持的数据结构
# dict1 = {1:[1, 2, 3]}
# print(type(dict1))

# 在一个字典里key不可以重复
# info_ = {"语文": 90, "数学": 80, "英语": 92, "语文": 90}
# print(info_)

# 如何获取字典里面的内容：用变量[key]   如果key不存在，报key error
# print(info['语文'])

# 往字典中添加数据: 变量[key] = value
# info['物理'] = 88
# print(info)

# 修改字典中的数据：变量[key] = value
# info['语文'] = 35
# print(info)

# 删除字典中的数据 del 变量[key]
# del info['语文']
# print(info)

# 清空字典
# info.clear()
# print(info)

"""
字典的常用函数
"""

# len(info) 获取长度

# 将字典转换为字符串
# print(type(str(info)))

# in和not in 判断一个key是否在字典中
# print('语文' in info)
# print('语文' not in info)

# items() 遍历字典
# for i in info.items():    #一个变量获取的是tuple类型
#     print(i)
#
# for i,j in info.items():  #两个变量获取的是key,value
#     print(i, "--", j)
#
# for i in info.items():
#     print(i[0], "--", i[1])  #这样也能获取到key，value，i出来后是元组，元组再获取数据

# keys():遍历key，用list()转换成数组
# print(info.keys())
# print(list(info.keys()))

# value():遍历value，用list()转换成数组
# print(info.values())
# print(list(info.values()))

# pop(key)：删除键值对，返回整个key的value
# print(info.pop("语文"))
# print(info)

# 数组list中可以放字典
# info_list = [{"语文": 90, "数学": 80, "英语": 92}, {"语文": 20, "数学": 50, "英语": 72}]
# print(info_list[1])
# print(info_list[1]["语文"])


"""
题目：实现购物车功能。程序运行后让购物车输入水果的编号，然后让购物车内水果数量增加
"""
items = {1: "苹果", 2: "香蕉", 3: "芒果"}
items_keys = list(items.keys())
shopcart = {"苹果": 0, "香蕉": 0, "芒果": 0}

while True:
    print("当前购物车内： ", str(shopcart))
    num = int(input("请选择你要做什么，购物输入1，退出程序输入2： "))
    if num == 1:
        while True:
            print(str(items))
            choose_num = int(input("请选择商品的号码："))
            if choose_num not in items_keys:
                print("商品号码不存在，请重新选择~")
                continue
            else:
                shopcart[items[choose_num]] += 1
                num = int(input("继续购物请按1，退出请按2："))
                if num == 1:
                    continue
                else:
                    break
    elif num == 2:
        print("程序已退出")
        break
    else:
        print("输入错误，请重新选择： ")
        continue






