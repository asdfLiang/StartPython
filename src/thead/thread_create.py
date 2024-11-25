from threading import Thread
import time

count = 0


# 第一种方式：继承Thread对象
class CustomThread(Thread):
    def run(self) -> None:
        global count
        for _ in range(100):
            count += 1
        print(f"和为 {count}")


# 第二种方式：将普通方法作为Thread对象的参数传入
def adder():
    global count
    for _ in range(100):
        count += 1
    print(f"和为 {count}")


if __name__ == "__main__":
    for _ in range(100):
        t = Thread(target=adder)
        # t = CustomThread()
        t.start()
