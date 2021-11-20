
def rec(n):
    # n이 10일 때
    if n==10:
        return 1
    # n이 20일 때
    elif n==20:
        return 3
    # n이 30보다 클 때
    elif n>=30:
        # n의 결과값 = (n-10의 결과값) + (n-20의 결과값)*2
        return rec(n-10) + rec(n-20)*2

# 테스트케이스를 입력받는다.
T = int(input())
# 테스트케이스를 순회하면서
for tc in range(1, T+1):
    # 가로 길이(N)를 입력받는다.
    N = int(input())
    # N의 결과값을 초기화한다.
    res = 0
    print("#{} {}".format(tc, rec(N)))
