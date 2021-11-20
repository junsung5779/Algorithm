import sys
sys.stdin = open("input210219.txt")

#테스트케이스 개수를 입력받는다
T = int(input())

# 테스트케이스 개수만큼 순회하면서
for tc in range(1,T+1):
    # 각 테스트 케이스는 총 5줄로 이루어져있으므로
    # 5번 순회하면서
    # 입력값을 문자열로 받아 리스트형태로 저장한다.
    arr = [list(str(input())) for _ in range(5)]
    # 출력값 초기화
    res = ''
    # 입력받은 값을 세로로 세기 위해 열을 나중에 카운트한다
    for w in range(15):
        # 첫번째 행부터 마지막 행까지 순회하면서 결과값에 해당 인덱스에 위치하는 문자를 더해준다.
        for r in range(5):
            if w < len(arr[r]):
                res += arr[r][w]

    print("#{} {}".format(tc,res))
