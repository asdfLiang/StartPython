import random

list0 = [random.randint(0, 100) for _ in range(10)]
print(f"全部元素：{list0}")
sorted(list0)
print(f"临时排序：{list0}")
list0.sort()
print(f"永久排序：{list0}")
