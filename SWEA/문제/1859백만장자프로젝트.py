import sys
sys.stdin = open("inputtest.txt")


# 테스트케이스횟수를 입력받는다
T = int(input())
# 테스트케이스횟수만큼 순회하면서
for tc in range(1, T + 1):
    # 자연수N을 받는다.
    N = int(input())
    # 각 날의 매매가를 나타내는 N개의 자연수들을 공백을 기준으로 받는다.
    arr = list(map(int, input().split()))
    # 최대이익을 초기화한다.
    res = 0
    # 가격이 같은 날이 연속된 수를 1로 초기화 한다.
    cnt = 1
    # 최댓값 초기화
    max_value = 0
    # arr을 뒤에서부터 순회하며
    for i in range(N-1, -1, -1):
        # 만약 max_value == 0 이라면
        if max_value == 0:
            # 현재값을 max_value에 저장한다.
            max_value = arr[i]

        # 만약 max_value != 0 이라면
        else:
            # 현재값이 max_value보다 작다면
            if arr[i] < max_value:
                # (max_value - 현재값) 을 최대이익(res)에 더한다.
                res += (max_value - arr[i])
            # 현재값이 max_value보다 크거나 같다면
            else:
                # 현재값을 max_value에 저장한다.
                max_value = arr[i]


    # 결과값 출력
    print("#{} {}".format(tc, res))