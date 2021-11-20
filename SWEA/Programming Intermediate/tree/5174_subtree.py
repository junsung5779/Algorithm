import sys
sys.stdin = open('input5174.txt')


def order(child):
    global count
    # 순회를 할때마다 카운트
    count += 1
    # 자식노드를 순회한다.
    for i in tree[child]:
        order(i)


for tc in range(int(input())):
    # 노드의 개수와 출력할 노드
    E, N = map(int, input().split())
    # 노드의 개수만큼 리스트 만들기
    tree = [[] for _ in range(E+2)]
    edges = list(map(int, input().split()))
    for i in range(0, len(edges), 2):
        parent = edges[i]
        child = edges[i+1]
        tree[parent].append(child)



    # count 초깃값 설정
    count = 0
    order(N)
    # 결과값 출력
    print("#{} {}".format(tc+1, count))
