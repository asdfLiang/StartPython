from collections import deque
import queue

# 线程不安全队列
print("===== 线程不安全队列 =====")
q = deque()
# 入队
q.append(1)
q.append(2)
q.append(3)
print(f"队列元素数量：{len(q)}")
# 查看对头元素
print(f"查看队头元素（线程不安全）：{q[0]}")

# 出队
print(f"出队（线程不安全）：{q.popleft()}")
print(f"出队（线程不安全）：{q.popleft()}")


# 线程安全队列
print("====== 线程安全队列 ======")
safeQ = queue.Queue()
# 入队
safeQ.put("a")
safeQ.put("b")
safeQ.put("c")
print(f"队列元素数量：{safeQ.qsize()}")

# 查看队头元素
print(f"查看队头元素（线程不安全）：{safeQ.queue[0]}")

# 出队
print(f"出队（线程安全）：{safeQ.get()}")
print(f"出队（线程安全）：{safeQ.get()}")
