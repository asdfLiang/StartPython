import os

"""
    os 操作系统接口模块，提供了一些方便使用操作系统相关的函数
"""

# 读取环境变量
print("=============== 读取环境变量 ===============")
print(os.getenv("path"))
print()

# 读取路径
print("=============== 读取路径 ===============")
print(os.path.split("src/internal/internal_os.py"))  # 把路径分为：目录路径、文件名
print(os.path.dirname("src/internal/internal_os.py"))  # 目录路径
print(os.path.basename("src/internal/internal_os.py"))  # 文件名
print(os.path.exists("src/internal/internal_os.py"))  # 路径是否存在
print(os.path.isfile("src/internal/internal_os.py"))  # 是否是文件
print(os.path.isdir("src/internal/internal_os.py"))  # 是否是文件夹
print(os.path.abspath("src/internal/internal_os.py"))  # 返回绝对路径
print(os.path.abspath("."))  # 当前路径的绝对路径
print(os.path.abspath("../"))  # 上一层路径的绝对路径
print()
