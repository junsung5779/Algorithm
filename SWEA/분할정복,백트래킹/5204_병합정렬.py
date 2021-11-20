
# 병합정렬
def merge_sort(data):
    # 입력받은 리스트의 길이가 1이면
    if len(data) == 1:
        # 해당 리스트 반환
        return data
    # 이분할의 기준이 되는 가운데인덱스를 설정
    middle = len(data)//2
    # 입력받은 data를 0번 인덱스부터 middle-1번 인덱스까지를 슬라이싱한 후 left에 저장
    left = merge_sort(data[:middle])
    # 입력받은 data를 middle번 인덱스부터 마지막 인덱스까지를 슬라이싱한 후 right에 저장
    right = merge_sort(data[middle:])
    # left,right를 병합한 것을 반환
    return merge(left,right)

# 병합
def merge(left,right):
    global cnt
    res = list()
    i,j=0,0
    # 만약 left의 마지막 값이 right의 마지막 값보다 크다면
    if left[-1] > right[-1]:
        # 카운트 1회
        cnt += 1

    # left의 길이가 i보다 크거나, right의 길이가 j보다 크면
    while i < len(left) or j < len(right):
        # left의 길이가 i보다 크면서 right의 길이가 j보다 클때
        if i < len(left) and j < len(right):
            # left의 i번째 요소가 right의 j번째 요소보다 같거나 작다면
            if left[i] <= right[j]:
                # res에 left의 i번째 요소 추가
                res.append(left[i])
                i += 1
            # left의 i번째요소가 right의 j번째 요소보다 크다면
            else:
                # res에 right의 j번째 요소 추가
                res.append(right[j])
                j += 1
        # left 에만 요소가 남아있고 right에는 요소가 없을 때
        elif i < len(left):
            # res에 left의 i번째 요소 추가
            res.append(left[i])
            i += 1
        # right에만 요소가 남아있고 left에는 요소가 없을 때
        elif j < len(right):
            res.append(right[j])
            j += 1
    # 조건문이 끝난다음 결과 반환
    return res

T = int(input())
for tc in range(1,T+1):
    cnt = 0
    N = int(input())
    arr = list(map(int, input().split()))
    res = merge_sort(arr)
    print("#{} {} {}".format(tc, res[N//2],cnt))
