T = int(input())
for tc in range(1, T+1):
    # N : 상자의 개수
    #
    N, Q = map(int, input().split())
    # 입력받은 N의 길이만큼 0을 집어넣는다
    arr = [0]*N
    # 1부터Q까지 순회하면서
    for i in range(1, Q+1):
        # L과 R을 입력받아서
        L, R = map(int, input().split())
        # L-1 부터 R까지 범위를 잡고 순회하면서
        for j in range(L-1, R):
            # arr의 해당 인덱스에 i를 집어넣는다.
            arr[j] = i
    # print("#{} {}".format(tc, *arr))
    print("#{}".format(tc), *arr)