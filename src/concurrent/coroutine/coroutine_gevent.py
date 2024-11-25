"""
    使用gevent创建协程：pip install gevent
"""

import gevent


def func1():
    print("协程一：第1条输出")
    print("协程一：第2条输出")


def func2():
    print("协程二：第1条输出")
    print("协程二：第2条输出")


gt1 = gevent.spawn(func1)
gt2 = gevent.spawn(func2)

gt1.join()
gt2.join()
