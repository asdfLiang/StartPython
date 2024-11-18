# 修改列表
list4 = []
list4.append(0)
print(f"通过append添加数据: {list4}")
list5 = [1, 2, 3]
list4.extend(list5)
print(f"通过extend添加数据：{list4}")
list4.insert(4, 5)
list4.insert(-1, 4)
print(f"通过insert添加数据：{list4}")
list4[0:0] = [-1]
print(f"使用切片添加数据：{list4}")
list4[0:4] = [0, 1, 2]
print(f"使用切片替换数据：{list4}")
print(f"使用+号拼接数组：{list4 + [6]}")
