def find_set(x):
    # 부모값과 자식값이 같지 않다면
    while p[x] != x:
        # 자식값을 x에 저장하고
        # 다시 조건문으로 돌아간다
        x = p[x]
    # 부모값과 자식값이 같다면 조건문을 빠져나오고
    # 해당 부모값을 return한다.
    return x


for tc in range(1, int(input())+1):
    N,M = map(int, input().split())
    arr = list(map(int, input().split()))
    # 대표원소 초기화
    # n번인덱스에 들어있는 값을 그대로 쓰기위해 0번 인덱스를 하나 만듦
    p = [0]*(N+1)
    # 반복문을 순회하면서
    for i in range(1,N+1):
        # p의 i번째 인덱스값을 i로 저장
        p[i] = i

    for i in range(M):
        # a: 부모값
        # b: 자식값
        a,b = arr[i*2], arr[i*2+1]
        # 자식값의 인덱스에 해당하는 값을 부모값으로 저장
        p[find_set(b)] = find_set(a)

    cnt = 0
    # 부모원소 하나에 여러개의 자식원소들이 딸려있는 형태이므로
    # 부모원소만 체크하면 된다
    # p리스트를 돌면서
    for i in range(1,N+1):
        # 만약 부모원소를 만난다면
        if p[i] == i:
            # 1회 카운트 해준다.
            cnt += 1
    print('#{} {}'.format(tc,cnt))