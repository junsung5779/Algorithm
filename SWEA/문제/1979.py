import sys
sys.stdin = open("input1979.txt")

T = int(input())
# 테스트케이스 횟수만큼 순회하면서
for tc in range(1, T+1):
    #N,K 값을 입력받는다.
    N, K = map(int, input().split())
    # 이중배열의 형태로 입력값을 받는다.
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 카운트 값을 초기화한다.
    cnt1 = 0
    cnt2 = 0
    # (0,0)부터 (N,N)까지 순회하며
    for i in range(N):
        # K와 비교할 길이를 초기화한다.
        res1 = 0
        res2 = 0

        # 인덱스를 N만큼 순회한다.
        for j in range(N):

            # 가로로 검사
            # 해당 인덱스에 1이 있고 j가 마지막 인덱스가 아니라면 res1에 1을 더한다.
            if arr[i][j] == 1 and j != N-1:
                res1 += 1
            # 마지막 인덱스에 도달했을 때
            if j == N-1:
                # 해당 인덱스에 1이 있다면 res1에 1을 더한다
                if arr[i][j] == 1:
                    res1 += 1
                    # 1을 더했을 때 1이 연속으로 K만큼 있다면
                    if res1 == K:
                        # 카운트에 1을 더한다
                        cnt1 += 1
                # 해당 인덱스에 0이 있다면
                if arr[i][j] == 0:
                    # 1이 연속으로 K만큼 있다면 카운트에 1을 더한다
                    if res1 == K:
                        cnt1 += 1
            # 해당 인덱스에 0이 있고 j가 마지막 인덱스가 아니라면
            if arr[i][j] == 0 and j != N-1:
                # 1이 연속으로 K만큼 있다면 카운트에 1을 더한다.
                if res1 == K:
                    cnt1 += 1
                    # 그리고 res1값을 초기화시킨다.
                    res1 = 0
                # 1이 연속으로 K만큼 있지 않다면 res1값을 초기화시킨다.
                if res1 != K:
                    res1 = 0

            # 세로로 검사
            # 해당 인덱스에 1이 있고 j가 마지막 인덱스가 아니라면 res2에 1을 더한다.
            if arr[j][i] == 1 and j != N-1:
                res2 += 1
            # 마지막 인덱스에 도달했을 때
            if j == N - 1:
                # 해당 인덱스에 1이 있다면 res2에 1을 더한다
                if arr[j][i] == 1:
                    res2 += 1
                    # 1을 더했을 때 1이 연속으로 K만큼 있다면
                    if res2 == K:
                        # 카운트에 1을 더한다
                        cnt2 += 1
                # 해당 인덱스에 0이 있다면
                if arr[j][i] == 0:
                    # 1이 연속으로 K만큼 있다면 카운트에 1을 더한다
                    if res2 == K:
                        cnt2 += 1
            # 해당 인덱스에 0이 있고 j가 마지막 인덱스가 아니라면
            if arr[j][i] == 0 and j != N-1:
                # 1이 연속으로 K만큼 있다면 카운트에 1을 더한다.
                if res2 == K:
                    cnt2 += 1
                    # 그리고 res2값을 초기화시킨다.
                    res2 = 0
                # 1이 연속으로 K만큼 있지 않다면 res2값을 초기화시킨다.
                if res2 != K:
                    res2 = 0

    print("#{} {}".format(tc, cnt1+cnt2))