import heapq

heap = []

# 小顶堆
heapq.heappush(heap, 932)
heapq.heappush(heap, 193)
heapq.heappush(heap, 393)
heapq.heappush(heap, 118)
heapq.heappush(heap, 524)
heapq.heappush(heap, 543)

print("查看堆顶元素：", heap[0])

while heap:
    print(heapq.heappop(heap))

alphaHeap = []
heapq.heappush(alphaHeap, "k")
heapq.heappush(alphaHeap, "f")
heapq.heappush(alphaHeap, "q")
heapq.heappush(alphaHeap, "z")
heapq.heappush(alphaHeap, "d")
heapq.heappush(alphaHeap, "e")
while alphaHeap:
    print(heapq.heappop(alphaHeap))
