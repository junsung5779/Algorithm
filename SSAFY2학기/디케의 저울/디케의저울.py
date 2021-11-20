T = int(input())
weights = list(map(int, input().split()))
res = list()
# 트리 형태로 계산
# 저울의 왼쪽에 올리는 경우, 오른쪽에 올리는 경우, 저울에 아무것도 안 올리는 경우