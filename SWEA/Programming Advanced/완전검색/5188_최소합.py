import sys
sys.stdin = open("input5188.txt")

def dfs(r,c):
    down = right = N * 11  # 범위 밖 가상의 값

    # 마지막 지점에 다다랐을 때
    if r == c >= N-1:
        # 도착위치 반환
        return arr[r][c]
    # 마지막 지점이 아닐 경우
    else:
        if r < N-1:  # 아래쪽 끝이 아니면 아래로 한칸 이동
            down = dfs(r+1, c)
        if c < N-1:  # 오른쪽 끝이 아니면 오른쪽으로 한칸 이동
            right = dfs(r, c+1)

    # 이동이 끝난 후 가장 작은 값을 반환한다
    if down < right:
        return down + arr[r][c]
    else:
        return right + arr[r][c]

T = int(input())
for tc in range(1, 1 + T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    print('#{} {}'.format(tc, dfs(0,0)))