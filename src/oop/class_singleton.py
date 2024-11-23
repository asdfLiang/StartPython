"""
    单例
"""


# 第一种方式：使用__new__
class SingletonA:
    _inst = None

    def __new__(cls, *args, **kwargs):
        if cls._inst is None:
            cls._inst = super().__new__(cls)
        return cls._inst


print(SingletonA())
print(SingletonA())


# 第二种方式：使用类方法
class SingletonB:
    _inst = None

    @classmethod
    def getInstance(cls):
        if cls._inst is None:
            cls._inst = super().__new__(cls)
        return cls._inst


print(SingletonB.getInstance())
print(SingletonB.getInstance())


# 第三种方式：通过装饰器实现
def singleton(className: str):
    _instDict = {}

    def getInstance():
        if className not in _instDict:
            _instDict[className] = className()
        return _instDict[className]

    return getInstance


@singleton
class SingletonC:
    pass


print(SingletonC())
print(SingletonC())


# 第四种方式：通过元类实现
class SingletonD:
    def __init__(self, name) -> None:
        self.name = name

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_inst"):
            cls._inst = super().__new__(cls)
        return cls._inst


d1 = SingletonD("d1")
d2 = SingletonD("d2")
print(d1)
print(d2)


# 第五种方式：通过模块导入实现
import singletonE
import singletonE

print(singletonE.e1)
print(singletonE.e1)
