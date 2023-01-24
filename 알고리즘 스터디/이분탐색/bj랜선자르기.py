import sys
input = sys.stdin.readline
K, N = map(int, input().split())   # 4 11
arr = []
# 각 랜선의 길이를 arr에 입력
for i in range(K):
    arr.append(int(input()))

start = 1
answer = 0
end = max(arr)  # OK 최솟값만 만족하면 그보다 긴 랜선들은 다 만족하니깐!
# end = 457
while start <= end: # 최솟값이 최댓값보다 같거나 작은 경우
    mid = (start+end)//2    # mid == 228
    count = 0
    for i in arr:   # 랜선을 돌면서
        count += i//mid # 해당 랜선을 mid 길이로 자르면 나오는 최대 갯수를 count에 저장
        if count >= N:  # 만약 랜선의 최대 갯수를 오버 한 경우에는
            break
    # 만약 count갯수가 만들어야 할 랜선의 갯수보다 크거나 같다면
    if count >= N:
        answer = mid
        start = mid + 1 # 최소 길이를 늘린다.
        # 그러면 쉿
    else:
        end = mid - 1   # 최소 길이를 줄인다.
print(answer)