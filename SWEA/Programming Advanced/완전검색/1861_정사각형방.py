import sys
sys.stdin = open("input_1861.txt")


def BFS(lst):
    # 만약
    # 리스트 전체를 돌면서
    for i in range(N):
        for j in range(N):
            # 사방으로 뻗어나간다
            pass
    return

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [[0]*(N+2) for _ in range(N+2)]
    room = [list(map(int, input().split())) for _ in range(N)]
    for i in range(1,N+1):
        for j in range(1, N+1):
            arr[i][j] = room[i-1][j-1]
    print(arr)