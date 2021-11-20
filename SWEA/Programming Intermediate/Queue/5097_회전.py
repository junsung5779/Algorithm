import sys
sys.stdin = open("input5097.txt")

def pnp(): #팝하고 푸쉬하고
    # M번 반복하며
    for m in range(M):
        a = arr.pop(0)
        arr.append(a)
    return arr[0]


T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    # 테스트케이스를 입력받는다.
    arr = list(map(int, input().split()))
    print("#{} {}".format(tc, pnp()))