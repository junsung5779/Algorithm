
# PRIM알고리즘
# 시작정점을 입력받는다.
def prim(start_vertex):
    # 최소신장트리의 가중치 결과값 초기화
    res = 0
    # 가중치 저장 배열 생성
    weight = [INF]*V
    # 시작정점의 가중치는 0으로 초기화
    weight[start_vertex] = 0
    # 방문체크 배열 생성
    visited = [0]*V
    # 노드의 연결관계 배열 생성
    st = [-1]*V
    # 최소 가중치를 찾아내서 결과값에 더하는 반복문
    for i in range(V):
        # 최소 가중치의 초기값을 1e9로 한다.
        min_w = INF
        # 최소 가중치를 가지는 정점의 번호를 초기화한다.
        min_v = 0
        # 방문하지 않았고, 가중치가 최소인 경우를 탐색하여 조건에 부합하면 최소가중치 갱신
        for j in range(V):
            if not visited[j] and weight[j] < min_w:
                min_w = weight[j]
                min_v = j
        # 최소가중치를 구한 다음 결과값에 해당 최소가중치를 더함
        res += min_w
        # 해당정점에 방문체크
        visited[min_v] = 1

        # 선택한 정점의 인접 정점의 가중치중 최솟값을 가진 가중치로 업데이트
        for k in range(V):
            # 만약 k번째에 있는 정점이 min_v번째 정점과 연결이 되어있고(연결이 안되어 있다면 adj[min_v][k] = INF), 방문하지 않은 상태라면.
            if adj[min_v][k] < weight[k] and not visited[k]:
                # K번째 정점과 도작정점사이의 가중치를 저장한다(여기서는 K번째 정점은 인덱스이다. 도착정점은 min_v번째 정점이나)
                weight[k] = adj[min_v][k]
                # weight처럼 인덱스 자체를 정점으로 사용하기 떄문에 st의 K번째 인덱스에 저장되어 있는 번호가 weight의K 번째 정점의 도착번호이다.
                st[k] = min_v
    return res




# 테스트케이스를 입력받는다.
for tc in range(1,int(input())+1):
    # 테스트케이스 별로 첫 줄에 마지막 노드번호 V와 간선의 개수 E가 주어진다.
    V,E = map(int, input().split())
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