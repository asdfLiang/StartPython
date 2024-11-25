import re

"""
    匹配单个字符
"""

# 不用符号匹配
print("====> 不使用符号匹配：")
re0 = re.match("liang", "liangzj9624@163.com")
print(re0)
re1 = re.match("zhang", "liangzj9624@163.com")
print(re1)


# 匹配单个字符
print("====> 匹配任意一个字符，不包括换行符：'.'")
re2 = re.match("t.o", "too")
re3 = re.match("t.o", "tiao")
print(re2.group() if re2 else re2)
print(re3.group() if re3 else re3)

print("====> 匹配列举的任意一个字符：'[]'")
re4 = re.match("[Hh]", "hello World")
re5 = re.match("[Hh]", "Hello World")
print(re4.group() if re4 else re4)
print(re5.group() if re5 else re5)

print("====> 匹配数字0-9：")
re6 = re.match("[0123456789]", "7hello World")
re7 = re.match("[0-9]", "8Hello World")
print(re6.group() if re6 else re6)
print(re7.group() if re7 else re7)

print("====> 匹配数字0-9，但不匹配4：")
re8 = re.match("[0-35-9]", "7hello World")
re9 = re.match("[0-35-9]", "4hello World")
print(re8.group() if re8 else re8)
print(re9.group() if re9 else re9)

print("====> 匹配数字、非数字：'\d'、'\D'")
re10 = re.match("\d", "78hello World")
re11 = re.match("\D", "hello12 World")
print(re10.group() if re10 else re10)
print(re11.group() if re11 else re11)

print("====> 匹配空格：'\s'")
re12 = re.match("\s", "hello")
re13 = re.match("\ss", " shello")
print(re12.group() if re12 else re12)
print(re13.group() if re13 else re13)
