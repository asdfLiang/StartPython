from greenlet import greenlet

"""
    使用greenlet创建协程：pip install greenlet
"""


def func1():
    print("协程一：第1条输出")
    g2.switch()
    print("协程一：第2条输出")
    g2.switch()
    print("协程一：第3条输出")


def func2():
    print("协程二：第1条输出")
    g1.switch()
    print("协程二：第2条输出")
    g1.switch()
    print("协程二：第3条输出")


g1 = greenlet(func1)
g2 = greenlet(func2)

g1.switch()
