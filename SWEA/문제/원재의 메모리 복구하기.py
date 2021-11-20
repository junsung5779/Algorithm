def convert(value, start):
    for i in range(start, len(arr)):
        arr1[i] = value

T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input()))
    arr1 = [0]*len(arr)
    cnt = 0

    if arr[0] == 1:
        cnt += 1
        arr1 = [1]*len(arr)

    for i in range(len(arr)-1):
        # 앞뒤가 같을 경우 스킵
        if arr[i] == arr[i+1] : continue

        # 앞뒤가 다를 경우 다른 비트로 채우기
        if arr[i] == 1:
            # i+1부터 0으로 채우기
            convert(0, i+1)
        else:
            # i+1부터 1으로 채우기
            convert(1, i+1)
        cnt +=1
    print("#{} {}".format(tc, cnt))