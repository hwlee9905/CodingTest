# https://www.acmicpc.net/problem/11054
import sys
INPUT = sys.stdin.readline
N = int(INPUT())
arr = list(map(int, INPUT().split()))
dp = [1] * N
current = 0
for i in range(N):


print(dp)