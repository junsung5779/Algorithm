import sys
sys.stdin = open("input스도쿠.txt")


def sudoku(arr):
    global flag

    # 행검사
    for i in range(9):
        count = [0] * (9 + 1)
        for j in range(9):
            count[arr[i][j]] += 1
            if count[arr[i][j]] > 1:
                flag = 0
                return

    # 열검사
    for i in range(9):
        count = [0] * (9 + 1)
        for j in range(9):
            count[arr[j][i]] += 1
            if count[arr[j][i]] > 1:
                flag = 0
                return
    # 3 x 3
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            count = [0] * (9 + 1)
            for x in range(3):
                for y in range(3):
                    count[arr[i + x][j + y]] += 1
                    if count[arr[i + x][j + y]] > 1:
                        flag = 0
                        return


T = int(input())
for tc in range(1, T + 1):
    flag = 1  # 스도쿠아니면 0으로
    arr = [list(map(int, input().split())) for _ in range(9)]

    sudoku(arr)
    print("#{} {}".format(tc, flag))