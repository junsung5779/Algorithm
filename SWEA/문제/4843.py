#4843_특별한정렬
def bubble_sort(arr):
    for i in range(N-1):
        for j in range(N-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j + 1] = arr[j+1],arr[j]


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    #정렬하고, 역순정렬 준비(역순 슬라이싱)
    bubble_sort(arr)    # 오름차순 정렬
    arr2 = arr[::-1]    # 오름차순 정렬을 역순으로 배열 복사(내림차순)
    result = list()
    for i in range(5):  # 문제에서 10개만 출력하라고 했으니 우리는 2개씩 갖다붙이기때문에 5번만 반복
        result.append(arr2[i])  # 큰 수
        result.append(arr[i])   # 작은수
    print("#{}".format(tc),end=" ")
    for i in range(len(result)):
        print(result[i],end=" ")
    print()