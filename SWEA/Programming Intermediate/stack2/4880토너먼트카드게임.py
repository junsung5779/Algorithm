import sys
sys.stdin = open("input4880.txt")

# 그룹을 두 개로 나누어서 승자를 뽑기
# 그룹이 (2명으로 이루어지거나 또는) 한 명으로 이루어 질 때까지
# 그룹을 나누어 주고, 각각의 승자를 뽑아야 한다.

# 하나의 그룹을 두 그룹으로 나누어서
# 각각의 승자 중 승자를 반환하는 함수
def game(s,e):
    # 전체 그룹을 두 그룹으로 나누고
    # 각 절반의 승자를 뽑아서
    # 승자끼리 결과를 반환
    # 재귀는 그룹에 포함되는 학생이 한 명이면, 재귀 호출 중단
    if s == e:
        # 승자는 본인
        return s

    center = (s+e)//2
    # s부터 center까지의 승자
    v1 = game(s,center)
    # center+1부터 e까지의 승자
    v2 = game(center+1,e)
    # v1과 v2중에 승자 뽑기
    if cards[v1] == '1':      # v1이 가위인 상황
        if cards[v2] == '2':
            return v2
        # v2가 가위나 보자기인 경우에는 전부 v1으로 반환된다.
        else:
            return v1
    elif cards[v1] == '2':    # v1이 바위인 상황
        if cards[v2] == '3':
            return v2
        else:
            return v1

    else:                   # v1이 보자기인 상황
        if cards[v2] == '1':
            return v2
        else:
            return v1

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    #  0  1  2  3  4  5  6  7
    # [1][2][2][1][3][3][1][1]
    # 학생의 번호가 1~N 까지인데, 인덱스는 0~N-1까지니까
    # 결과출력할 때 승자번호 +1 해주면 된다.
    cards = input().split()
    # game을 시작할 떄는 전체 범위를 이용해서 시작
    result = game(0, N-1)
    print('#{} {}'.format(tc, result+1))