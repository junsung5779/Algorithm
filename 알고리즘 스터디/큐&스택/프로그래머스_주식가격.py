########## 하문 풀이 ##########

# def solution(prices):
#     answer = []
#     cnt = 0
#     # prices의 배열의 길이가 주식 장이 열린 시간이다.
#     for i in range(len(prices)):    # 나타내야 할 prices배열의 길이만큼 반복하면서
#         # 다음 시간대에 가격이 떨어지지 않은 경우
#         # prices의[i+1]번째 인덱스의 값보다 가격이 낮거나 같다면 다음 시간대에 가격이 떨어지지 않았으므로
#         if prices[i] <= prices[i+1]:
#             # (전체 주식시간) - (i+1)번째 주식시간(배열 스타트가 0부터니깐)을 answer의 i번째 인덱스에 담는다.
#             answer[i] = len(prices) - (i+1)
#         # 다음 시간대에 가격이 떨어진 경우
#         # prices의[i+1]번째 인덱스의 값보다 가격이 높다면 다음 시간대에 가격이 떨어진 것이므로
#         else:
#             # 1을 answer의 i번째 인덱스에 담는다.
#             answer[i] = 1
#     return answer

########## 풀이 ##########
# prices = [1, 2, 3, 2, 3, 1] return [5, 4, 1, 2, 1, 0]
def solution(prices):
    length = len(prices)

    # answer을 max값으로 초기화
    answer = [i for i in range(length - 1, -1, -1)]

    # 주식 가격이 떨어질 경우 찾기
    stack = [0]
    # prices를 순회한다.
    for i in range(1, length):
        # stack이 있고, 현재 순회하고 있는 값이 stack의 마지막인덱스에 해당하는 prices의 값보다 작을 경우 아래 과정을 반복
        while stack and prices[stack[-1]] > prices[i]:
            j = stack.pop() # stack에서 값을 pop한다.
            answer[j] = i - j   # 위에서 pop한 인덱스의 answer값을 (작아질 때의 인덱스 - pop한 인덱스)로 변경한다.
        stack.append(i) # stack에 순회하는 인덱스를 append한다.
    return answer