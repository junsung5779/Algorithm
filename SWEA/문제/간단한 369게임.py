
num = int(input())
# 출력시킬 내용의 초기값을 지정한다

# 1부터 T까지 숫자를 돌리고 i로 나타낸다
    # T의 자릿수를 구한다.
    # 0부터 i의 길이까지 반복문을 돌리고 j로 나타낸다
        # 10의 j승을 i로 나눈 나머지를 k로 나타낸다
        # k가 만약 3또는 6또는 9라면 출력시킬 내용에 '-'를 추가한다.

cnt = 0
while num > 0:
    d = num %10
    num //= 10
    if d == 3 or d == 6 or d == 9:
        cnt += 1

    # 3/6/9 가 없으면 숫자를 출력
    if cnt == 0:
        print(num, end=" ")
    else:
        print("-"*cnt, end=" ")
    # 박수를 친다. -