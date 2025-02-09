# # https://www.acmicpc.net/problem/2096
# import sys
# INPUT = sys.stdin.readline
# N = int(INPUT())
# List = list(map(int, INPUT().split()))
# MaxDp = [0] * 3
# MinDp = [0] * 3
# MaxDp[0] = List[0]
# MaxDp[1] = List[1]
# MaxDp[2] = List[2]
# MinDp[0] = List[0]
# MinDp[1] = List[1]
# MinDp[2] = List[2]
#
# if N > 1:
#     for i in range(1, N):
#         List = list(map(int, INPUT().split()))
#         prevMaxDp = [MaxDp[0], MaxDp[1], MaxDp[2]]
#         prevMinDp = [MinDp[0], MinDp[1], MinDp[2]]
#
#         for a in range(3):
#             if a == 0:
#                 MaxDp[a] = max(prevMaxDp[0], prevMaxDp[1]) + List[0]
#                 MinDp[a] = min(prevMinDp[0], prevMinDp[1]) + List[0]
#             if a == 1:
#                 MaxDp[a] = max(prevMaxDp[0], prevMaxDp[1], prevMaxDp[2]) + List[1]
#                 MinDp[a] = min(prevMinDp[0], prevMinDp[1], prevMinDp[2]) + List[1]
#             if a == 2:
#                 MaxDp[a] = max(prevMaxDp[1], prevMaxDp[2]) + List[2]
#                 MinDp[a] = min(prevMinDp[1], prevMinDp[2]) + List[2]
#         print(MaxDp)
#
# print(f'{max(MaxDp)} {min(MinDp)}')

# https://www.acmicpc.net/problem/2096
import sys
INPUT = sys.stdin.readline
N = int(INPUT())
List = list(map(int, INPUT().split()))
MaxDp = [0] * 3
MinDp = [0] * 3
MaxDp[0] = List[0]
MaxDp[1] = List[1]
MaxDp[2] = List[2]
MinDp[0] = List[0]
MinDp[1] = List[1]
MinDp[2] = List[2]

if N > 1:
    for i in range(1, N):
        List = list(map(int, INPUT().split()))
        for a in range(3):
            if a == 0:
                MaxDp[a] += max(List[0], List[1])
                MinDp[a] += min(List[0], List[1])
            if a == 1:
                MaxDp[a] += max(List[0], List[1], List[2])
                MinDp[a] += min(List[0], List[1], List[2])
            if a == 2:
                MaxDp[a] += max(List[1], List[2])
                MinDp[a] += min(List[1], List[2])
        print(MaxDp)



print(f'{max(MaxDp)} {min(MinDp)}')

