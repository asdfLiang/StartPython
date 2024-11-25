import re

"""
    search() 扫描整个字符串并返回第一个成功的匹配

    与match()比较：
        match(): 只能从字符串开始位置比较
        search(): 扫描整个字符串，返回第一个匹配成功的
"""

print(re.search("\d+", "今天是25号吗").group())
