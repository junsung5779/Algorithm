arr = [7,5,4,6,3,2,8,1,9]

def SelectionSort(lst):
    n=0
    # 0부터 리스트 길이까지 순회하면서
    while n < len(arr):
        # 임시로 옮겨둘 곳을 만들어주고
        tmp=0
        # 정렬 시도
        if arr[n] > arr[n+1]:
            tmp = arr[n]
            arr[n] = arr[n+1]
            arr[n+1] = tmp
        n+=1
