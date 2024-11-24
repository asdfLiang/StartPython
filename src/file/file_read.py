"""
    文件读取
"""

# 第一种读取方式：手动读取
f = open("resources/training_log.txt", "r")
try:
    print(f.read())
finally:
    f.close()


# 第二种读取方式：with...as...，自动捕获异常、关闭流
with open("resources/training_log.txt", "r") as file:
    content = file.read()
    print(content)

print("############################################################")

# 读取一行
with open("resources/training_log.txt", "r") as file:
    line = file.readline()
    print(line)

print("############################################################")

# 读取所有行
with open("resources/training_log.txt", "r") as file:
    lines = file.readlines()
    print(type(lines))
