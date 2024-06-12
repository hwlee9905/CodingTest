#import sys

sumList = []
N = int(input())
list = [[] for _ in range(N)]
for i in range(N):
    list[i] = [-1 for _ in range(3)]
    list[i][0], list[i][1], list[i][2] = map(int, input().split())
# def RGB(start):
# 시간초과 하지 않는 코드
# N = int(input())
# cost = []
# for _ in range(N):
#     cost.append(list(map(int, input().split())))
#
# dp = [[0] * 3 for _ in range(N)]
# dp[0][0], dp[0][1], dp[0][2] = cost[0]
#
# for i in range(1, N):
#     dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + cost[i][0]
#     dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + cost[i][1]
#     dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + cost[i][2]
#
# print(min(dp[N-1]))

class Node:
    def __init__(self, data=None, i=None, depth=None):
        self.data = data
        self.i = i
        self.left = None
        self.right = None
        self.depth = depth
        if (len(list) - 1) != depth:
            if i == 0:
                self.left = Node(self.data + list[self.depth + 1][1], 1, self.depth + 1)
                self.right = Node(self.data + list[self.depth + 1][2], 2, self.depth + 1)
            if i == 1:
                self.left = Node(self.data + list[self.depth + 1][0], 0, self.depth + 1)
                self.right = Node(self.data + list[self.depth + 1][2], 2, self.depth + 1)
            if i == 2:
                self.left = Node(self.data + list[self.depth + 1][0], 0, self.depth + 1)
                self.right = Node(self.data + list[self.depth + 1][1], 1, self.depth + 1)
        else:
            sumList.append(self.data)
    def preorder(self):
        if self:  # 기본 종료 조건 추가
            print(self.data, end=" ")  # 현재 노드 데이터 출력
            if self.left:  # 왼쪽 자식이 있으면 왼쪽 자식부터 순회
                self.left.preorder()
            if self.right:  # 오른쪽 자식이 있으면 오른쪽 자식 순회
                self.right.preorder()

root = Node(list[0][0], 0, 0)
root1 = Node(list[0][1], 1, 0)
root2 = Node(list[0][2], 2, 0)
print(min(sumList))

