# 读取文件
with open("resources/training_log.txt", "r") as file:
    print(file.read())

print("==========================================================")
# 按行读取文件
with open("resources/training_log.txt", "r") as file:
    print(file.readline())
    print(file.readline())
    print(file.readline())

# 写入，多次执行不会追加内容，而是覆盖
with open("resources/example_1.txt", "w") as file:
    file.write("Hello World!")

# 写入多行，多次写入不会追加内容，而是覆盖
lines = ["Hello World!", "Welcome to Python programming"]
with open("resources/example_2.txt", "w") as file:
    file.writelines(line + "\n" for line in lines)
