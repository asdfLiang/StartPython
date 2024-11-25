import time

"""
    使用yield方式创建协程
"""


def func1():
    while True:
        yield "协程1"
        time.sleep(0.5)


def func2():
    while True:
        yield "协程2"
        time.sleep(1)


if __name__ == "__main__":
    f1 = func1()
    f2 = func2()

    while True:
        print(next(f1))
        print(next(f2))
