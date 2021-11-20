import sys
sys.stdin = open("input4839.txt")

# 페이지를 찾는 함수
def find_cnt(page,target):
    # 시작페이지
    s = 1
    # 마지막 페이지
    e = page
    # 중간값
    c = int((s+e)/2)
    # center에 위치한 숫자가 내가 찾는 숫자가 아니면 계속 찾는것을 반복
    cnt = 1
    while c != target:
        if target > c:
            s = c
        else:
            e = c
        cnt += 1
        c = int((s+e)/2)
    return cnt


# 테스트 케이스 개수를 정수로 입력받는다.
T = int(input())
# 1부터 T까지 반복한다.
for tc in range(1,T+1):
    P, A, B = map(int, input().split())
    result_a = find_cnt(P,A)
    result_b = find_cnt(P,B)
    # 승자 초기화
    winner = '0'
    if result_a > result_b:
        winner = 'B'
    elif result_a < result_b:
        winner = 'A'
    print('#{} {}'.format(tc, winner))



    # A의 탐색횟수와 B의 탐색횟수를 비교하여 이긴사람(탐색횟수가 더 적은 사람)을 출력하고 비길 경우(탐색횟수가 같을 경우) 0을 출력한다.
