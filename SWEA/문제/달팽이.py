# 우,하,좌,상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 테스트 케이스 횟수를 입력받는다
T = int(input())
# 테스트 케이스 횟수를 순회하면서
for tc in range(1, T+1):
    # 정사각형의 한쪽 길이를 입력받는다
    N = int(input())
    # N*N의 배열을 생성한다.
    snail = [[0]*N for _ in range(N)]

    x, y = 0, 0
    i = 2
    d = 0
    snail[x][y] = 1
    while i <= N*N:

        if -1<x+dx[d%4]<N and -1<y+dy[d%4]<N and snail[x+dx[d%4]][y+dy[d%4]] == 0:
            x = x+dx[d%4]
            y = y+dy[d%4]
            snail[x][y] = i
            i += 1
        else:
            d += 1
    print('#{}'.format(tc))
    for i in range(N):
        print(*snail[i])