"""
    文件读取
"""

# 读取全部
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
