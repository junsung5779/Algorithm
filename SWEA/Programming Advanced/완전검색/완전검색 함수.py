def sequentialSearch(a,n,key):
    i=0
    # a: 탐색할 리스트
    # n: 탐색범위
    # key: 찾을 값
    # i: 인덱스
    # i가 n보다 작고, 리스트a의 i번째 인덱스가 key가 아닐경우
    while i < n and a[i] != key:
        # i값에 1을 더한다.
        i = i+1
    # 만약 i값이 n보다 작을경우
    if i<n:
        # 탐색성공(해당 인덱스값을 반환한다.)
        return i
        # 탐색실패
    else:
        return -1

# T=[1,2,3,4]
# print(sequentialSearch(T, len(T), 2))

# 서로다른 3가지 숫자를 순서대로 뽑는 모든 경우의 수(순열)
#######################################################
arr=[1,2,3,4,5]
for i in range(0, len(arr)-3+1):
    for j in range(i+1, len(arr)-2+1):
        for k in range(j+1, len(arr)-1+1):
            print([i,j,k])

# 재귀를 이용한 순열
#######################################################
def f(i,j,n,r): # i, c[i], j 선택구간의 시작
    if i==r:
        print(c)
    else:
        for k in range(j, n-r+i+1):
            c[i]=A[k]
            f(i+1,k+1,n,r)

n=5
r=3
A=[1,2,3,4,5]
c=[0]*r

f(0,0,n,r)