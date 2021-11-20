import sys
sys.stdin = open('prim_input.txt')

def prim(start_vertex):
    # 최소 신장 트리의 가중치 결과
    result = 0

    #2. 가중치 저장 배열 생성
    weight = [INF]*V
    weight[start_vertex] = 0

    #3. 방문 체크 배열 생성
    visited = [0]*V

    #4. 노드의 연결관계 배열 생성
    st = [-1]*V

    #5. 최소 가중치 탐색&결과값에 더하는 반복문
    for _ in range(V):
        min_w = INF
        min_v = 0
        #5-1. 방문하지 않았고 가중치가 최소인 경우를 탐색하여 최소key의 가중치 찾기
        for i in range(V):
            if weight[i] < min_w and not visited[i]:
                min_w = weight[i]
                min_v = i

        #5-2. 최소 가중치 값 연산, 방문 체크
        result += min_w
        visited[min_v] = 1

        #5-3. 선택한 정점의 인접 정점의 가중치를 최단 가중치로 업데이트
        for i in range(V):
            #7-1. 기존에 있던 가중치보다 더 작은 가중치일 경우이고 아직 방문하지 않았을 경우,
            if adj[min_v][i] < weight[i] and not visited[i]:
                # 현재 vertex와 이어진 간선의 가중치가 최솟값이므로 갱신
                weight[i] = adj[min_v][i]
                st[i] = min_v

    return result


for tc in range(1, int(input()) + 1):
    V, E = map(int, input().split())
    INF = 1e9

    # 1. 가중치(간선)를 저장하는 인접행렬 생성, 값 입력하기
    adj = [[INF] * V for x in range(V)]

    for i in range(E):
        s, e, w = map(int, input().split())
        adj[s][e] = w
        adj[e][s] = w
    print(prim(0))