# 1. 연산자 N개를 가지고 나올 수 있는 모든 조합을 구해야 한다. 또는 DFS를 이용해 최대, 최솟값을 구한다.
# 2. 해당 조합으로 나온 순서대로 계산한 결과값의 최소, 최대값을 갱신해준다.
# 3. 출력쓰~

N = int(input())    # 숫자 개수
num = list(map(int, input().split()))   # 숫자 목록
operator = list(map(int, input().split()))  # 연산자 목록

max_num = -1e9
min_num = 1e9


def dfs(depth, total, plus, minus, multiply, divide):
    global max_num, min_num # 재귀호출 시에도 해당 최소, 최댓값은 바뀌어야 하기 때문

    # 연산자 N개를 모두 사용한 경우(마지막 숫자에 도달한 경우)
    if depth == N:
        if total > max_num:
            max_num = total
        if total < min_num:
            min_num = total
        return

    # 사용해야 할 연산자가 남아 있는 경우
    # 남은 연산자의 총 갯수를 -1하고, 해당 연산을 하고, 해당 연산자의 남은 숫자를 -1함
    if plus:
        dfs(depth+1, total + num[depth], plus-1, minus, multiply, divide)
    if minus:
        dfs(depth+1, total - num[depth], plus, minus-1, multiply, divide)
    if multiply:
        dfs(depth+1, total * num[depth], plus, minus, multiply-1, divide)
    if divide:
        dfs(depth+1, int(total/num[depth]), plus, minus, multiply, divide-1)    # 정수 나눗셈으로 몫만 취함 (문제에 나와있음 ㅇㅇ)


dfs(1, num[0], operator[0], operator[1], operator[2], operator[3])
print(max_num)
print(min_num)