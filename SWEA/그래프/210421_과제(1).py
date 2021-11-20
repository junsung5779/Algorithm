
#v : 현재 노드 번호
#d : 경로 길이
def dfs(v,d):
    global max_length
    visited[v] = 1
    # 현재 길이가 최장길이인지 확인
    if max_length < d:
        max_length = d
    # 갈 수 있는 모든 경로 탐색
    for i in range(1,N+1):
        # 만약 두 정점사이에 간선이 있고 해당 정점이 방문하지 않은 곳이라면
        if adj[v][i] and not visited[i]:
            # dfs
            # 다음 경로의 길이는 현재 경로길이 +1
            dfs(i,d+1)
    # 다른 경로에서 해당 노드를 탐색하려고 할 때 방문여부를 False로 해줘야한다(방문할 수 있도록)
    visited[v] = 0

for tc in range(1,int(input())+1):
    N,M = map(int,input().split())
    adj = [[0]*(N+1) for _ in range(N+1)]
    for _ in range(M):
        # 연결되어있는 정점에 대한 정보를 받는다
        s,e = map(int,input().split())
        # 무방향이므로 서로 연결되어있어야 한다
        # 인접행렬에 표시
        adj[s][e] = 1
        adj[e][s] = 1
    
    visited = [0]*(N+1)
    max_length = 0
    # 순회 시작 위치에 따라서 경로길이가 달라질 수 있음
    # 모든 정점에 대해 각 정점마다 시작점으로 잡고 DFS했을 때 최고길이 구하기
    for i in range(1,N+1):
        # 모든 정점에서 순회 시작
        dfs(i,1)
    print("#{} {}".format(tc, max_length))