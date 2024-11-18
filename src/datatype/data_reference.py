"""
    数据引用
"""

# 基本数值类型初始值相同时，地址相同
a = 10
b = 10
print(id(a) == id(b))

# 列表类型直接赋值，地址相同
list1 = [1, 2, 3]
list2 = list1
list1.append(4)
print(id(list1) == id(list2))

# 列表类型初始化为相同初值，地址不同
list3 = [1, 2, 3]
list4 = [1, 2, 3]
print(id(list3) == id(list4))
