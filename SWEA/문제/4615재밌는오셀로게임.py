import sys
sys.stdin = open("input4615.txt")

# 테스트케이스 횟수를 입력받는다.
T = int(input())
# 테스트케이스 횟수만큼 순회하면서
for tc in range(1, T+1):
    # 보드의 한 변의 길이 N과 플레이어가 돌을 놓는 횟수 M을 입력받는다
    N, M = map(int, input().split())
    # 좌표를 1,1부터 쓰고 델타탐색을 할 때 인덱스범위를 초과하는 오류를 만들지 않기 위해 (N+2)*(N+2)크기의 보드를 만든다.
    arr = [[0]*(N+2) for _ in range(N+2)]
    # 게임을 시작하기 전에 정 가운대에 흑돌2개 백돌2개를 배치 한다.
    arr[(N+1)//2][(N+1)//2] = 2
    arr[(N+2)//2][(N+2)//2] = 2
    arr[(N+1)//2][(N+2)//2] = 1
    arr[(N+2)//2][(N+1)//2] = 1
    # 델타탐색을 위해 8방향을 미리 설정한다.
    #     상 우 하 좌 좌상 우상 우하 좌하
    dx = [-1, 0, 1, 0, -1, -1, 1, 1]
    dy = [0, 1, 0, -1, -1, 1, 1, -1]
    # 플레이어가 돌읗 놓는 횟수 만큼 테스트케이스를 입력받는다
    for a in range(M):
        # r : 바둑돌을 놓는 행
        # c : 바둑돌을 놓는 열
        # bw : 놓는 바둑돌의 흑백여부(흑:1, 백:2)
        r, c, bw = map(int, input().split())
        # 바둑돌을 놓는다.
        arr[r][c] = bw
        # 델타탐색을 이용하여 8방향을 검사한다.
        for d in range(8):
            # 카운트 값을 초기화한다.
            cnt = 0
            # 해당 방향으로 한 칸 이동한다.
            r1 = r+dx[d]
            c1 = c+dy[d]
            # 만약 놓는 바둑돌과 인접한 해당방향의 칸에 다른색의 바둑돌이 있다면
            if arr[r1][c1] != 0 and arr[r1][c1] != bw:
                # 조건문을 돌린다.
                while True:

                    # 계속 거리를 늘려가며 검사하다 놓는 바둑돌의 색과 같은 돌을 발견하면
                    if arr[r1][c1] == bw:
                        # 여태껏 진행해온 칸 수 만큼의 돌을
                        for k in range(cnt):
                            # 놓는 바둑돌의 색으로 바꾼다.
                            r1 = r1-dx[d]
                            c1 = c1-dy[d]
                            arr[r1][c1] = bw
                        break
                    # 계속 거리를 늘려가며 검사하다 바둑돌이 있으나, 놓는 바둑돌의 색과 같지 않다면
                    elif arr[r1][c1] != bw and arr[r1][c1] != 0:
                        # 해당방향의 다음 거리를 검사하고
                        r1 = r1 + dx[d]
                        c1 = c1 + dy[d]
                        # 카운트 값을 1회 늘린다
                        cnt += 1
                        break

                    # 인접한 해당방향의 칸이 마지막 칸일 경우
                    elif r1 == 1 or c1 == 1 or r1 == N or c1 == N:
                        # continue
                        break


            # # 만약 놓는 바둑돌과 인접한 해당방향의 칸에 같은색의 바둑돌이 있거나 바둑돌이 없다면
            # elif arr[r1][c1] == bw or arr[r1][c1] == 0:
            #     # continue
            #     continue

    # 테스트케이스가 끝나고 나면
    # 흑돌과 백돌의 갯수 초기화
    # B : 흑돌의 갯수
    # W : 백돌의 갯수
    B, W = 0, 0
    # 흑돌과 백돌의 개수를 센다.
    for i in range(N+2):
        for j in range(N+2):
            if arr[i][j] == 1:
                B += 1
            elif arr[i][j] == 2:
                W += 1

    print("#{} {} {}".format(tc, B, W))