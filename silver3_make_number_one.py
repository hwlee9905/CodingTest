# 문제
# https://www.acmicpc.net/problem/1463

import sys
INPUT = sys.stdin.readline
N = int(INPUT())

count = 0

for i in range(1, N + 1):
    if N == 1:
        break
    if N % 3 == 0:
        N /= 3
        count += 1
        print(N)
        continue
    if N % 2 == 0:
        N /= 2
        count += 1
        print(N)
        continue
    N -= 1
    count += 1
    print(N)

print(count)