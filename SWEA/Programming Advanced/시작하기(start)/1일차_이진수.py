import sys
sys.stdin = open("input이진수.txt")

def decimal_to_binary(num):
    global sum
    sum=''
    for i in num:
        n = int(i)
        # 이진수를 저장할 배열
        binary = [0]*4
        idx = 3
        while n > 0:
            binary[idx] = n%2
            n //= 2
            idx -= 1
        for j in binary:
            sum += str(j)
    return sum


T = int(input())
for tc in range(1,T+1):
    sum = ''
    N, hexadecimal = map(str, input().split())
    arr=list()
    for i in hexadecimal:
        if i == 'A':
            arr.append('10')
        elif i == 'B':
            arr.append('11')
        elif i == 'C':
            arr.append('12')
        elif i == 'D':
            arr.append('13')
        elif i == 'E':
            arr.append('14')
        elif i == 'F':
            arr.append('15')
        else:
            arr.append(i)
    decimal_to_binary(arr)

    print('#{} {}'.format(tc,sum))