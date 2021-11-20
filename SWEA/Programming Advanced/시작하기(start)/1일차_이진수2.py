import sys
sys.stdin = open("input이진수2.txt")

T = int(input())
for tc in range(1, T+1):
    #결과 저장 변수
    res = ''
    #계산해야 하는 숫자 받기
    num = float(input())
    #나누기 위한 값
    sub_num = 1
    #최대 12자리까지 출력
    for i in range(12):
        #진행이 될수록 크기는 반절이 된다.
        sub_num /= 2
        #값을 빼보았을때 0보다 크다면 빼고 결과에 '1'추가
        if num - sub_num >= 0:
            res += '1'
            num -= sub_num
            #숫자가 나눠떨어졌다면 반복문 종료
            if num == 0:
                break
        else:
            #계산이 안된다면 0추가
            res += '0'
    #모든 반복문이 끝났는데 값이 남아있다면 overflow 넣기
    if num != 0:
        res = 'overflow'
    print('#{} {}'.format(tc, res))