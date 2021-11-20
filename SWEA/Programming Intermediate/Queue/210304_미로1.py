import sys
sys.stdin = open("input미로1.txt")
#상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def BFS(r,c):
    Q = [(r,c)]

    while Q:
        cur_r, cur_c = Q.pop(0)
        # 서있는 위치가 도착지점인가?
        for i in range(4):
            nr = cur_r + dr[i]
            nc = cur_c + dc[i]
        
        if maze[nr][nc] == 3:
            return 1
        
        if nr < 0 or nr >= N or nc < 0 or nc >= N:
            continue
            
        # 갈 수 있는 자리라면
        if maze[nr][nc] != 1:
            Q.append((nr,nc))
            maze[nr][nc] = 1    # 방문체크


def DFS(r,c):
    global flag
    # 도착지점 확인
    if maze[r][c] == 3:
        flag = 1
        return
    maze[r][c] = 1

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if nr < 0 or nr >= N or nc < 0 or nc >= N:
            continue
        if maze[nr][nc] != 1:
            DFS(nr,nc)

for tc in range(10):
    tc_num = int(input())
    N = 16

    maze = [list(map(int, input().split())) for _ in range(N)]

    # 시작점을 찾아서 출발해야하므로
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                sR = i
                sC = j
                maze[i][j] = 1
    flag = 0    # 0으로 초기화
    # DFS(sR,sC)
    # print("#{} {}".format(tc_num, BFS(sR,sC)))
    print("#{} {}".format(tc_num, flag))