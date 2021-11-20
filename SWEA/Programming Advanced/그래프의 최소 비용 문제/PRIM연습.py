
# PRIM알고리즘
# 시작정점을 입력받는다.
def prim(start_vertex):
    # 최소신장트리의 가중치 결과값 초기화
    res = 0
    # 각 정점의 가중치 초기화
    weight = [INF]*V
    # 방문여부 초기화
    visited = [0]*V
    st = [-1]*V
    # 모든 노드를 순회하면서
    for i in range(V):
        # 최소가중치 초기화
        min_w = INF
        # 최소가중치정점인덱스 초기화
        min_v = 0
        for j in range(V):
            if weight[j] < min_w and not visited[j]:
                min_w = weight[j]
                min_v = j
        res += min_w
        visited[min_v] = 1
        for k in range(V):
            if adj[min_v][k] < weight[k] and not visited[k]:
                weight[k] = adj[min_v][k]
                st[k] = min_v
    return res





# 테스트케이스를 입력받는다.
for tc in range(1,int(input())+1):
    # 테스트케이스 별로 첫 줄에 마지막 노드번호 V와 간선의 개수 E가 주어진다.
    V,E = map(int, input().split())
    # 0번부터 V번까지 있으므로 V+=1해준다.
    V += 1
    # E개의 줄에 걸쳐 간선의 양 끝 노드와 가중치를 입력받는다.
    INF = 0xfffffff
    # 가중치가 무한인 인접행렬을 만든다
    adj = [[INF]*V for _ in range(V)]
    # 간선의 개수만큼 순회하면서
    for i in range(E):
        # s: 시작정점
        # e: 도착정점
        # w: 가중치
        s,e,w = map(int, input().split())
        # 인접행렬의 s행e열의 가중치를 w로 만든다
        # s와e가 이어졌을 뿐만 아니라 해당 간선의 가중치까지 한번에 등록됨
        # 따라서 해당 간선이 INF면 연결이 안되었다는 뜻임
        adj[s][e] = w
        # 무향 그래프이기 때문에 대칭행렬의 형태가 되야한다.
        adj[e][s] = w
    print("#{} {}".format(tc, prim(0)))