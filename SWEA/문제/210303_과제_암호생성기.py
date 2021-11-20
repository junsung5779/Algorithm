import sys
sys.stdin = open("input암호생성기.txt")


def mooyaho():
    while True:
        for i in range(1,6):
            # 첫번째 숫자를 i 감소한 뒤, 맨 뒤로 보낸다
            # 다음 첫 번째 수는 2 감소한 뒤 맨 뒤로
            # 그 다음 첫 번째 수는 3을 감소하고 맨 뒤로,
            # 그 다음 수는 4, 그 다음 수는 5를 감소한다.
            a = arr.pop(0)-i
            # 종료조건 : 숫자가 감소할 때 0보다 작아지는 경우 0으로 유지되며 프로그램은 종료됨
            if a <= 0:
                arr.append(0)
                # 이 때 8자리의 숫자 값이 암호가 됨
                return arr
            # 숫자가 감소할 때 0보다 작아지지 않았을 경우 pop으로 반환한 수를 해당 배열의 맨 마지막에 추가
            else:
                arr.append(a)


try:
    while True:
        # 테스트 케이스의 번호를 입력받는다.
        T = int(input())
        if T == None:
            False
        # 8개의 숫자를 입력받는다.
        arr = list(map(int, input().split()))
        # 최대 감소수치는 5이므로 5까지를 1사이클로 정한다.
        mooyaho()
        print(f'#{T}', *arr)
except:
    False