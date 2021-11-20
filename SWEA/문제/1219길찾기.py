# V : 현재 탐색중인 노드의 번호
def dfs(V):
    # V 노드를 방문했음을 표시
    visited[V] = 1
    if V == 99:
        # 도착지점에 도착을 했음!!
        return 1
    # 할 수 있는거 다해보기 path의 1번길, 2번길 살펴보기
    for i in range(2):
        if path[i][V] != -1 and not visited[path[i][V]]:
             if dfs(path[i][V]) == 1:
                 return 1
    return 0

for _ in range(10):
    tc, N = map(int, input().split())
    path = [[-1]*100 for _ in range(2)]
    edge = list(map(int, input().split()))
    #방문했음을 표시하는 배열
    visited = [0] * 100
    # 간선정보를 이용해서 path배열 채우기
    # 인덱스를 초과하지 않기 위해 (N*2)+1 가 아니라 N*2로 함
    for i in range(0,N*2,2):    # 입력값을 잘 봐라!
        # 만약에, 1번길이 비어있으면, 1번길에 넣어주고
        if path[0][edge[i]] == -1:
            path[0][edge[i]] = edge[i+1]
        # 1번길이 비어있지 않으면, 2번길에 넣음
        else:
            path[1][edge[i]] = edge[i+1]
    print("#{} {}".format(tc, dfs(0)))