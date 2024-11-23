"""
    一、查找
"""

str0 = "hello world"

# find
print("================== find ==================")
print(str0.find("o"))
print(str0.find("z"))
print(str0.find("l", 1, 5))

# index
print("================== index ==================")
print(str0.index("o"))
print(str0.index("l", 1, 5))

# count
print("================== count ==================")
print(str0.count("l"))
print(str0.count("l", 4))
