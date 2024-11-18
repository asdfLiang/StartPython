"""
    python3的6种基本数据类型：Number(int, float, complex, bool)、String、List、Set、Dictionary、Tuple
"""

# 数字
intNum = 1234
floatNum = 1234.0
boolNum = True
complexNum = 3 + 4j

print(intNum, f" type is: {type(intNum)}")
print(floatNum, f" type is: {type(floatNum)}")
print(boolNum, f" type is: {type(boolNum)}")
print(complexNum, f" type is: {type(complexNum)}")

# 字符串
string = "12345"
print(string, f" type is: {type(string)}")

# 列表
list0 = [1, 2, 3]
print(list0, f" type is: {type(list0)}")

# 集合
set0 = {1, 2, 3}
print(set0, f" type is: {type(set0)}")

# 字典
dict0 = {1: "a", 2: "b", 3: "c"}
print(dict0, f" type is: {type(dict0)}")

# 元组
tuple0 = (1, 2, 3)
print(tuple0, f" type is: {type(tuple0)}")
