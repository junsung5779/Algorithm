import sys
sys.stdin = open("input오목판정.txt")

def check(x,y):
    for i in range(8):
        cnt = 1
        r, c = x +dx[i], y + dy[i]
        # 같은 방향에서 누적하는 방법(한 방향으로 계속 가기)
        while 0<= r <N and 0<= c <N and board[r][c] == 'o':
            cnt += 1
            r, c = r+dx[i], c+dy[i]
        if cnt == 5: return True
    return False


T = int(input())
ans=["NO","YES"]
# 상, 하, 좌, 우, 우상, 우하, 좌하, 좌상
dx = [-1, 1, 0, 0,-1, 1, 1, -1]
dy = [0, 0, -1, 1, 1, 1, -1, -1]
for tc in range(1, T+1):
    N = int(input())
    board = [input() for _ in range(N)]

    flag = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == ".": continue
            if check(i, j):
                flag = 1
                break
        if flag: break

    print("#{} {}".format(tc, ans[flag]))