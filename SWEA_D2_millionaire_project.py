# 테스트 케이스의 수 입력
T = int(input())

# 각 테스트 케이스에 대해 실행
for test_case in range(1, T + 1):
    # 각 테스트 케이스의 길이 입력
    N = int(input())
    # 각 날짜별 매매가 입력
    prices = list(map(int, input().split()))

    # 뒤에서부터 순회하며 최대 이익 계산
    max_profit = 0
    max_price = prices[-1]  # 마지막 날의 매매가를 최대 매매가로 설정

    for i in range(N - 2, -1, -1):  # 뒤에서부터 순회
        if prices[i] < max_price:  # 현재 매매가가 최대 매매가보다 작다면
            max_profit += max_price - prices[i]  # 차익을 더함
        else:
            max_price = prices[i]  # 아니라면 최대 매매가 갱신

    # 결과 출력
    print("#{} {}".format(test_case, max_profit))
