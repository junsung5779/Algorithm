import sys
sys.stdin = open("input4866.txt")

# 테스트 케이스 횟수를 입력받는다
T = int(input())
# 테스트케이스 횟수만큼 반복하면서
for tc in range(1, T+1):
    # 테스트 케이스를 입력받는다.
    str1 = str(input())
    arr = []
    # 빈 리스트에 pop을 할 경우???? 아니면 처음오는 괄호가 닫는 괄호일 경우 에러가 나는데 이 때를 대비해서 try를 써준다.
    try:
        for i in range(len(str1)):
            if str1[0] == "}" or str1[0] == ")":
                res = 0
                break
            # "{" 다음에 ")" 가 오거나 "(" 다음에 "}" 가 오면
            elif (str1[i] == "{" and str1[i+1] == ")") or (str1[i] == "(" and str1[i+1] == "}"):
                # 결과값에 0을 저장하고
                res = 0
                # 반복문 탈출
                break
            # str1을 순회하다가 "{"을 발견하면
            elif str1[i] == "{":
                # arr리스트의 마지막에 1을 넣는다.
                arr.append(1)
            # str1을 순회하다가 "("을 발견하면
            elif str1[i] == "(":
                # arr리스트의 마지막에 2를 넣는다.
                arr.append(2)
            elif str1[i] == "}":
                arr.pop()
            elif str1[i] == ")":
                arr.pop()
        if arr == []:
            res = 1
        else:
            res = 0
    except:
        res = 0
    print("#{} {}".format(tc, res))