import sys
sys.stdin = open("input4881.txt")

# idx : 행을 의미하는 인덱스
# sum_v : 값을 선택했을 떄의 누적합
def solve(idx, used, sum_v):
    global min_v
    # 경우의 수를 줄이기 위해서, 유망하지 않으면 실행하지 않음
    if sum_v >= min_v:      # backtracking
        return
    if idx == N:
        # 모든 행을 결정
        if sum_v < min_v:
            min_v = sum_v
        return

    # 각 행에서 선택할 수 있는 열을 선택한 다음
    # 다음행을 결정한다.
    for i in range(N):  # 각 열을 확인할건데...
        if not used[i]: # used[i] == 0 : 아직 사용하지 않은 열
            # 각 행에서 선택한 열의 인덱스가 필요한게 아니라
            # 합만 알면 된다.
            # 각 행에서 열을 선택할 때마다, 열의 값을 더해서
            # 다음 행으로 넘어간다.
            used[i] = 1 # i번째 열을 사용했음을 표시
            solve(idx+1, used, sum_v + data[idx][i])
            # i번째 열을 선택햇을 때, 모든 경우의 수를 고려함
            # 다음 연산을 위해서 사용하지 않은것으로 표시
            used[i] = 0


# 테스트케이스 횟수를 입력받는다.
T = int(input())
# 테스트케이스 횟수를 반복하면서
for tc in range(1, T+1):
    # N*N배열을 결정하는 N을 입력받는다.
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    # 순열을 만드는데 사용된 열을 표시하기 위한 배열
    used = [0]*N
    # 순열 만들어서 합 구하기
    min_v = 100
    # sum_v의 누적합을 0으로 썻다
    solve(0,used,0)
    print('#{} {}'.format(tc, min_v))