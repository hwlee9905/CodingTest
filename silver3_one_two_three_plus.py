# 문제
# https://www.acmicpc.net/problem/9095
import sys
INPUT = sys.stdin.readline
T = int(INPUT())
results = []
for _ in range(T):
    N = int(INPUT())
    arr = [0] * (N + 1)
    arr[0] = 1
    for i in range(1, N + 1):
        if i > 0:
            arr[i] += arr[i - 1]
        if i > 1:
            arr[i] += arr[i - 2]
        if i > 2:
            arr[i] += arr[i - 3]
    results.append(arr[N])

for result in results:
    print(result)
