# https://www.acmicpc.net/problem/1697
import sys, collections
INPUT = sys.stdin.readline
N, K = map(int, INPUT().split())
deque = collections.deque
MAX = 100001
graph = [0] * MAX

queue = deque([N])

while queue:
    node = queue.popleft()
    if node == K:
        print(graph[node])
        break

    for next_v in (node-1, node+1, 2*node):
        if 0 <= next_v < MAX and not graph[next_v]:
            graph[next_v] = graph[node] + 1
            queue.append(next_v)

