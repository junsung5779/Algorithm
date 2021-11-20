# 합이 0인 모든 부분집합 구하기

arr = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]

for i in range(1<<10):
    s = 0
    for j in range(10):
        if i&(1<<j):
            s += arr[j]

    if s==0:
        for j in range(10):
            if i & (1<<j):
                print(arr[j], end=' ')
        print()