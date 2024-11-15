list0 = list(range(10))

list0.remove(1)
print(f"使用delete删除元素：{list0}")
list0.pop(1)
print(f"使用pop删除元素：{list0}")
del list0[1]
print(f"使用del删除元素：{list0}")
list0.clear()
print(f"使用clear清空元素：{list0}")
