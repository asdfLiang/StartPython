# % 形式输出
name = "alice"
age = 20
print("My name is %s, %d years old" % (name, age))

# %f 浮点数
a = 9.123456
print("%f" % a)
print("%.2f" % a)

# 进制输出
a = 10
print("十进制整数：%d" % a)
print("八进制整数：%o" % a)  # a只能是整数
print("十六进制整数：%x" % a)  # a只能是整数

# format
a = "hello"
b = "world"
print("{}, {}".format(a, b))
print("{0}, {1}, {0}".format(a, b))  # 带数字可调换顺序
print("My name is {name}, {age} years old".format(name="bob", age=30))  # 设置参数

# f"{表达式}" 不需要考虑数据类型
print(f"My name is {"Clack"}, {40} years old")
