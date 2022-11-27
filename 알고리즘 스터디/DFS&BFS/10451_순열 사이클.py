import sys
sys.setrecursionlimit(10000)    # 재귀 한도 설정하여 에러 방지

def dfs(V):
    visited[V] = 1  #방문한 곳 1로 표시
    next = arr[V]   # 다음 방문할 노드 지정
    if visited[next] == 0: #아직 방문하지 않은 곳인 경우
        dfs(next)

T=int(input())

for i in range(T):
    answer = 0  # 사이클의 갯수
    N = int(input())
    arr = [0] + list(map(int, input().split())) # 노드 입력받기
    visited = [0] * (N + 1) # 각 노드별 방문 여부

    # 이루어진 수의 갯수만큼 반복
    for i in range(1, N+1):
        # 방문하지 않은 곳이라면 dfsㄱㄱ뚠 하고
        if visited[i] == 0:
            dfs(i)
            answer += 1 # 사이클의 갯수 하나 늘리기
    print(answer) #순열 사이클의 개수