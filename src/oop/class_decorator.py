"""
    装饰器（可用于函数时间统计、框架路由传参、插入日志、事务处理、权限校验、缓存）
"""


# 模板
def wrapper(func):
    def inner(*args, **kwargs):
        res = func(*args, **kwargs)
        return res

    return inner


# 日志
def logger(func) -> None:
    def wapper(*args, **kwargs):
        print(f"开始执行：方法{func.__name__}")
        print(f"方法参数：args: {args}, kwargs: {kwargs}")
        res = func(*args, **kwargs)
        print(f"完成执行, 结果为：{res}")

    return wapper


@logger
def add(x: int, y: int) -> int:
    return x + y


add(1, 2)


# 事务
def transaction(func) -> None:
    def wrapper(*args, **kwargs):
        print("start transaction")
        print(f"res = {func(*args, **kwargs)}")
        print("end transaction")

    return wrapper


@transaction
def prod(x: int, y: int) -> int:
    return x * y


prod(2, 3)
