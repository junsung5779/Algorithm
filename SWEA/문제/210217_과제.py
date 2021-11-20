import sys
sys.stdin = open("input210217.txt")

T = int(input())

# 정렬용 알파벳
num = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

for tc in range(1, 1 + T):

    n = list(map(str, input().split()))

    # 무작위 숫자 리스트
    num_list = list(map(str, input().split()))

    # 결과 저장용
    res = []
    # num에 저장되어있는 리스트에 나온요소를 모두 사용하기 위해 0~9까지 순회한다.
    for a in range(10):
        # 무작위 숫자 리스트를 순회하면서
        for b in num_list:
            # num의 a번째 인덱스의 값과 b가 같다면
            if num[a] == b:
                # 결과 리스트에 b를 추가한다.
                res.append(b)

    print('#{}'.format(tc))
    print(*res)