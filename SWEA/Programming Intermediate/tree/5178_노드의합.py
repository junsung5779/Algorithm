import sys
sys.stdin = open('input_5178.txt')

T = int(input())
for tc in range(1,T+1):
    N,M,L = map(int,input().split())
    #N = 노드의 개수, M = 리프노드의 개수, L = 출력할 노드번호
    tree = [0] * (N+1)
    #완전이진 트리이고, 1~N번이 빠짐없이 노드번호가 매겨지기 때문에
    #배열로 트리를 만들면 노드번호가 배열의 인덱스가 됩니다.
    for i in range(M):
        #num :노드번호, val : 노드 값
        num, val = map(int,input().split())
        tree[num] = val

    # v : 현재 노드의 번호
    def traversal(v):
        if v > N:
            return 0
        # 자식노드들부터 먼저 순회해서.... 값받아오고,
        # 자식노드들의 합을 내 위치에 저장
        left = traversal(v*2)
        right = traversal(v*2+1)
        tree[v] += left+right
        return tree[v]

    traversal(1)
    print("#{} {}".format(tc,tree[L]))