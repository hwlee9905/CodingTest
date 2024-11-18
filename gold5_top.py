# 문제
# https://www.acmicpc.net/problem/2493
import sys, collections
deque = collections.deque
input = sys.stdin.readline

N = int(input())
top = list(map(int, input().split()))
len = top.__len__()
accept = [0 for _ in range(len)]


for n in top:
    len -= 1
    for i in range(len - 1, -1, -1):
        if top[i] >= n:
            accept[len] = i + 1
            break

for i in accept:
    print(i, end=" ")
