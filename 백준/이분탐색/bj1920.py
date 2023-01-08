N = int(input())
N_arr = list(map(int, input().split()))
N_arr.sort()
M = int(input())
M_arr = list(map(int, input().split()))
# N_arr = [4, 1, 5, 2, 3]
# M_arr = [1, 3, 7, 9, 5]

def binarySearch(arr, target, start, end):
    # 종료조건
    if start > end:
        return 0
    mid = (start + end) // 2

    # 원하는 값 찾은 경우 인덱스 반환
    if target == arr[mid]:
        return 1
    # 원하는 값이 중간점의 값보다 작은 경우 왼쪽 부분(절반의 왼쪽 부분) 확인
    elif target < arr[mid]:
        return binarySearch(arr, target, start, mid - 1)
    # 원하는 값이 중간점의 값보다 큰 경우 오른쪽 부분(절반의 오른쪽 부분) 확인
    else:
        return binarySearch(arr, target, mid + 1, end)

for i in M_arr:
    print(binarySearch(N_arr, i, 0, N-1))