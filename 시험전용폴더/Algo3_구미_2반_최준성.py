
def prim(start_vertex):
    # 최소 가중치의 합 초기화
    res = 0
    # 가중치를 저장하는 리스트
    weight = [INF]*V
    # 시작정점의 가중치를 0으로 초기화
    weight[start_vertex] = 0
    # 방문여부 확인
    visited = [0]*V
    # 간선을 순회하면서
    for i in range(V):
        # 최소가중치 초기화
        min_w = INF
        # 최소가중치 인덱스 초기화
        min_v = 0
        for j in range(V):
            # 만약 정점이 서로 연결되어 있고, 방문하지 않은 상태라면
            if weight[j] < min_w and not visited[j]:
                # 최소가중치 갱신
                min_w = weight[j]
                # 최소가중치를 가진 정점 갱신
                min_v = j
        # 최소 가중치를 결과값에 더하기
        res += min_w
        # 방문표시
        visited[i] = 1

        # 최소비용 간선을 가진 정점 갱신
        for k in range(V):
            # 만약 해당 정점의 가중치가 현재 최소가중치보다 작고 방문하지 않았을 경우
            if adj[min_v][k] < weight[k] and not visited[k]:
                # 해당 간선의 최소가중치 갱신
                weight[k] = adj[min_v][k]
    # 결과값 반환
    if M >= res:
        return M-res
    else:
        return -1





for tc in range(1,int(input())+1):
    V,E,M = map(int, input().split())
    INF = 0xfffffff
    adj = [[INF]*V for _ in range(V)]
    for i in range(E):
        # 시작도시, 도착도시, 가중치를 받는다
        s,e,w = map(int, input().split())
        s -= 1
        e -= 1
        # 무방향이므로 대칭행렬이 되도록 값을 저장한다.
        adj[s][e] = w
        adj[e][s] = w
    print(prim(0))