def sumK(nums, k):
    # ex) nums == [1, 2, 3]
    # ex) k == 2
    nums_length = len(nums)
    sum_arr = list()

    for i in range(1<<nums_length): # ex) nums_length == 3 인 경우 -> 1<<3 == 2^3 == 8 == 1000(이진수)
        sum = 0 # 부분집합의 합을 구할 때 마다 sum_arr에 추가해줘야 하니 여기서 초기화
        for j in range(nums_length):
            if i&(1<<j):    # i == (0~7) # 1<<j == (2^j(min) ~ 2^j(max))
                # print(nums[j], end=',')
                sum += nums[j]
        sum_arr.append(sum) # 부분집합의 각 원소의 합을 sum_arr에 추가
        # print() # 줄바꿈
    # print(sum_arr[k]) # 0번째 인덱스 0을 제외한 k번째 작은 값
    # 1. nums를 가지고 sub-array를 만들어야 한다. -> 어떻게 만들지? -> 비트연산자를 가지고 어떻게 하면 될 것 같은데.....
    # 2. 생겨난 sub-array의 합을 나타낸 후 배열로 집어넣는다.
    # 3. 정렬 해서 4번째 인덱스의 값을 출력한다.
    sum_arr.sort()
    return sum_arr[k]   # 0번째 인덱스 0을 제외한 k번째 작은 값
nums = list(map(int, input().split()))
k = int(input())

# 제약사항
# n == nums.length
# 1 <= n <= 5 *10^4
# 1 <= nums[i] <= 10^5
# 1 <= k <= n*(n+1) / 2
print(sumK(nums,k))
# print(nums, k)