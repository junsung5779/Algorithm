# 포화/완전 이진트리의 경우

# 전위 순회
# 1) 현재 노드 n을 방문하여 처리한다.: V
# 2) 현재 노드 n의 왼쪽 서브 트리를 순회한다. : L
# 3) 현재 노드 n의 오른쪽 서브 트리를 순회한다.: R

# 전위 순회 알고리즘
preorder_traverse(TREE T)
    IF T is not null
        visit(T)
        preorder_traverse(T.left)
        preorder_traverse(T.right)


# 중위 순회
# 1) 현재 노드 n의 왼쪽 서브트리를 순회한다. : L
# 2) 현재 노드 n을 방문하여 처리한다. : V
# 3) 현재 노드 n의 오른쪽 서브트리를 순회한다. : R
preorder_traverse(TREE T)
    IF T is not null
        preorder_traverse(T.left)
        visit(T)
        preorder_traverse(T.right)

# 후위 순회
# 1) 현재 노드 n의 왼쪽 서브트리를 순회한다. : L
# 2) 현재 노드 n의 오른쪽 서브트리를 순회한다. : R
# 3) 현재 노드 n을 방문하여 처리한다. : V
preorder_traverse(TREE T)
    IF T is not null
        preorder_traverse(T.left)
        preorder_traverse(T.right)
        visit(T)
