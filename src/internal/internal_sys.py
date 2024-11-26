import sys

"""
    对python解释器系统进行操作
"""


# 命令行参数列表
print(sys.argv)

# 获取当前系统编码
print(sys.getdefaultencoding())

# 返回环境变量路径
print(sys.path)

# 返回当前系统平台
print(sys.platform)

# 查看系统python版本
print(sys.version)
