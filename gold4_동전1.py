# https://www.acmicpc.net/problem/2293
import sys
INPUT = sys.stdin.readline

n, k = map(int, INPUT().split())

arr = list(int(INPUT()) for _ in range(n))

print(arr)