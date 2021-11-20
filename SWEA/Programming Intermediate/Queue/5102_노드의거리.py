import sys
sys.stdin = open("input5102.txt")

def BFS(sV):
    # 큐를 생성과 동시에 선언
    Q = [[sV, 0]]
    # 방문체크를 위한 리스트 생성
    visited = [False] * (V+1)
    # 첫번째는 방문함
    visited[sV] = True

    while Q:
        v, dist = Q.pop(0)
        # 만약 V라는 지점이 도착지점이면 거리를 반환하고 끝냄
        if v == eV:
            return dist
        for i in range(1, V+1):
            # 내가 지금 보고있는 정점과 i라는 정점이 연결이 되어있으면서 해당 지점에 방문을 하지 않았으면
            if adj_arr[v][i] == 1 and visited[i] == False:
                Q.append([i, dist+1])
                visited[i] = True
    return None



T = int(input())
for tc in range(1, T+1):
    # v: 정점의 수 1번부터 시작,
    # E: 간선의 수
    V, E = map(int, input().split())
    # 인접행렬을 이용하여 작성해보자
    # 해당 좌표를 그래도 사용하기 위해 (V+1)*(V+1)행렬로 설정
    adj_arr = [[0]*(V+1) for _ in range(V+1)]
    for i in range(E):
        a, b = map(int, input().split())
        # 무방향이므로 양쪽 연결
        adj_arr[a][b] = 1
        adj_arr[b][a] = 1

    # 시작점, 끝점
    sV, eV = map(int, input().split())
    print("#{} {}".format(tc, BFS(sV)))