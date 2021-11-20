# 오름차순으로 정렬된 리스트 기준으로 이진탐색
# dir : 1이면 왼쪽, 2이면 오른쪽, 3이면 시작
def binary_search(data,low,high,key,dir):
    global cnt
    # 만약 low인덱스가 high인덱스 보다 크면(탐색을 다 했음에도 원하는 값을 찾지 못했으면)
    if low > high:
        # -1 반환
        return -1
    # low인덱스가 high인덱스 보다 같거나 작으면(탐색이 아직 안끝난경우)
    else:
        # 가운데 인덱스(mid)를 저장
        mid = (low+high)//2
        # 만약 찾고자 하는 값(key)이 리스트의 가운데 인덱스값과 같다면
        if key == data[mid]:
            # 카운트 값을 1회 올린다.
            cnt += 1
            # 해당 인덱스를 반환
            return mid
        # 찾고자 하는 값(key)이 리스트의 가운데 인덱스값보다 작다면
        elif key < data[mid] and dir != 1:
            # low ~ mid-1 인덱스까지 재탐색
            return binary_search(data,low,mid-1,key,1)
        # 찾고자 하는 값(key)이 리스트의 가운데 인덱스값보다 크다면
        elif key > data[mid] and dir != 2:
            return binary_search(data,mid+1,high,key,2)

T = int(input())
for tc in range(1,T+1):
    # 카운트값 초기화
    cnt = 0
    # N: arr의 길이
    # M: num_list의 길이
    N,M = map(int, input().split())
    # 탐색범위 리스트
    arr = list(map(int, input().split()))
    arr = sorted(arr)
    # 탐색할 키값들의 집합 리스트
    num_list = list(map(int, input().split()))
    # key값을 모아둔 리스트를 순회하면서
    for i in num_list:
        # 키값i를 탐색하고 해당 키값의 인덱스를 반환
        binary_search(arr, 0, len(arr)-1, i,3)
    print('#{} {}'.format(tc,cnt))
# arr = [1,2,3,4,5,6,7,8,9]
# binary_search(arr,0,len(arr)-1,7)
