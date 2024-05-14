# import collections
# TC = int(input())
# for tc in range(TC):
#     SUM = 0
#     n, m = map(int, input().split())
#     Ri = [False for _ in range(n+1)]
#     Wi = [False for _ in range(m+1)]
#     sequence = []
#     for i in range(1, n+1):
#         Ri[i] = int(input())
#     for i in range(1, m+1):
#         Wi[i] = int(input())
#     for _ in range(2*m):
#         sequence.append(int(input()))
#
#
#     queue = collections.deque
#     currentCarQueue = queue()
#     currentWaitQueue = queue()
#     for i in sequence:
#         if not currentCarQueue:
#             currentCarQueue.append(sequence[0])
#             continue
#         while currentCarQueue or currentWaitQueue:
#             if i > 0:
#                 if len(currentCarQueue) == len(Ri)-1:
#                     currentWaitQueue.append(i)
#                     # print(f'주차장 꽉차서 대기열에 추가 {currentWaitQueue}')
#                     break
#                 else:
#                     currentCarQueue.append(i)
#                     # print(f'주차장이 비엇으므로 바로 입장{currentCarQueue}')
#                     break
#
#
#             else:
#                 exitCarIndex = -i
#                 # print(f'currentCarQueue.index(exitCarIndex) {currentCarQueue.index(exitCarIndex)+1}')
#                 SUM = SUM + (Wi[exitCarIndex] * Ri[currentCarQueue.index(exitCarIndex)+1])
#                 currentCarQueue.remove(exitCarIndex)
#                 # print(f'{exitCarIndex} 번차 나감 {currentCarQueue}')
#                 # print(f'SUM = {SUM}')
#                 if currentWaitQueue:
#                     currentCarQueue.append(currentWaitQueue.popleft())
#                     # print(f'대기열에서 추자장 입장{currentCarQueue}')
#                 break
#
#
#     print(f'#{tc + 1}', end=" ")
#     print(f'{SUM}')
#     # print(f'Ri = {Ri}')
#     # print(f'Wi = {Wi}')
#     # print(f'sequence = {sequence}')

T = int(input())

for tc in range(1, T + 1):

    N, M = map(int, input().split())  # 주차 공간 대수, 차량 대수
    park_cost = [int(input()) for _ in range(N)]  # 주차 공간 별 비용
    car_weight = [0] + [int(input()) for _ in range(M)]  # 차량 별 무게
    enter_list = [int(input()) for _ in range(2 * M)]  # 차량 입장 순서
    parking = [0] * N  # 주차장
    answer = 0

    wait_list = []  # 차량 대기 목록
    while enter_list:

        # 빈 주차 공간이 있으면 진용이는 곧바로 주차를 시키며, 주차 가능한 공간 중 번호가 가장 작은 주차 공간에 주차하도록 한다.
        # 다음 힌트에 근거하여 항상 제일 처음에 차량 대기 목록을 확인 후 주차한다. (break 하지 않는 것 주의 -> 대기 목록은 최대한 주차)
        if wait_list:
            for i in range(N):
                if parking[i] == 0:
                    parking[i] = wait_list.pop(0)

        car_num = enter_list.pop(0)
        if car_num > 0:  # 주차 하려는 차량이면
            for i in range(N):  # 번호가 적은 것 부터 주차 공간이 있다면 주차한다.
                if parking[i] == 0:
                    parking[i] = car_num
                    break
            else:  # 주차 공간이 없다면 대기 목록에 넣는다.
                wait_list.append(car_num)

        else:  # 출차 하려는 차량이면
            car_num = abs(car_num)

            park_num = 0
            for i in range(N):  # 주차장에서 해당 번호의 차량을 찾고 출차한다.
                if parking[i] == car_num:
                    park_num = i
                    parking[i] = 0

                    answer += (car_weight[car_num] * park_cost[park_num])
                    print(answer)
                    break

    print(f"#{tc}", answer)