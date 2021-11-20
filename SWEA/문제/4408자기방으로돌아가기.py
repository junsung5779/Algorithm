import sys
sys.stdin = open("input4408.txt")

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    S, E = list(), list()
    # 기본 이동 시간 1로 초기화
    cnt = 1
    cor = [0]*200
    for n in range(N):
        S1, E1 = list(map(int, input().split()))
        S.append(S1)
        E.append(E1)
    print(S,E)
    for i in range(N):
        for j in range(cor[S[i]-1], cor[E[i]-1]+1):
            cor[j] += 1

    cnt += max(cor)
    print("#{} {}".format(tc, cnt))