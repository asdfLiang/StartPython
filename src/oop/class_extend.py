"""
    类的继承、私有方法
"""


# 私有属性、方法
class Animal:
    __tail: True

    def __use_tail(self):
        print("use tail")


class Human(Animal):
    name: str
    age: int

    def introduce(self):
        print(f"My name is {self.name}, {self.age} years old")


h = Human()
h.name = "Human"
h.age = 5000
h.introduce()


# 重写
class Man(Human):
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name}, {self.age} years old, I am a man.")


man = Man("Bob", 24)
man.introduce()


#
class Woman(Human):
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name}, {self.age} years old, I am a woman.")


woman = Woman("Alice", 20)
woman.introduce()
