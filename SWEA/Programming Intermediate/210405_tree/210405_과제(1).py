import sys
sys.stdin = open("input210405.txt")


def inorder(v):
    # 함수 밖의 res와 연결
    global res
    # 길이가 4인 경우(자식이 둘인 경우)
    if len(node[v]) == 4:
        # 왼쪽 -> 정점 -> 오른쪽 순으로 확인
        # 첫번째 자식노드 탐색
        inorder(int(node[v][2]))
        # 첫번째 자식노드를 탐색하고 난 후 두번째 자식노드를 탐색하기 전 정점의 값을 결과값에 더하기
        res += node[v][1]
        # 두번째 자식노드 탐색
        inorder(int(node[v][3]))
    # 길이가 3인 경우(자식이 하나인 경우)
    elif len(node[v]) == 3:
        # 첫번째 자식노드 탐색
        inorder(int(node[v][2]))
        # 첫번째 자식노드 탐색 후 정점의 값을 결과값에 더하기
        res += node[v][1]
    # 자식이 없는 경우
    else:
        # 해당 노드의 값을 바로 결과값에 더하기
        res += node[v][1]
    return

for tc in range(1, 11):
    n = int(input())
    # 정점번호는 1부터 시작이기 때문에 앞에 0추가해서 index값 통일
    node = [[0]] + [list(map(str, input().split())) for _ in range(n)]
    res = ''
    # 시작정점번호
    inorder(1)
    print('#{} {}'.format(tc, res))