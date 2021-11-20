# a = round(3.1234567, 6) # 3.123457


def max_percent(data,i,j):
    global N,r,c
    max = 0
    res = list()
    used = [[0]*N for _ in range(N)]
    # 0,0부터 N-1,N-1 인덱스까지의 이차원배열의 순열을 생성
    i,j = 0,0
    while True:
        for r in range(i,N):
            for c in range(j,N):

                res.append(data[r][c])


for tc in range(1,int(input())+1):
    i,j = 0,0
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 1행 1열부터 r행c열까지 계산
