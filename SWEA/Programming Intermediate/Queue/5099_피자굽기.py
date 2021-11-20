import sys
sys.stdin = open("input5099.txt")

def pizza(C):
    # 입력받은 피자 순서대로 번호를 부여한다.
    lst = list()
    for m in range(M):
        lst.append((C[m],m+1))

    # 화덕에 일단 피자를 꽉 채운다
    duck = list()
    for k in range(N):
        duck.append(lst.pop(0))
    # 화덕에 남아있는 피자의 갯수가 1개가 될 때까지 조건문을 반복한다.
    while len(duck) > 1:
        print(duck)
        # 다 안녹았을 경우 빼지 않고 치즈양을 절반으로 줄여서 화덕의 맨 뒤로 보낸다.
        a = duck.pop(0)
        b = (a[0]//2,a[1])
        if b[0] != 0:
            duck.append(b)

        # 화덕에 자리가 남고 더 넣을 피자가 있을경우에 화덕에 피자를 집어넣는다.
        if len(duck) < N and len(lst) > 0:
            duck.append(lst.pop(0))

    return duck[0][1]




T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    C = list(map(int, input().split()))
    result = pizza(C)
    print("#{} {}".format(tc, result))