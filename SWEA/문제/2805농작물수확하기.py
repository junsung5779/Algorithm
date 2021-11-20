import sys
sys.stdin = open("농작물")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]


    # 반으로 죽여버려!
    start = end = mid = N//2
    total = 0
    for i in range(N):
        for j in range(start, end+1):
            total += arr[i][j]
        if i < mid:
            start -= 1
            end += 1
        else:
            start += 1
            end -= 1
    print("#{} {}".format(tc, total))