import sys
sys.stdin = open("input4836.txt")


# 테스트 케이스 갯수
for t in range(int(input())):
    # 칠할 영역의 갯수 받기
    n = int(input())
    # 10x10격자의 좌표 받아서 arr에 저장(0부터 10까지니 실제로는 11x11이 된다)
    arr = [[0 for _ in range(11)] for a in range(11)]

    # 겹치는 갯수 카운트
    cnt = 0
    # 칠할 영역의 갯수중 첫번째부터 마지막까지 반복문을 돌린다.
    for i in range(n):
        # x1, x2, y1, y2 좌표와 색상(color) 좌표를 순서대로 받는다.
        x1, y1, x2, y2, color = map(int, input().split())
        # 칠해진 영역의 색깔을 arr에 좌표로 저장한다.
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                arr[x][y] += color
                # 만약 빨강색과 파란색이 겹치는 경우(3이 저장된 경우) (color = 1 (빨강), color = 2 (파랑))
                if arr[x][y] == 3:
                    # 카운트 갯수를 하나 올린다.
                    cnt += 1

    print("#{} {}".format(t + 1, cnt))