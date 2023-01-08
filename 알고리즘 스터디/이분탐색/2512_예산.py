# import sys
# input = sys.stdin.readline
# N = int(input())
# arr = list(map(int, input().split()))
# budget = int(input())
#
# # 1. 일단, 요청하는 예산의 합 <= 배정된 예산 이라면, 요청하는 예산 중 최댓값을 출력한다.
# if sum(arr) <= budget:
#     print(max(arr))
# # 2. 아닐 경우 요청하는 예산이 budget//N 보다 작은 것들을 bugdet에서 차감한 후
# # 2-1. (남은 budget // 요청하는 예산이 (budget//N)보다 큰 것의 개수) 를 출력
# else:
#     for i in arr:
#         if i < (budget//N):
#             budget = budget - i
#             N = N - 1
#     print(budget//N)

import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
budget = int(input())

# 1. 일단, 요청하는 예산의 합 <= 배정된 예산 이라면, 요청하는 예산 중 최댓값을 출력한다.
if sum(arr) <= budget:
    print(max(arr))
# 2. 아닐 경우 요청하는 예산이 budget//N 보다 작은 것들을 bugdet에서 차감한 후
# 2-1. (남은 budget // 요청하는 예산이 (budget//N)보다 큰 것의 개수) 를 출력
else:
    for i in arr:
        if i < (budget//N):
            budget = budget - i
            N = N - 1
    print(budget//N)