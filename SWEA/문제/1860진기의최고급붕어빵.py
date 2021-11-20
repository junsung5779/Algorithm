T = int(input())
for tc in range(1, T+1):
    # N : 오는 사람의 수
    # M : 붕어빵이 만들어지는데 걸리는 시간
    # K : 한번 만들때 생기는 붕어빵의 수
    N, M, K = map(int, input().split())
    # S : S초가 지났을 때 사람이 온다.
    S = list(map(int, input().split()))
    S.sort()
    #남은 붕어빵의 수
    cnt = 0
    # 손님순서
    idx = 0
    for i in range(S[-1]+1):
        # 0은 나머지가 0으로 나오기 때문에 제외
        if i != 0:
            if i%M == 0:
                cnt += K

        # 첫 번째 손님이 올 시간
        if i == S[idx]:
            # 남은 붕어빵이 없으면 출력하고 종료
            if cnt == 0:
                print("#{} {}".format(tc, "Impossible"))
                break
            # 붕어빵이 남아있는 경우
            else:
                cnt -=1
                idx +=1
        # 끝까지 다 돌았으면, 성공 출력
        if i == S[-1]:
            print("#{} {}".format(tc, "Possible"))