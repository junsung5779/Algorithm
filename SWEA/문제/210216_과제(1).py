#사다리1
import sys
sys.stdin = open("input210216.txt")
T = 10
for _ in range(1,T+1):
    tc = int(input())
    ladder = [list(map(int,input().split())) for _ in range(100)]
    #시작 지점 찾기 : r 이 0 인행 탐색하면서 1이면  출발
    #움직임에 대한 변화량 배열 선언
    dr = [1,0,0]
    dc = [0,1,-1]
    result = 0
    for i in range(100):
        if ladder[0][i] == 1:   # 1이면 출발
            #위치값을 가지고 있으면서 변화량을 더하는 형태로 이동할거임
            r = 0
            c = i
            dir = 0 #아래 방향 0 , 오른쪽방향 1, 왼쪽방향 2
            while r < 100:
            #움직이기 시작 ( while문으로 이동)
                #움직이는 방향을 지정해서 특정한 조건을 만족하면 방향 전환
            #마지막 도착 지점을 찾으면, 시작지점을 출력하면 됨
                if dir == 0:
                    #좌 우 확 인, 갈수 있는 길이 있으면, 방향전환
                    if  c - 1 >= 0 and ladder[r][c-1] == 1:
                        #왼쪽에 길이 있으니 왼쪽으로 방향 전환
                        dir = 2
                    elif c + 1 < 100 and ladder[r][c+1] == 1:
                        #오른쪽에 길이 있으니 오른쪽으로 방향전환
                        dir = 1
                elif dir == 1 or dir == 2 : # 오른쪽, 왼쪽으로 가고 있었음
                    #아래쪽으로 길이 있는지만 확인하면됨
                    if r+1 < 100 and ladder[r+1][c] == 1:
                        dir = 0

                #이동하려는 방향으로의 변화량을 더해주면됨
                r += dr[dir]
                c += dc[dir]
                if r == 99 and ladder[r][c] == 2:
                    result = i
                    break
                # print(r,c)

    print("#{} {}".format(tc,result))

