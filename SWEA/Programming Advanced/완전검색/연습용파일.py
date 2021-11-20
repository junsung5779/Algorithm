# 1부터 N까지 누적합이 출력 되도록 func 작성: 글로벌 변수 사용 X
def func(n):
    if n == 1:
        return 1
    return func(n-1) + n
N=5
result = func(N)
print(result)

# 재귀로 순열구하기
# 재귀 한번 호출 할 때 마다 각 idx별 숫자가 어디에
# 들어갈지 결정
# 어떤 요소의 위치를 결정할지 idx가 필요
# 어떤 위치가 사용되었는지 정보가 필요: used
# 순열을 저장하는 배열 : perm
# 요소의 개수 : N

arr = [1,2,3]
used =[0,0,0]
N = 3
newArr = [0]*N
def perm_func(perm,used,idx,N):
    if idx == N:
        print(perm)
        return

    for i in range(N):
        # used[1] == 0
        if used[i] == 0:

            perm[i] = arr[idx]
            # newArr[2] = arr[2]
            # newArr:[1,2,3]
            used[i] = 1
            # used[2] = 1
            # used:[0,0,1]
            perm_func(perm,used,idx+1,N)
            # prem_func([1,2,3],[0,0,1],3,3)
            used[i] = 0
            a=0
            # used[2] = 0
            # used:[0,0,0]

perm_func(newArr,used,0,N)
