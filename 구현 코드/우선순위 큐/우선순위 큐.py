import heapq,sys
ip = sys.stdin.readline
heap = []
for i in range(int(ip())):
    n = int(ip())
    if n == 0:
        if heap:
            print(abs(heapq.heappop(heap)))
        else:
            print(0)
    else:
        heapq.heappush(heap,-n)
# 백준 최대힙
