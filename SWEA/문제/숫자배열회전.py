import sys
sys.stdin = open("input숫자배열회전.txt")

T = int(input())
for tc in range(1,T+1):
    # 행렬의 수
    N = int(input())
    # 왜 4개를 받느냐? 초깃값 받고 90도,180도,270도 회전 이렇게 총 4개를 받기때문
    arr = [[[0]*N for _ in range(N)] for _ in range(4)]
    for i in range(N):
        arr[0][i] = list(map(int, input().split()))

    # 회전~~ 회오리~~~
    # 90도,180도,270도 이렇게 세개를 돌려야 하기 때문
    for k in range(1,4):
        for i in range(N):
            for j in range(N):
                arr[k][j][N-1-i] = arr[k-1][i][j]
    print("#{}".format(tc))
    for i in range(N):
        for k in range(1,4):
            if k != 1: print(end=" ")
            for j in range(N):
                print(arr[k][i][j], end="")
        print()