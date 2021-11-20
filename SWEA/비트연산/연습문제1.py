import sys
sys.stdin = open("input연습문제1.txt")

# 7개 비트씩 끊어서 10진 숫자로 만들기
bits = list(map(int,input()))
# bits의 전체 길이만큼 반복
for i in range(0,len(bits),7):
    # 시작점부터...7개 반복
    num = 0 # 7개 비트가 나타내는 10진수를 저장할 변수
    cnt = 6
    for j in range(i,i+7):
        if bits[j] == 1:
            num += 2**cnt
        # 다음 비트를 검사할 때 2의 승수가 하나 무조건 낮아져야함
        cnt -= 1
    print(num,end=", ")