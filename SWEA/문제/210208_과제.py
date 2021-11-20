import sys
sys.stdin = open("input210208.txt")

# 10개의 테스트 케이스를 반복하면서
for tc in range(1, 11):
    # 테스트케이스의 길이를 입력받고
    N = int(input())
    # 테스트케이스를 입력받는다.
    M = list(map(int, input().split()))
    # 결과값을 초기화한다.
    res = 0
    # 맨 왼쪽 두 칸과 맨 오른쪽 두 칸은 건물이 지어지지 않으므로 제외한다.
    for k in range(2, N-2):
        if M[k-2] > M[k-1]:
            left = M[k-2]
        else:
            left = M[k-1]
        if M[k+2] > M[k+1]:
            right = M[k+2]
        else:
            right = M[k+1]

        # 만약 해당 건물의 높이가 좌, 우 2칸이내의 건물들 중 가장 높을 경우
        if M[k] > left and M[k] > right:
            # 왼쪽 최고높이가 오른쪽 최고 높이보다 높을 경우
            if left > right:
                # 확보된 조망권을 결과값에 더한다.
                res += M[k]-left
            else:
                res += M[k]-right
    print("#{} {}".format(tc, res))