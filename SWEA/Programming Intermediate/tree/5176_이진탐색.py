import sys
sys.stdin = open('input5176.txt')

# 함수 작성
def maketree(v):
    global count
    # 만약 배열의 크기보다 같거나 작다면
    if v <= N:
        #규칙에 의해 왼쪽 자식노드 부터 탐색
        maketree(v*2)
        # 트리의 마지막 자식노드에 도착하면 해당 인덱스에 count값을 저장
        tree[v] = count
        # count값을 저장하고 나면 count값을 1 증가시킴
        count += 1
        # 오른쪽 자식노드 탐색
        maketree(v*2+1)


for tc in range(int(input())):
    N = int(input())
    count = 1
    tree = [0 for _ in range(N+1)]
    maketree(1)
    print("#{} {} {}".format(tc+1, tree[1], tree[N//2]))