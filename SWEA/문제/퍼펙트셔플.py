
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(str, input().split()))
    ans = [0]*N
    
    # 두 부분으로 나눌때 홀수일 때 앞쪽이 하나 더 많게
    if N%2 == 0:
        mid = N//2
    else:
        mid = N//2+1
    
    #i:앞쪽, j:뒷쪽, k:새로만들 정답의 인덱스
    i,j,k = 0, mid, 0
    while k < N:
        if k%2 == 0:
            ans[k] = arr[i]
            i += 1
        else:
            ans[k] = arr[j]
            j += 1
        k += 1
    print("#{} {}".format(tc, " ".join(ans)))