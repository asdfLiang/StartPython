"""
    多继承、类方法、静态方法
"""


# 静态方法
class Machine:
    wheel: str
    gear: str
    shelf: str

    def __work(self):
        print(f"do specifical work")

    @staticmethod
    def modify():
        print("modify machine")


# 类方法
class EmbeddedSystem:
    soc: str
    app: list

    @classmethod
    def udpate(cls):
        print(cls.__name__)


# 多继承
class Car(Machine, EmbeddedSystem):
    name: str

    def __init__(self, name: str):
        self.wheel = "4 wheels"
        self.app = ["map", "player"]

    def work(self):
        print(f"use {self.wheel} run, and open {self.app[0]}、{self.app[1]} app")


car = Car("car")
car.work()
Car.udpate()
Car.modify()
