import sys
sys.stdin = open("input파리퇴치.txt")

# M <= N이다.
# 테스트케이스 받기
T = int(input())
# MxM크기의 파리채를 NxN배열안에서 내리친다.
for tc in range(1, T+1):
    N, M = map(int, input().split())
    # 2차원배열로 파리의 배치를 내려받는다
    mylist = [list(map(int, input().split())) for _ in range(N)]
    sum_max = 0
    # 좌상단의 좌표를(0,0)부터 시작해서 (N-M+1,N-M+1)까지 순회하면서
    for r in range(N-M+1):
        for c in range(N-M+1):
            sum = 0
            for i in range(r, r+M):
                for j in range(c, c+M):
                    sum += mylist[i][j]
            if sum_max < sum:
                sum_max = sum
    print('#{} {}'.format(tc, sum_max))
    # 좌상단의 좌표(x,y)를 기점으로 (x,y)부터 (x+M, y+M)까지 NxN배열의 인덱스에 해당하는 값의 합을 구한다.
    # 최댓값과 현재값을 비교해서 현재 값이 최댓값보다 더 크면 최댓값이 갱신된다.