import sys
sys.stdin = open('input5174.txt')

T = int(input())
for tc in range(1,T+1):
    E, N = map(int, input().split())
    data = list(map(int,input().split()))
    #노드번호가 1번부터 시작 0이면 자식 노드가 없는 것
    #left,right : 각 노드의 왼쪽자식과 오른쪽자식의 번호를 저장하는 배열
    #모든 노드의 번호는 1~E+1 , 인덱스로 활용하기 위해서 E+2개 크기의 배열 선언
    left = [0] * (E+2)
    right = [0] * (E+2)
    for i in range(0,len(data),2):
        parent = data[i]
        child = data[i+1]
        if left[parent] == 0:
            left[parent] = data[i+1]
        else:
            right[parent] = data[i+1]
    # N번부터 시작하는 서브트리 순회하면서 노드 개수 세기
    cnt = 0
    # v : 현재 방문하고 있는 노드 번호
    def traversal(v):
        global cnt
        #노드에 방문을 했으니 노드 개수 증가 시키기
        cnt += 1
        #만약에 왼쪽자식이 있으면 왼쪽자식 방문
        if left[v] != 0:
            traversal(left[v])
        #오른쪽 자식이 있으면 오른쪽 자식 방문
        if right[v] != 0:
            traversal(right[v])

    #N번 노드를 루트로 하는 서브트리 순회
    traversal(N)
    #결과 출력
    print("#{} {}".format(tc,cnt))

