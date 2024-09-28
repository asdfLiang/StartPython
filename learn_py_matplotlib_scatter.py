import random
import numpy as np
import matplotlib.pyplot as plt

# 点坐标
num_points = 100
x = np.random.rand(num_points)  # x坐标
y = np.random.rand(num_points)  # y坐标

# 点样式
colors = np.random.rand(num_points)  # 点的颜色
sizes = 1000 * np.random.random(num_points)  # 点的大小
alphas = np.random.rand(num_points)  # 点的透明度

# 散点图
plt.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap="viridis")
plt.colorbar()  # 颜色条

plt.show()
