import sys
sys.stdin = open('input_5177.txt')


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    #노드 번호 입력받으면서.. heap에 넣어주기
    #heap : 완전 이진트리
    # 1. 새로운 노드를 입력받으면, 마지막 위치에 넣어준다.
    # 2. 새로 추가한 노드의 값이  부모노드의 값보다 작으면 바꿔준다.
    # 3. 2번 작업을 반복해주는데  부모노드의 값보다 크거나, 루트일때 까지 반복
    heap = [0] * (N+1)
    last = 1   #새로운 노드가 추가 되어야 하는 인덱스(노드 번호)
    #값을 받아와서 heap 에 추가하는 함수
    def insert(val):
        global last
        heap[last] = val
        # 2. 새로 추가한 노드의 값이  부모노드의 값보다 작으면 바꿔준다.
        # 3. 2번 작업을 반복해주는데  부모노드의 값보다 크거나, 루트일때 까지 반복
        cur = last
        parent = cur//2
        while parent > 0 and heap[cur] < heap[parent]:
            heap[cur] , heap[parent] = heap[parent] , heap[cur]
            cur = parent
            parent = cur//2
        #요소를 추가했으니, 마지막 요소 위치 변경
        last += 1
    data = list(map(int,input().split()))
    for i in range(len(data)):
        insert(data[i])

    #마지막 노드부터 루트까지 찾으면서 합구하기
    cur = (last - 1)//2
    #합을 구해야 하니까 0으로 초기화
    result  = 0
    while cur > 0:
        result += heap[cur]
        cur = cur//2

    print("#{} {}".format(tc,result))