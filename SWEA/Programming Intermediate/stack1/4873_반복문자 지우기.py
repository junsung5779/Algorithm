
def check(data):
    stack = []
    # 데이터의 인덱스를 반복하면서
    for i in range(len(data)):
        # 만약 i번째 인덱스의 값과 stack의 마지막값이 같지 않다면
        if not stack or data[i] != stack[-1]:
            # stack에 해당 인덱스의 값을 추가
            stack.append(data[i])
        else:
            stack.pop()
    return stack

for tc in range(1,int(input())+1):
    data = input()
    res = check(data)
    print('#{} {}'.format(tc, len(res)))