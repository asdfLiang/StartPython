import time

"""
    处理时间的内置模块
"""

# 获取一个时间戳
t1 = time.time()
print(t1, type(t1))  # 1732587415.8602316 <class 'float'>
print()

# 将时间戳转换为数组格式的时间
t2 = time.localtime()
# time.struct_time(tm_year=2024, tm_mon=11, tm_mday=26, tm_hour=10, tm_min=16, tm_sec=55, tm_wday=1, tm_yday=331, tm_isdst=0)
print(t2)
print(t2[0])  # 2024
print(t2.tm_year)  # 2024
print()

# 把表示时间的元组简化
print(time.asctime())  # Tue Nov 26 10:16:55 2024
print()

# 选择性简化
print(time.strftime("%Y-%m-%d", t2))  # 2024-11-26
print()

# 将格式字符串转化成struct_time
stime = "2024-11-26 10:15:34"
# time.struct_time(tm_year=2024, tm_mon=11, tm_mday=26, tm_hour=10, tm_min=15, tm_sec=34, tm_wday=1, tm_yday=331, tm_isdst=-1)
print(time.strptime(stime, "%Y-%m-%d %H:%M:%S"))
print()
