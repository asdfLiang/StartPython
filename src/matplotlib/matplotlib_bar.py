import numpy as np
import matplotlib.pyplot as plt

"""
    柱状图
"""

# 数据
labels = ["A", "B", "C", "D", "E"]
values = [3, 7, 2, 5, 8]

# 设置标签的位置
x = np.arange(len(labels))


# 柱状图
plt.bar(x, values, color="blue", align="center", alpha=0.7)
plt.title("Simple Bar Chart")

# 轴标签
plt.xlabel("Labels")
plt.ylabel("Values")

# x轴的标签
plt.xticks(x, labels)

plt.show()
