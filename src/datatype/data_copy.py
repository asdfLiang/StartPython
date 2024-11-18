import copy

"""
    数据的拷贝
"""

a = [1, 2, 3, 4, 5]
a_copy = copy.copy(a)
a_deep_copy = copy.deepcopy(a)
print("列表a浅拷贝地址比较：", id(a) == id(a_copy))
print("列表a深拷贝地址比较：", id(a) == id(a_deep_copy))

print("###############################################################")

b = [{"name": "alice", "age": 10}, {"name": "bob", "age": 20}]
b_copy = copy.copy(b)
b_deep_copy = copy.deepcopy(b)
print("列表b浅拷贝后元素0地址比较：", b[0] == b_copy[0])
print("列表b深拷贝后元素0地址比较：", b[0] == b_deep_copy[0])
b[0]["age"] = 11
print("列表b浅拷贝后，进行修改，元素0地址比较：", b[0] == b_copy[0])
print("列表b深拷贝后，进行修改，元素0地址比较：", b[0] == b_deep_copy[0])
print("列表b浅拷贝后，进行修改，元素1地址比较：", b[1] == b_copy[1])
print("列表b深拷贝后，进行修改，元素1地址比较：", b[1] == b_deep_copy[1])
