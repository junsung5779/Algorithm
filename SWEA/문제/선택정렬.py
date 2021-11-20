arr = [5,2,6,1,9,3,7,8,4]
N = len(arr)
arred = [0]*N
def selection_sort(N, arr):
    # 최솟값을 초기화한다.
    min_arr = 99999
    # 리스트의 길이만큼 반복하면서
    for i in range(N):
        # 최솟값을 정렬하고 나서는 그 최솟값을 비교하면 안되므로 시작범위를 한칸씩 증가한다.
        for j in range(N):
            # 인덱스 에러가 나지 않게 하기 위해 조건문을 달아준다.
            if i+j < N-1:
                # 해당 인덱스에 있는 값이 min_arr보다 작으면
                if arr[i+j] < min_arr:
                    # 최솟값을 해당 인덱스에 있는 값으로 갱신한다
                    min_arr = arr[i+j]
        # 범위 내에서 최솟값을 찾아낸 후 그 최솟값을 오름차순으로 정렬한다.
        arred[i] = min_arr
    # 정렬된 리스트를 반환한다
    return arred
print(arred)