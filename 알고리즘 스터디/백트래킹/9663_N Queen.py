import sys
sys.setrecursionlimit(10000)


# 퀸 끼리 영향을 끼치는 범위가 겹치는지 확인하는 함수
def check(x):
    for i in range(x):
        if col[x] == col[i] or abs(col[x]-col[i]) == x-i:   # 열이나 대각선이 겹치면 false, 대각선이 겹치는 경우는 두 좌표에서 행 - 행 == 열 - 열 인 경우이다.
            # col[x] == col[i] : x와 i가 같으면 같은 행에 위치하는 경우임 -> 공격 사정거리 내에 있음
            # col[x] - col[i] == x - i : 두 퀸의 좌표에 대해서 x2-x1 == y2-y1인 경우 기울기가 1 또는 -1이다 -> 즉, 같은 대각선 상에 있다.
            return False
    return True


def dfs(x):
    global res   # 재귀호출 시에도 해당 값은 바뀌어야 하기 때문에 글로벌 변수 설정
    # 각 행마다 퀸을 놓는 반복문
    for i in range(N):
        if not check(x):    # 행, 열, 대각선 체크
            return
    # 종료조건
    if x == N:  # 퀸을 다 배치했으므로
        res += 1    # 경우의 수가 1개 추가된다.
        return
    # 각 행마다 퀸을 놓는 반복문
    for i in range(N):
        col[x] = i  # x번째 행의 i번째 열에 퀸을 놓겠다
        dfs(x+1)    # 겹치지 않은 경우 백트래킹 하지 않고 다음 행으로 바로 넘어가기;
        # 겹치는 경우 for문 계속 ㄱㄱ(백트래킹)


N = int(sys.stdin.readline())
res = 0
col = [0]*N # 몇번째 줄에 몇번째 칸에 있냐 를 나타내는 배열
dfs(0)
print(res)