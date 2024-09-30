import random

"""
    list
"""
print(
    "/**************************************** list ****************************************/"
)

# 列表创建
print("================ init ================")
list1 = [1, 2, 3, 4, 4, 5]
list2 = [i for i in range(0, 10)]
print(f"{list1}")
print(f"{list2}")

# 列表打印
print("================ print ================")
list3 = ["alice", "bob", "cod", "devid"]
print("原始列表：", list3)

# 列表添加元素
print("================ add ================")
list3.append("tail")
list3.insert(0, "head")
print("在头部插入head, 尾部插入tail：", list3)

# 列表删除元素
print("================ del ================")
list3.pop(2)
del list3[0]
print("删除第0、第2个元素：", list3)

# 列表排序
print("================ sort ================")
list4 = [random.randint(0, 10) for i in range(10)]
print("原始列表：", list4)
sorted(list4)  # 临时排序
print("临时排序：", list4)
list4.sort()  # 永久排序
print("永久排序：", list4)

# 列表子集获取
print("================ subList ================")
print(list2)
print(list2[:5])
print(list2[0:5])

print(list2[-2:])
print(list2[:-2])

print(list2[::-1])
print(list2[0:10:2])
print(list2[0:10:2])


"""
    set
"""
print(
    "/**************************************** set ****************************************/"
)
set1 = set(list1)
set2 = {1, 2, 3, 4, 4, 6}

print(f"set1 = {set1}")
print(f"set2 = {set2}")
