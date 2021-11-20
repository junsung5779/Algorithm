import sys
sys.stdin = open("input그래프경로.txt")

def dfs(start, end):
    stack = []
    # 방문한 노드 리스트 초기화
    visited = [0]*(V+1)
    # stack 리스트의 마지막에 시작노드번호 추가
    stack.append(start)
    # 입력받은 시작노드(start)부터 시작, 값이 있고 아직 방문하지 않은 정점이면 stack에 추가
    # stack이 0보다 클 때
    while stack:
        # stack 리스트의 마지막 인덱스에 있는 값을 하나 제거하고 제거한 값을 i에 저장한다
        i = stack.pop()
        # 방문한 노드 리스트의 i번째 인덱스에 1을 저장한다.
        visited[i] = 1
        # 열을 순회하면서
        for j in range(V+1):
            # 만약 방문한 노드가 아니고
            # visited의 j번째 인덱스에 저장된 값이 0이고
            if not visited[j]:
                # 
                # arr배열의 해당 인덱스에 있는 값이 0보다 크다면
                if arr[i][j]:
                    # stack 리스트의 마지막에 j를 추가한다.
                    stack.append(j)
    # 도착노드에 도착하였는지 반환
    # end 지점을 방문하였는지 반환
    # visited 리스트에서 end에 저장된 값의 인덱스의 값을 반환
    return visited[end]

# 테스트케이스 입력값을 받는다.
T = int(input())
# 테스트 케이스 입력값을 순회하면서
for tc in range(1, T+1):
    # V와 E를 입력받는다.
    # V: 노드갯수
    # E: 간선갯수
    V, E = map(int, input().split())
    # 이차원 배열을 초기화한다.
    # 0행과 0열은 사용하지 않기 때문에 range(V+1)해준다.
    arr = [[0]*(V+1) for _ in range(V+1)]
    # E개의 줄에 걸쳐, 출발 도착 노드로 간선정보를 입력받는다
    # 입력받은 출발 도착 노드를 V*V크기의 이차원배열에 좌표값으로 넣는다.
    for a in range(E):
        r, c = map(int, input().split())
        arr[r][c] = 1
    result = 1

    # E개의 줄 이후에는 경로의 존재를 확인할 출발노드 S와 도착노드 G가 주어진다.
    S, G = map(int, input().split())
    # 입력받은 출발노드(S)와 도착노드(G)가 연결되어있는지 확인
    if not dfs(S,G):
        result = 0
    print("#{} {}".format(tc, result))