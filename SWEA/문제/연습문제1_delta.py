def getAbs(num):
    if 0<=num:
        return num
    else:
        return -num

arr = [[1, 2, 3, 4, 5],
       [1, 2, 3, 4, 5],
       [1, 2, 3, 4, 5],
       [1, 2, 3, 4, 5],
       [1, 2, 3, 4, 5]
       ]
N = 5
# 상 하 좌 우 방향으로 탐색
dr = [-1,1,0,0]
dc = [0,0,-1,1]
for i in range(len(arr)):
    for j in range(len(arr[i])):
        # 사방에 있는 값들과의 차이의 절대값의 합 구하기
        # 사방에 있는 애들 하나씩 접근하기
        sum_v = 0 # 각 요소마다 합을 구해야 하니까.

        for d in range(4):
            nr = i+dr[d]
            nc = j+dc[d]
            # 정상적인 좌표 값일 때만 사용하자!
            if 0<= nr <N and 0<= nc <N:
                # 원래 요소와의 차이의 절대값 구하기
                sum_v += getAbs(arr[i][j] - arr[nr][nc])
        print(sum_v, end=' ')
    print()