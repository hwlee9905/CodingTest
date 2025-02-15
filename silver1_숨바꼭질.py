# https://www.acmicpc.net/problem/1697
import sys
INPUT = sys.stdin.readline
N, K = map(int, INPUT().split())

graph = []

for i in range(N, K + 1):
    