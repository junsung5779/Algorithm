data = list(map(int,"1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13".split()))
H = 4
tree = [-1]*(pow(2,H+1))
# 루트는 1
tree[1] = 1
for i in range(0,len(data), 2):
    # data[i]: 부모번호
    # data[i+1]: 자식번호
    parent = data[i]
    child = data[i+1]
    # 자식의 인덱스를 찾아야 함
    # 자식의 인덱스 : 부모 노드의 인덱스 *2 또는 부모 노드의 인덱스 *2 +1
    # 부모노드 인덱스 찾기: index()함수 이용
    p_idx = tree.index(parent)
    # 만약에 왼쪽 자식이 없다면, 왼쪽자식에 추가
    # 왼쪽자식이 있다면 오른쪽 자식에 추가
    if tree[p_idx] == -1:   # 왼쪽자식이 없음, 왼쪽자식으로 추가
        tree[p_idx*2] = child
    else:   # 왼쪽 자식이 있으면 오른쪽 자식으로 추가
        tree[p_idx*2+1] = child
print(tree)