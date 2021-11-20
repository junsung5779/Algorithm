import sys
sys.stdin = open("input2.txt")


# K : 한번 충전으로 최대한 이동할 수 있는 정류장 수
# N : 종점의 위치
# M : 충전기가 설치된 정류장의 개수

# Logic
# 나타내야 할 노선의 수는 T개이다.
T = int(input())

# 첫번째 노선부터 T번째 노선까지 반복문을 돌린다.
for j in range(1, T+1):
    # K, N, M을 나타내는 리스트
    K, N, M = map(int, input().split())
    # 충전기가 설치된 정류장을 나타내는 리스트
    busstop = list(map(int, input().split()))
    # 충전기가 설치된 정류장을 나타내는 리스트를 처음부터 끝까지 한번 반복한다.
    # 0부터 시작해서 출발한다.
    now = 0
    # 충전 횟수 초기화
    # now가 testcase리스트의 요소다.
    # [1, 2, 3, 4]
    # 그 다음과 그 다다음 정류장과 비교를 한다.
    # 만약에 now가 3이라면 그 다다음을 넣을때 인덱스 오류가 난다.
    # now가 리스트 내의 위치에서 맨 마지막과 맨 마지막 전의 리스트가 아닐 경우 정상적으로 코드를 실행한다.
    # 마지막과 마지막 전 정류장일 경우
    # now가 리스트의 몇번째에 위치하는지를 알고싶습니다.
    count = 0
    for i in range(len(busstop)):
        # 만약 3에서 충전했으면 3+K까지 갈 수 있으므로 현재 정류장과 다음 정류장 사이의 거리가 K 이하이면 충전횟수를 한번 더한다.
        # 인덱스 오류를 없애기 위해 i의 범위를 (리스트 길이-2)까지 지정해준다
        if ((busstop[i]-now) <= K) and (i < len(busstop)-2):
            # busstop [1,2,3,4,5]
            # i = 0,1,2,3,4
            # i= 4  5-2
            # 현재 정류장에서 충전을 하고 K만큼 이동하는 사이에 충전기가 있는 정류장(들)을 지나친다면??
            #
            if busstop[i+2] - busstop[i] <= K:
                now = busstop[i+2]
                continue
            else:
                count += 1
                now = busstop[i]
        elif ((busstop[i]-now) <= K) and (i >= len(busstop)-2):
            if busstop[i] < N:
                continue
            else:
                count=0
                break

        # # 현재 정류장과 다음 정류장 사이의 거리가 K+1이상이면 0을 출력한다.
        # elif (busstop[i]-now) >= K+1:
        #     count = 0
        #     break
        # # 마지막 충전기가 설치된 정류장과 종점 사이의 거리가 K+1이상이면 0을 출력한다
        # elif (busstop[i]-M) >= K+1:
        #     count = 0
        #     break

    print("#{} {}".format(j, count))

