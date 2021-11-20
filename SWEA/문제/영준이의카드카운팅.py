import sys
sys.stdin = open("input영준이의카드카운팅.txt")

def check_card():
    for i in range(4):
        for j in range(1, 13+1):
            if count[i][j] > 1: #중복될 때
                return 0
            elif count[i][j] == 1: # 해당 무늬카드 세기
                ans[i] += 1
    return 1

# 테스트케이스 갯수를 입력받는다.
T = int(input())
# 테스스케이스 갯수를 순회하면서
for tc in range(1, T+1):
    count = [[0]*14 for _ in range(4)]
    card = input()
    ans = [0]*4
    flag = 1

    for i in range(0, len(card), 3):
        row = 0
        sdhc = card[i]
        col = int(card[i+1]+card[i+2])

        if sdhc == 'S': row = 0
        elif sdhc == 'D': row = 1
        elif sdhc == 'H': row = 2
        elif sdhc == 'C': row = 3

        count[row][col] += 1

    flag = check_card()
    print("#{}".format(tc), end=" ")
    if flag == 0: print("ERROR", end=" ")
    else:
        for i in range(4):
            print(13-ans[i], end=" ")
    print()