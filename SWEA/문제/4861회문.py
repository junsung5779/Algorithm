import sys
sys.stdin = open('input4861회문.txt')

# 테스트케이스의 수를 받는다
T = int(input())

# 길이가 M인 회문을 골라내야 한다.
for tc in range(1,T+1):
    # N과 M을 받는다
    N, M = map(int, input().split())
    # N개의 글자를 가진 N개의 줄을 이중배열로 받는다.
    arr = [list(map(str, input())) for _ in range(N)]

    # 결과값을 초기화한다.
    res = ''
    # 1. 가로로 회문을 찾는경우
    # y좌표를(i)을 0~N까지 순회하면서
    for i in range(N):
        # 길이 M인 회문만 검색하기
        # 시작하는 x좌표(j)의 범위(0~(N-M+1))을 순회하면서
        for j in range(N-M+1):
            # 회문이 있는지 확인
            # 회문 판단변수를 초기화한다
            ok1 = 0
            ok2 = 0
            # 구하고자 하는 회문의 길이가 홀수인 경우 짝수인경우를 M-1로 구분했다.
            # 시작하는 x좌표(j)에서 j+(M-1)//2 까지를 순회하면서
            for k in range(M//2):
                # arr의[i][j+k]와 arr의[i][j+M-1-k]가 같으면
                if arr[i][j+k] == arr[i][j+M-1-k]:
                    # 회문판단변수(ok)에 1을 더한다.
                    ok1 += 1
                # arr의[i][k]와 arr의[i][M-k]가 같으면
                if arr[j + k][i] == arr[j+M-1-k][i]:
                    # 회문판단변수(ok)에 1을 더한다.
                    ok2 += 1
            # 만약 순회를 하고 난 후 ok에 저장된 값이 M//2와 같다면
            if ok1 == M//2:
                # arr의[i][j] 부터 arr의[i][M] 까지 결과값에 문자열형태로 저장한다.
                for k in range(j, j+M):
                    res += arr[i][k]
            if ok2 == M//2:
                # arr의[i][j] 부터 arr의[i][M] 까지 결과값에 문자열형태로 저장한다.
                for k in range(j, j+M):
                    res += arr[k][i]


    print("#{} {}".format(tc, res))