import sys
sys.stdin = open("input4.txt")

T = int(input())


for i in range(1, T+1):
    # 정수의 개수N과 구간의 개수M을 입력받는다
    N, M = map(int, input().split())
    # N개의 정수를 입력받는다.
    tc = list(map(int, input().split()))

    res_max = 0
    res_min = 0
    # 구간의 개수를 오버 하지 않기 위해 0~N-M까지 검사하면서
    for j in range(0,N-M+1):
        # res의 초기값을 설정해준다.
        res = 0
        # tc리스트의 j와 j+1, j+2.... j+M 번째 요소를 더해 res에 저장한다.
        for k in range(j, j+M):
            res += tc[k]
        # res에 다 저장하고 난 후

        # 만약 최솟값이 0일 경우 res값은 최솟값에 저장된다.
        if res_min == 0:
            res_min = res
        # 만약 res값이 최솟값보다 크고 최댓값이 0이라면 res값은 최댓값에 저장된다.
        elif (res > res_min) and (res_max == 0):
            res_max = res
        # 만약 res값이 최솟값보다 작으면
        elif res < res_min:
            # 만약 최댓값이 0일 경우
            if res_max == 0:
                # 기존의 최솟값은 최댓값에 저장되고
                res_max = res_min
                # res값은 최솟값에 저장된다.
                res_min = res
            # 만약 최댓값이 0이 아닌 경우
            else:
                # res값은 최솟값에 저장된다.
                res_min = res
        # 만약 res값이 최댓값보다 크다면
        elif (res > res_max):
            # res값은 최댓값에 저장된다.
            res_max = res
    # tc리스트의 0번째부터 N-M번째 리스트까지 검사를 마친 후
    # 최댓값과 최소값의 차이를 출력한다..
    print("#{} {}".format(i, (res_max)-(res_min)))