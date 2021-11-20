import sys
sys.stdin = open("input4874.txt")

T = int(input())
# 테스트케이스 횟수를 반복하면서
for tc in range(1,T+1):
    # 스택을 쌓을 빈 리스트 만들기
    stack = list()
    # 문자열리스트에 입력값을 문자열로 받아 요소로 저장
    ex_str = list(map(str, input().split()))
    # 스택의 길이 저장
    N = len(ex_str)
    # 문자열리스트의 길이만큼 반복하면서(.이 나오면 끝내야 하므로)
    for n in range(N-1):
        # 피연산자를 만나면 스택에 push함
        if ex_str[n].isdigit():
            stack.append(ex_str[n])
        else:
            num1 = int(stack.pop())
            if len(stack) == 0:
                break
            num2 = int(stack.pop())
            if ex_str[n] == "*":
                result = num2*num1
            elif ex_str[n] == "/":
                result = num2//num1
            elif ex_str[n] == "+":
                result = num2+num1
            elif ex_str[n] == "-":
                result = num2-num1
            stack.append(str(result))

    # 다 하고 난 후 스택의 길이가 1이면(결과값이 하나이므로 계산이 성공 한 경우)
    if len(stack) == 1:
        print("#{} {}".format(tc, stack[0]))
    # 계산이 성공적이지 못한 경우
    else:
        print("#{} error".format(tc))
