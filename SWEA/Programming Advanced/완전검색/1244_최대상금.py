import sys
sys.stdin = open("input1244.txt")

def dfs(d, cnt):
    global max_num
    if cnt == n:
        max_num = max(int("".join(num)), max_num)
        return
    for i in range(d, l):
        for j in range(i+1, l):
            if num[i] <= num[j]:
                num[i], num[j] = num[j], num[i]
                dfs(i, cnt + 1)
                num[i], num[j] = num[j], num[i]

T = int(input())
for tc in range(1, T + 1):
    num, n = input().split()
    num = list(num)
    numbers = num[:]
    # 입력받은 값을 정수형으로 변경
    n = int(n)
    l = len(num)
    max_num = 0
    tmp = 0
    # 입력받은 문자열의 길이가 2이거나 입력받은 문자열을 내림차순으로 정렬한것이 같으면
    if len(num) == 2 or num == sorted(num, reverse=True):
        # 카운트 = 0
        cnt = 0
        # 교환횟수를 다 사용하지 않았다면
        while cnt != n:
            # 교환해주고
            numbers[-1], numbers[-2] = numbers[-2], numbers[-1]
            # 카운트 1회 증가
            cnt += 1
        tmp = int("".join(numbers))
    cnt = 0
    dfs(0, cnt)
    if max_num == 0:
        max_num = tmp
    print("#" + str(tc) + " " + str(max_num))