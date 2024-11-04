# 문제
# https://www.acmicpc.net/problem/1012

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    List = [[] for _ in range(K)]
    for i in range(K):
        List[i] = map(int, input().split())

