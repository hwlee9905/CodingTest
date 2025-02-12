# https://www.acmicpc.net/problem/2178
import sys, collections
INPUT = sys.stdin.readline
N, M = map(int, INPUT().split())
List = [[[0] * (M + 2)] + [[0] + list(map(int, INPUT().strip()))  + [0] for _ in range(N)] + [[0] * (M + 2)]]
visited = [[0] * (M + 2) for _ in range(N + 2)]
deque = collections.deque
queue = deque([1,1,1])
print(List)