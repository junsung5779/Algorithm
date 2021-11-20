import sys
sys.stdin = open("input2.txt")

# 일단 세칸을 가보고 충전기가 없으면 한칸 뒤로 간다
# 한칸 뒤로 간 후 충전기가 없으면 한칸 더 뒤로 간다.
# 한칸 뒤로 간 후 충전기가 없으면 내가 갈 수 있는 곳이 없으므로 0을 출력한다.
T = int(input())

for tc in range(1, T+1):
    # K : 이동할 수 있는 거리
    # N : 마지막 종점의 위치
    # M : 충전소의 개수
    K, N, M = map(int, input().split())

    charge = list(map(int, input().split()))

    bus_stop = [0]*(N+1)

    # 충전소를 표시하자.!
    # for i in range(M):
    #    bus_stop[charge[i]] = 1
    for i in charge:
        bus_stop[i] = 1

    bus = 0 # 버스 위치
    ans = 0 # 충전 횟수

    while True:
        # 버스가 이동할 수 있는 만큼 이동을 하자.
        bus += K
        if bus >= N : break # 종점에 도착하거나, 종점지보다 더 나아간 경우

        for i in range(bus, bus-K, -1):
            # if bus_stop[i] == 1:
            if bus_stop[i]:
                # 충전기가 있으면 충전을 하고
                ans += 1
                # 버스의 현재 위치를 i값으로 갱신
                bus = i
                break
        # 충전기를 못찾았을 때
        else:
            ans = 0
            break

    print("#{} {}".format(tc, ans))