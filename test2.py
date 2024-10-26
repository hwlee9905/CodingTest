def soln(T, N, A, B):
    for _ in range(T):
        # 각 학생이 처음에 가지고 있는 족보의 집합 초기화
        tribes = [{i} for i in range(1, N+1)]
        day = 0
        while True:
            has_changed = False  # 변화가 있었는지 추적하는 플래그
            day += 1
            # 각 학생이 전달받은 족보를 자신의 집합에 추가
            for i in range(N):
                before = len(tribes[B[i]-1])  # 변화 전 길이
                tribes[B[i]-1] |= tribes[A[i]-1]
                if len(tribes[B[i]-1]) > before:  # 변화가 있었다면
                    has_changed = True
            # 모든 학생이 모든 족보를 가지고 있거나, 변화가 없었다면 종료
            if all(len(t) == N for t in tribes) or not has_changed:
                print(day)
                break
# 입력 예시
T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    soln(1, N, A, B)