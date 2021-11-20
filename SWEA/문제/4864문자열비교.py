import sys
sys.stdin = open("input4864.txt")
T = int(input())
for tc in range(1, T+1):
    # 문자열 1을 입력받는다.
    N1 = str(input())
    # 문자열 2를 입력받는다.
    N2 = str(input())
    # 카운트 초기값을 설정한다.
    cnt = 0
    # 문자열 1이 2에서 반복하는 총 반복 시작범위는 0~ len(문자열2)-len(문자열1)+1까지
    for i in range(0,len(N2)-len(N1)+1):
        # 문자열 1의 길이를 비교 범위로 지정해서
        # 문자열 2의 비교범위는 i ~ i+len(문자열1)까지 지정 한 후
        if N1[:len(N1)] == N2[i:i+len(N1)]:
            # 비교를 해서 같다면 카운트를 1회 증가시킨다.
            cnt += 1
    print("#{} {}".format(tc, cnt))
