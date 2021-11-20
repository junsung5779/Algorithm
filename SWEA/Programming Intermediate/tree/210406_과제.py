import sys
sys.stdin = open('input_210406.txt')


def cal(v):
    if 1 <= v <= N:
        # 현재 노드의 값이 사칙연산이라면?
        if type(tree[v]) is str:
            # 왼쪽 자식 노드의 하위노드 cal계산
            left_value = cal(left[v])
            # 오른쪽 자식 노드의 하위노드 cal계산
            right_value = cal(right[v])
            if tree[v] == "+":
                tree[v] = left_value + right_value
            elif tree[v] == "-":
                tree[v] = left_value - right_value
            elif tree[v] == "*":
                tree[v] = left_value * right_value
            else:
                tree[v] = left_value / right_value
        return tree[v]


for tc in range(1, 11):
    # N: 노드의 개수
    N = int(input())
    # tree 배열 정의(0번 인덱스 제외)
    tree = [0] * (N + 1)
    # 자식 노드를 배열로 정의(0번 인덱스 제외)
    left = [0] * (N + 1)
    right = [0] * (N + 1)

    # 트리 값 및 연결 관계 저장
    for n in range(N):
        # 들어오는 인자의 갯수를 모르므로 가변인자로 받아준다.
        idx, a, *b = input().split()
        idx = int(idx)
        operator = ['+', '-', '*', '/']
        # 만약 첫번째로 들어오는 값이 사칙연산이 아니면
        if a not in operator:
            # 정수형으로 바꿔준다
            a = int(a)
        tree[idx] = a
        # 만약 가변인자가 0이 아니면(존재하면)
        if b:
            # 해당 노드의 왼쪽 자식노드에 연결된 노드의 인덱스 값을 저장한다.
            left[idx] = int(b[0])
            # 만약 idx를 제외하고 값만 하나 달랑 들어왔다면
            if len(b) == 2:
                # 해당 오른쪽 자식노드에 그 값을 저장한다.
                right[idx] = int(b[1])

    # 루트 노드 값 구하기
    result = cal(1)
    print("#{} {}".format(tc, int(result)))

