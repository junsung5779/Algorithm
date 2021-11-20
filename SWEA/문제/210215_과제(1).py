import sys
sys.stdin = open("input1209.txt")

# 테스트 케이스를 받는다.
T = 10
# 테스트 케이스만큼 반복한다.
for i in range(1, T+1):
    n = int(input())
    # 총 최댓값을 초기화한다.
    res = 0
    # 각 행의 합의 최댓값, 각 열의 합의 최댓값, 각 대각선의 합의 최댓값을 초기화한다.
    row_max, col_max, cross_max = 0,0,0
    # 100x100 2차원 배열을 받는다.
    # 숫자는 100개씩 받아 리스트 안에 하나의 리스트로 총 100개를 저장한다.
    mylist = [list(map(int, input().split())) for j in range(100)]
    # 각 행과 열의 합의 최댓값을 구해야 한다.
    # 행을 0~99번까지 반복한다.
    for a in range(100):
        #각 행의 합, 각 열의 합을 초기화한다.
        row, col = 0, 0
        # 열을 0~99번까지 반복한다.
        for b in range(100):
            # 하나의 행의 합을 구한다.
            row += mylist[a][b]
            #하나의 열의 합을 구한다.
            col += mylist[b][a]
        # 만약 구한 행의 값이 행의 최댓값보다 높으면
        if row >= row_max:
            # 구한 행의 값을 행의 최댓값으로 바꾼다
            row_max = row

        # 만약 구한 열의 값이 열의 최댓값보다 높으면
        if col >= col_max:
            # 구한 열의 값을 열의 최댓값으로 바꾼다
            col_max = col

    # 좌상 -> 우하 대각선의 합의 최댓값을 구한다.
    # 대각선의 합의 값을 초기화한다.
    cross = 0
    # 0~99까지 반복한다.
    for c in range(100):
        # 대각선의 합의 값이 현재는 하나뿐이므로 최댓값에 바로 저장한다.
        cross_max += mylist[c][c]
        # 99~0까지 반복한다.
        for d in range(99,-1,-1):
            # c와d의 합이 99이면
            if (c+d)==99:
                # 우상 -> 좌하 대각선의 해당 값을 더한다.
                cross += mylist[c][d]
        # 대각선의 합의 최댓값을 구한다.
        if cross >= cross_max:
            cross_max=cross

    # 나온 세개의 값중 최댓값을 구한다.
    if row_max >= col_max and row_max >= cross_max:
        res = row_max
    if col_max >= row_max and col_max >= cross_max:
        res = col_max
    if cross_max >= row_max and cross_max >= col_max:
        res = cross_max
    print("#{} {}".format(n, res))