# https://www.acmicpc.net/problem/15686
import sys, itertools
combination = itertools.combinations
INPUT = sys.stdin.readline
N, M = map(int, INPUT().split())
arr = [list(map(int, INPUT().split())) for _ in range(N)]
MIN = 0
chickenStore = []
house = []

for r in range(N):
    for c in range(N):
        if arr[r][c] == 2:
            chickenStore.append([r,c]) #치킨집 행,열
        if arr[r][c] == 1:
            house.append([r,c])  # 집 행,열

distanceArr = [[0] * len(house) for _ in range(len(chickenStore))]
minList = [0] * len(house)

for c in range(len(chickenStore)):
    for h in range(len(house)):
        houseR = house[h][0] + 1
        houseC = house[h][1] + 1
        chickenStoreR = chickenStore[c][0] + 1
        chickenStoreC = chickenStore[c][1] + 1
        distance = abs(houseR - chickenStoreR) + abs(houseC - chickenStoreC)
        distanceArr[c][h] = distance

comList = list(combination(distanceArr, M))

for Lists in comList:
    for distList in Lists:
        for a in range(len(distList)):
            if minList[a] == 0:
                minList[a] = distList[a]
            elif minList[a] > distList[a]:
                minList[a] = distList[a]
    if MIN == 0:
        MIN = sum(minList)
    elif sum(minList) < MIN:
        MIN = sum(minList)
    minList = [0] * len(house)

print(MIN)