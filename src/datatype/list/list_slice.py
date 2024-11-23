# 列表切片

list2 = [i for i in range(0, 10)]

print(list2)
print(list2[:5])
print(list2[0:5])

print(list2[-2:])
print(list2[:-2])

print(list2[::-1])
print(list2[0:10:2])
print(list2[0:10:2])

print(list2[-1:3])
print(list2[-1:3:-1])  # 步长可以控制方向，-数表示从后向前
print(list2[0:1000])  # 可以超出范围
