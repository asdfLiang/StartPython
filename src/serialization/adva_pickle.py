import pickle

"""
    序列化
"""

# 示例数据
data = {"name": "John", "age": 30, "isStudent": False, "grades": [85, 90, 78, 92]}

# 使用 pickle 保存数据
with open("resources/pkl_data", "wb") as file:
    pickle.dump(data, file)

# 使用 pickle 加载数据
with open("resources/pkl_data", "rb") as file:
    load_data = pickle.load(file)
print(load_data)
