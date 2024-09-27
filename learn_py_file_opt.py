import os
import shutil

"""
    文件及文件夹操作
"""

print(
    "======================================= 创建文件夹 ======================================="
)
dir1 = "./resources/dir1"
dir2 = "./resources/dir2"
if os.path.exists(dir1):
    print("文件夹1已存在")
else:
    os.mkdir(dir1)
    print("文件夹1已创建完毕")

if os.path.exists(dir2):
    print("文件夹2已存在")
else:
    os.mkdir(dir2)
    print("文件夹2已创建完毕")

print(
    "======================================= 遍历文件夹 ======================================="
)
dir3 = "./resources/dir3/"


print(
    "======================================= 文件操作 ======================================="
)
file_source = dir1 + "/1.jpg"
file_target = dir2 + "/1.jpg"
# 复制文件
shutil.copyfile(file_source, file_target)
# 移动文件
shutil.move(file_source, file_target)
# 删除文件
