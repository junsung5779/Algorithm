# 연습문제3
data = [1,2,1,3,2,4,2,5,4,6,5,6,6,7,3,7]
# 정점의 개수
V = 7
# 간선의 개수
E = 8
adj = [[0]*(V+1) for _ in range(V+1)]
for i in range(0, E*2,2):
    a,b = data[i], data[i+1]
    adj[a][b] = 1
    adj[b][a] = 1

# 시작 노드로부터 같은 거리에 있는 정점을 모두탐색 후
# 거리를 늘려서 탐색
# s: 시작정점
def bfs(s):
    # bfs는 먼저 방문한 정점이 먼저 버려진다.
    queue = list()
    # 한번 방문한 정점을 확인하기 위한 visited
    visited = [0]*(V+1)
    # 큐에 시작지점 집어넣고
    queue.append(s)
    # 방문처리하기
    visited[s] = 1
    #1. queue에서 가장 먼저 방문한 정점을 방문: queue에서 가장 앞에 있는 정점을 방문
    #2. 해당 정점에서 방문할 수 있는 모든 경로를 저장: queue에 순서대로 넣어줌
    #3. 1~2번을 queue가 빌때 까지 반복한다.
    while queue:
        # queue에서 가장 앞에 있는 정점을 가져옴
        front = queue.pop(0)
        # 방문순서를 출력
        print(front, end=" ")
        # front에서 갈 수 있는 경로를 탐색
        for i in range(1,V+1):
            # 인접행렬이 1이면, 경로가 있는것, 방문하지 않은 정점을 방문해야함
            if adj[front][i] == 1 and not visited[i]:
                # 정점을 방문하고
                queue.append(i)
                # 해당 위치에 방문표시
                visited[i] = 1
    # 줄내림
    print()

bfs(1)