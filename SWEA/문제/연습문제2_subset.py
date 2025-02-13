arr= [-1,1,4, 7, -5,2,6,-10,4,3]
#부분집합의 합이 0이되는 모든 부분집합 출력하기
N = 10

# 모든 부분집합을 구한다.
#모든 부분집합의 모양을 숫자로 나타내서 각 숫자의 이진수 를 확인
#1<<N : 원소 N개인 집합의 모든 부분집합의 개수 (2^N)
# 0000000000 ~ 1111111111까지 이진법으로 1씩 증가시키면서 반복문 돌린다.
for i in range(1<<N):
    #i 는 0~ N-1
    #i의 이진 수 모양이 부분집합의 모양이다.
    # i의 이진수의 각 비트를 확인하기
    # 비트 몇개 확인하면 되요?? N 개
    #부분집합에 포함되는 모든 요소의 합이 0인지 아닌지 판단!!
    sum_v = 0
    sub_set = list()
    # 원소의 개수(N=10)를 처음부터 끝가지 반복을 하면서
    for j in range(N):
        #파이썬에서는 0이면 false , 나머지 true
        if i & (1<<j):  # 참이면 해당비트에 매칭되는 요소가 부분집합에 포함
            sum_v += arr[j]
            sub_set.append(arr[j])
    if sum_v == 0:
        print("모든 합이 0입니다.", sub_set)

