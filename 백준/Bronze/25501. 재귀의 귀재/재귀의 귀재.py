def recursion(s, l, r):
    # s: 문자열
    # l: 왼쪽 인덱스
    # r: l과 대칭하는 인덱스
    global cnt # 함수 내에서 전역 변수로 cnt를 활용하기 위해 global로 명시해준다.
    cnt += 1
    
    if l >= r:
        return 1    # 만약 왼쪽 인덱스가 오른쪽 인덱스보다 같거나 크다면 펠린드롬임
    elif s[l] != s[r]:    # 만약 왼쪽 인덱스의 값과 오른쪽 인덱스의 값과 다르다면 펠린드롬이 아님
        return 0
    else:        # 둘 다 아니라면
        return recursion(s, l+1, r-1)    # 왼쪽 인덱스는 오른쪽으로, 오른쪽 인덱스는 왼쪽으로 한칸 이동하여 재귀함수 발동

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

for _ in range(int(input())):
    cnt = 0
    print(isPalindrome(input()), cnt)    #rstrip([chars]): 인자로 전달된 문자를 String의 오른쪽에서 제거