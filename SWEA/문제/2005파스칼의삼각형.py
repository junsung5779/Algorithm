T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # 바로 출력하지 않고 N*N 배열에 넣어서 출력
    arr = [[0]*N for _ in range(N)]
    for i in range(N):
        # 자기 행 번호와 같은 열 까지만 나타낼거임
        for j in range(i+1):
            if j==0 or i==j:
                arr[i][j] = 1
            else:
                # 내 위에 숫자랑, 왼쪽 위 숫자 더하기
                if i > 0 and j > 0:
                    arr[i][j] = arr[i-1][j] + arr[i-1][j-1]

    print("#{}".format(tc))
    for i in range(N):
        for j in range(i+1):
            print(arr[i][j], end=" ")
        print()