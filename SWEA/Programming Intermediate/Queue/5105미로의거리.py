import sys
sys.stdin = open("input5105.txt")

# 출발점부터 미로를 탐색한다.
# 탐색하다가 출발점을 찾으면 출발점부터 도착점까지 뚫려있는 최단경로를 계산한다.

# 델타탐색 정의
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def min_length(r,c):
    # queue에 출발점의 좌표와 해당 노드까지의 거리를 집어넣은채로 초기화한다.(queue = [(r,c,0)])
    queue = [(r,c,0)]
    # 방문 배열을 초기화한다.
    visited = [[0]*N for _ in range(N)]
    # queue의 길이가 0이 될 때 까지 while문을 돌면서
    # (해당 좌표에서 갈 수 있는곳이 하나도 없는 부분이 계속 존재하기 떄문에 queue의 길이는 줄어들 수 밖에 없음)
    while queue:
        # queue의 첫 번째 원소를 pop한다.(queue.pop(0))(탐색을 마친 좌표를 제거하는 과정)(이동할 수 없는 경우도 자동으로 제거됨)
        cr, cc, cd = queue.pop(0)
        # 만약 해당 좌표가 도착점이라면
        if arr[cr][cc] == '3':
            # 도착점까지의 최솟값을 반환
            return cd-1
        # 4방향을 탐색한다.
        for i in range(4):
            nr = cr+dr[i]
            nc = cc+dc[i]
            # queue의 첫 번째 원소에서 모든 방향을 확인하며 인덱스 에러가 나지 않고 도착점이 아닌 갈 수 있는 좌표가 있으면(해당 좌표에 저장된 값이 0일 경우)
            if 0<= nr < N and 0<= nc < N and arr[nr][nc] != '1' and not visited[nr][nc]:
                # queue에 갈 수 있는 좌표와 해당 좌표와 (해당 노드까지의 거리+1)를 append 한다.(nr,nc,cd+1)
                queue.append((nr,nc,cd+1))
                visited[nr][nc] = 1

    # 도착점을 찾기 못한 채로 조건문이 끝나게 되면 0을 반환한다(return 0)
    return 0


T = int(input())    # 테스트케이스횟수를 입력받음
for tc in range(1,T+1): # 테스트케이스 횟수만큼 순회하면서
    r, c = 0, 0
    N = int(input())    # N*N배열의 크기를 정하는 N을 입력받음
    arr = [list(input()) for _ in range(N)] # 테스트케이스를 N*N배열의 형태로 받음
    # 해당 배열을 탐색하여 출발점의 좌표를 찾아내어 r,c로 저장
    for i in range(N):
        for j in range(N):
            if arr[i][j] == '2':
                r, c = i, j

    # 이제 이 출발점 좌표를 가지고 함수에 입장!
    result = min_length(r, c)
    # 결과값 출력
    print("#{} {}".format(tc, result))

