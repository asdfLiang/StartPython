"""
    锁
"""

from threading import Thread, Lock

lock = Lock()
count = 0


def adder():
    try:
        lock.acquire()
        global count
        for _ in range(1000):
            count += 1
        print(f"res = {count}")
    finally:
        lock.release()


if __name__ == "__main__":
    for _ in range(100):
        t = Thread(target=adder)
        t.start()
