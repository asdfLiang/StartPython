import gevent, time
from gevent import monkey

"""
    gevent自动切换
"""


def task(name: str):
    for i in range(3):
        print(f"task {name} print i = {i}")
        time.sleep(2)


def gtask(name: str):
    for i in range(3):
        print(f"gevent task {name} print i = {i}")
        gevent.sleep(2)


# 自动切换
gevent.joinall(
    [gevent.spawn(gtask, "自动切换任务一"), gevent.spawn(gtask, "自动切换任务二")]
)

# 不自动切换
# monkey.patch_all() # 将不同任务转换成自动切换任务
gevent.joinall(
    [gevent.spawn(task, "不自动切换任务一"), gevent.spawn(task, "不自动切换任务二")]
)
