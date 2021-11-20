import sys
sys.stdin = open('input5176.txt')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    tree = [0]*(N+1)
    #중위 순회하면서, 번호를 차례대로 넣으면
    #N개짜리 이진검색트리와 모양이 같다.
    num = 1 #tree에 노드 번호를 넣어주기 위한 변수
    def inorder(v):
        global num
        if v <= N:
           inorder(v*2)
           tree[v] = num
           num += 1
           inorder(v*2+1)
    #이진탐색트리 모양을 하는 트리 만들기
    inorder(1)
    print("#{} {} {}".format(tc,tree[1],tree[N//2]))