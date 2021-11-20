
def quick_sort(A,l,r):
    if l < r:
        # 피봇구하기
        s = lomuto_partition(A,l,r)
        # 피봇의 왼쪽 구간에 대해 퀵정렬
        quick_sort(A,l,s-1)
        # 피봇의 오른쪽 구간에 대해 퀵정렬
        quick_sort(A,s+1,r)

# 피봇의 자리를 정하는 작업
def Hoare_partition(A,l,r):
    # 리스트의 제일 왼쪽을 피봇값으로 설정
    p = A[l]
    # 양쪽 끝부터 작업을 시작
    i,j=l,r
    # i가 j보다 같거나 작을때
    while i<=j:
        # i가 j보다 같거나 작으면서 피봇이 리스트의 i번째 값보다 같거나 크면 오른쪽으로 한칸 이동
        while i<=j and A[i] <= p:
            i += 1
        # i가 j보다 같거나 작으면서 피봇이 리스트의 j번째 값보다 같거나 작으면 왼쪽으로 한칸 이동
        while i<=j and A[j] >= p:
            j -= 1
        if i < j:
            # 리스트의 i와 j번째 인덱스에 해당하는 값을 서로 바꿈
            A[i],A[j] = A[j],A[i]
    # 반복문이 끝나고 나면
    # 리스트의 l번째 값과 j번째 값을 서로 바꿈
    A[l],A[j] = A[j],A[l]
    # 인덱스 j를 리턴
    return j

def lomuto_partition(A,start,end):
    # 피봇값을 리스트의 제일 마지막 인덱스 값으로 정하는 경우
    pivot = A[end]
    i = start-1
    # s부터 e-1(e번째 값이 피봇이므로)까지 순회하면서
    for j in range(start,end):
        # 리스트의 j번째 값이 pivot보다 같거나 작다면
        if A[j] <= pivot:
            # i의 인덱스를 1 올리고
            i += 1
            # 리스트의 i번째 인덱스의 값과 j번째 인덱스의 값을 서로 바꾼다
            A[i],A[j] = A[j],A[i]
    # 반복문이 끝나고 나면 작은 값 리스트의 제일 마지막 인덱스+1에 해당하는 값(=큰 값 리스트의 제일 첫번째 값)과
    # 큰 값 리스트의 제일 마지막 인덱스의 값을 서로 바꾼다.
    A[i+1],A[end] = A[end],A[i+1]
    # 인덱스 i+1(큰 값 리스트의 제일 첫번째 인덱스)을 반환한다
    return i+1

arr = [2,2,1,1,3]
quick_sort(arr,0,len(arr)-1)
print(arr)