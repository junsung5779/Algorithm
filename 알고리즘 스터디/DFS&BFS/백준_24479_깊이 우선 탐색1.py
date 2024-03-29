import sys
sys.setrecursionlimit(10 ** 6)  # 재귀 허용 깊이를 수동으로 늘려주는 코드

##### 무한루프 안타게 하기 위해서 방문 했던 곳을 체크하는 로직을 같이 작성하는 생각을 하도록 하자. #####
##### 푼 문제를 안보고 최대한 똑같이 다시 짜보기 #####

# 정점의 수,간선의 수,시작 정점
n, m, r = map(int, sys.stdin.readline().split())
# 연결노드 그래프 초기화(1번노드와 인덱스 값이 같게 하기 위해서 n+1로 )
# [[],[],[],[],[],[]]
graph = [[] for _ in range(n + 1)]
# 방문 순서 그래프 초기화
visted = [0] * (n + 1)
# 순차 입력
cnt = 1

# 시작 정점을 방문했다고 표시한다.
# 시작 정점의 인접한 정점의 집합(인접한 정점의 번호를 오름차순으로 방문)
def dfs(graph, v, visted):
    global cnt  # 함수 밖에 있는 cnt값 사용
    # 방문할 때마다 순차 값 변경
    visted[v] = cnt
    # 연결된 노드 방문
    for i in graph[v]:
        # 방문 안한 노드일 경우
        if visted[i] == 0:
            # 순차 증가(오름차순으로 방문해야 하기 때문)
            cnt += 1
            # dfs 실행
            dfs(graph, i, visted)


# 연결된 노드 입력 받기
for i in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

# 오름차순 정리
for i in range(n + 1):
    graph[i].sort()

dfs(graph, r, visted)
# 순차 출력
for i in range(n + 1):
    if i != 0:
        print(visted[i])