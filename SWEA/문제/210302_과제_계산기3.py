import sys
sys.stdin = open("input계산기3.txt")

# 연산자의 종류: +,*,(,)
# 피연산자는 출력(후위표기법에 더하기)
# +,*가 나오면 곱하기가 우선순위가 높음
# 여는 괄호를 만나면 stack에 넣고,
# 닫는 괄호를 만나면 그 때 stack에서 빼면 됨

# 중위표현식을 후위표현식으로 바꾸기
# 후위표현식 계산하기, 계산결과를 반환
def solve(exp):
    stack = list()  # 후위표기식을 만들기 위한 스택
    # 1. 후위표기식으로 바꾸기
    postfix = ''   # 후위표기식을 저장할 변수
    # 1. 표현식을 하나씩 읽음
    for i in range(L):
    # 2. 피연산자(숫자)가 나오면, 후위표기식에 더하기(문자열 1~9를 아스키코드로 비교하기 때문에 가능함)
        if "0" <= exp[i] <= "9":
            postfix += exp[i]
    # 3. 연산자가 나오면 우선순위에 의거해서 stack에 넣거나
        elif exp[i] == "(":
            stack.append(exp[i])
        elif exp[i] == ")":
            # 여는 괄호가 나올때 까지 빼면서, 후위 표기식에 추가
            while stack[-1] != "(":
                postfix += stack.pop()
            stack.pop() # 여는 괄호는 버림
        else: # exp[i] 가 +, * 인 경우
            if not stack:
                stack.append(exp[i])
                continue
            # 곱하기 이면서 stack[-1]이 곱하기가 아니면 push
            # 더하기 이면서, stack[-1]이 괄호이면, push
            # 나머지는 * +가 아닐때 까지 pop하고 push
            if exp[i] == "*":
                stack.append(exp[i])
            elif exp[i] == '+' and stack[-1] == "(":  # 얘보다 우선순위 낮은거는 '('에 없으니까...
                stack.append(exp[i])
            else:
                #   stack에서 빼기
                while (stack and (stack[-1] == "*" or stack[-1] == "+")):
                    postfix += stack.pop()
                stack.append(exp[i])
    while stack:
        postfix += stack.pop()
    cstack = list()
    # 2.후위표기식 계산하기
    # 피연산가 나오면 stack 넣고
    # 연산자가 나오면 stack에서 피연산자 2개 꺼내서 계산
    for i in range(len(postfix)):
        if postfix[i] == "*":
            v1 = cstack.pop()
            v2 = cstack.pop()
            cstack.append(v1 * v2)
        elif postfix[i] == "+":
            v1 = cstack.pop()
            v2 = cstack.pop()
            cstack.append(v1 + v2)
        else:
            cstack.append(int(postfix[i]))
    return cstack.pop()


for tc in range(1, 11):
    L = int(input())
    exp = input()
    result = solve(exp)
    print("#{} {}".format(tc,result))