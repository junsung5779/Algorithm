import sys
sys.stdin = open("input3.txt")

T = int(input())

# 테스트 케이스 개수를 1~T까지 반복한다.
for tc in range(1,T+1):
    # N : 카드의 개수
    N = int(input())
    card = input()

    # count 배열 생성
    count = [0] * 10

    max_count = -1
    max_num = -1

    # 카드 숫자 세기
    for i in card:
        count[int(i)] += 1

    for i in range(len(count)):
        if max_count <= count[i]:
            max_num = i
            max_count = count[i]

    print("#{} {} {}".format(tc, max_num, max_count))