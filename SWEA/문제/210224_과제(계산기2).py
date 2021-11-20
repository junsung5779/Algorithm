# 중위표기법 : 3 + 4 + 5 * 6 + 7 ==> 후위표기법: 34 + 56 * + 7 +
# 숫자가 오면 출력할 리스트에 담는다.
# 숫자가 아닌 연산자는 stack 리스트에 쌓는다.
# stack리스트의 맨 위 연산자의 가중치가 새로 추가되는 연산자의 가중치 보다 높거나 같다면 전부 출력할 리스트로 옮긴다.


import sys
sys.stdin = open("input210224.txt")
stack = list()

# 연산자의 가중치를 담은 딕셔너리를 작성한다.
instack = {"+": 1, "*": 2}

# 후위표기법 함수 작성
def whowe(arr):
    # 스택에 쌓기
    # 입력받은 식의 길이만큼 순회하면서
    for i in range(len(arr)):
        # 임시로 arr의 i인덱스에 있는 값을 lst로 표기한다.
        lst = arr[i]
        # lst가 "+"나 "*" 일 때
        if lst in ("+", "*"):
            # stack리스트에 아무것도 없거나, 해당 연산자의 가중치가 stack리스트의 최상단에 있는 연산자의 가중치보다 클 때
            if not stack or instack[lst] > instack[stack[-1]]:
                # stack리스트의 최상단에 해당 연산자를 추가한다.
                stack.append(lst)
            else:
                # 우선순위가 낮으면, 나보다 낮거나 같은애가 top에 있을때 까지 pop 하고 push
                while stack and instack[lst] <= instack[stack[-1]]:
                    print(stack.pop(), end=" ")
                # stack리스트의 최상단에 해당 연산자를 추가한다.
                stack.append(lst)
        else:  # 숫자이면,
            # 숫자는 출력하면 됨
            print(lst, end=" ")

    # 쌓인 스택을 풀면서 계산하기

#테스트케이스 횟수 10회를 순회하면서
for tc in range(1, 11):
    # 테스트케이스의 길이를 입력받는다.
    N = int(input())
    # 테스트케이스를 입력받는다.
    arr = input()
    whowe(arr)