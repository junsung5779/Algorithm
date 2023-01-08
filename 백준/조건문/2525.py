arr = list(map(int, input().split()))
t = int(input())

h = (t+arr[1])//60
m = (t+arr[1])%60
arr[0] += h
arr[1] = m
if arr[0] >= 24:
    arr[0] -= 24
print(str(arr[0])+" "+str(arr[1]))
