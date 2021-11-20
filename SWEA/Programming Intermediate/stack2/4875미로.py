import sys
sys.stdin = open("input4875.txt")

# 이차원 배열에서, DFS를 수행할 땐, 2차원배열의 각 요소가 그래프의 정점이다.
# 각 정점을 구분하는 방법은, 좌표값(r,c)
# 반복문과 stack을 이용한 dfs 구현
def dfs(r,c):
    # stack의 top에 있는 정점에서 갈 수 있는 방향을 탐색하고
    # 갈 수 있는 길(인접하면서, 방문하지 않은)이 있으면 그 길을 stack에 push
    # 없으면 stack.pop
    # 위 내용을 stack이 빌 때 까지 계속해서 반복(처음 stack이 비어있으면 안되니깐 시작정점(r,c)을 stack에 먼저 집어넣어야 함)

    stack = list()
    # 방문여부를 확인하기 위해 미로와 같은 모양의 visited 배열 생성
    visited = [[0]*N for _ in range(N)]
    # 시작 정점을 stack에 넣기(좌표를 넣어야 하므로 튜플구조로 넣기)
    stack.append((r,c))
    # 시장정점을 stack에 넣었으므로 방문표시도 해야함
    visited[r][c] = 1

    # 사방탐색을 위해 델타탐색좌표 생성
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]

    # stack이 빌 때 까지 계속해서 반복(dfs 시작)
    while stack:
        # stack의 top에서 갈 수 있는 경로 모두 탐색
        # stack에 append를 할 때 튜플구조로 한 쌍을 집어넣었기 때문에
        # pop 할 경우 각각받아야 함
        tr, tc = stack.pop()
        # tr,tc = stack[-1]
        for d in range(4):  # 사방탐색
            nr = tr + dr[d]
            nc = tc + dc[d]
            # 갈 수 있는 위치인지 검사(미로의 범위내, 방문하지 않음)
            if 0<=nr<N and 0<=nc<N and not visited[nr][nc]:
                # 방문하지 않은 지점에서 가능성 있는 값?? 0,1,3
                if maze[nr][nc] == 0:   # 통로, 이동하면 됨
                    stack.append((nr,nc))   # 해당 좌표를 튜플구조로 저장
                    visited[nr][nc] = 1     # 해당위치를 방문하였음
                # 출구를 찾은 경우
                elif maze[nr][nc] == 3:
                    # 1을 반환
                    return 1
    # dfs가 끝난 시점에, 목적지에 도달하지 못하면, 미로를 빠져나가지 못함
    return 0

# 테스트케이스횟수 입력받기
T = int(input())
# 테스트케이스 횟수를 반복하면서
for tc in range(1, T+1):
    # 미로의 크기를 입력받는다.
    N = int(input())
    # 미로의 크기만큼 미로의 지형에 대한 입력값을 받는다.
    maze = [list(map(int, input())) for _ in range(N)]

    # 시작점에서 DFS 탐색으로 목적지를 만나면 1, 아니면 0을 출력하면 됨
    # 1. 시작점 찾기
    # 2. 시작점에서 DFS 시작
    
    # 결과값 초기화
    result = 0
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                result = dfs(i,j)
    print("#{} {}".format(tc, result))