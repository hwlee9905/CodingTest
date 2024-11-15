# 문제
# https://www.acmicpc.net/problem/2583
import sys, collections
deque = collections.deque
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
count = 0
M, N, K = map(int, input().split())
array = [[True] * (N+1) for _ in range(M+1)] # N = 가로길이 M= 세로길이
visited = [[False] * (N+1) for _ in range(M+1)]
areaList = []

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(x1, x2):
        for y in range(y1, y2):
            array[y][x] = False


for y in range(M):
    for x in range(N):
        if not visited[y][x]:
            count = 0
            stack = deque([(x, y)])
            while stack:
                xStack, yStack = stack.pop()
                count += 1
                for vector in range(4):
                    xVector = xStack + dx[vector]
                    yVector = yStack + dy[vector]
                    if (N >= xVector > 0) and (M >= yVector > 0) and not visited[yVector][xVector]:
                        visited[yVector][xVector] = True
                        stack.append((xVector, yVector))
            areaList.append(count)

for y in range(M):
    for x in range(N):
        print(array[y][x], end=" ")
    print()

for area in areaList:
    print(area, end=" ")