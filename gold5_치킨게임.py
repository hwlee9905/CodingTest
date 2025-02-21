# https://www.acmicpc.net/problem/15686
import sys
INPUT = sys.stdin.readline
N, M = map(int, INPUT().split())
arr = [list(map(int, INPUT().split())) for _ in range(N)]
chickenStore = []
house = []
distanceSum = [0] * M
for r in range(N):
    for c in range(N):
        if arr[r][c] == 2:
            ## !!!!! 각 치킨집이 최소거리인 집들의 최소거리를 모두 합해서 해당 치킨집에 저장해야함
            chickenStore.append([r,c, 0]) #치킨집 행,열, 해당 치킨집이 최소거리인 집의 개수

        if arr[r][c] == 1:
            house.append([r,c,0,0])  # 집 행,열, 최소거리인 치킨집 인덱스, 최소거리


for c in range(len(chickenStore)):
    for h in range(len(house)):
        houseR = house[h][0] + 1
        houseC = house[h][1] + 1
        chickenStoreR = chickenStore[c][0] + 1
        chickenStoreC = chickenStore[c][1] + 1
        distance = abs(houseR - chickenStoreR) + abs(houseC - chickenStoreC)
        if distance < house[h][3] != 0:
            chickenStore[c][2] += 1
            chickenStore[house[h][2]][2] -= 1
            house[h][2] = c
            house[h][3] = distance

        elif house[h][3] == 0:
            house[h][2] = c
            house[h][3] = distance
            chickenStore[c][2] += 1

for h in range(len(house)):
    distanceSum[house[h][2]] =

house = sorted(house, key=lambda x: x[3]) # 최소거리 기준으로 집을 정렬
print(house)
print(chickenStore)
