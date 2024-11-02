# 문제
# https://www.acmicpc.net/problem/2606

# 예제 입력 1
# 7
# 6
# 1 2
# 2 3
# 1 5
# 5 2
# 5 6
# 4 7

# 예제 출력 1
# 4

import sys, collections
deque = collections.deque
input = sys.stdin.readline

# N: 컴퓨터의 수, M: 연결되어 있는 컴퓨터 쌍의 수
N, M = map(int, input().split())

# 그래프를 인접 리스트로 표현
graph = [[] for _ in range(N+1)]

# 간선 정보를 입력받아 그래프에 추가
for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)