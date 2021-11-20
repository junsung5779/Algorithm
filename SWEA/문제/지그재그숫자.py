
T = int(input())

for i in range(1, T+1):
    N = int(input())
    sum = 0
    for j in range(1, N+1):
        if j % 2 == 1:
            sum += j
        else:
            sum -= j
    print("#{} {}".format(i,sum))