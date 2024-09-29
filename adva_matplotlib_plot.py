import numpy as np
import matplotlib.pyplot as plt

# 创建一个x值的数组，从2pi到2pi，步长为0.01
x = np.arange(-2 * np.pi, 2 * np.pi, 0.01)

# 计算每个x值对应的sin(x)值
y = np.sin(x)

# 使用 matplotlib 绘图
plt.figure()  # 创建一个新图像窗口
plt.title("sin(x) diagram")  # 标题

plt.plot(x, y)  # 折线图
plt.xlabel("x")  # x轴标签
plt.ylabel("sin(x)")  # y轴标签
plt.grid(True)  # 显示网格

plt.show()  # 显示图像
