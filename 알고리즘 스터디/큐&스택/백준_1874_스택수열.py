########## hamoon의 풀이 ##########
import sys
sys.stdin = open('input1874.txt')
T = int(input())
s = []      # 스택 초기값 설정
ans = []    # 결과값 한번에 출력용 리스트 초기값 설정
count = 1   # 카운트 초기값 설정
TOF = True # 수열을 만들수 있는지 여부 초기 상태값 설정
# 입력받은 수열의 길이만큼 반복하면서
for i in range(T):
    num = int(input())
    # 입력받은 수가 count보다 크거나 같을 경우
    while count <= num:
        s.append(count) # 스택에 쌓는다.
        ans.append('+')  # '+' 출력
        count += 1  # count횟수를 1 증가시킨다.
        
    # 입력받은 수가 count보다 작을 경우
    # 만약 스택의 마지막 인덱스와 입력받은 값이 같다면
    if s[-1] == num:
        s.pop() # 스택의 마지막 인덱스를 뺀다.
        ans.append('-')  # '-'출력
    # 스택의 마지막 인덱스와 입력받은 값이 다르다면
    else:
        TOF = False    # 상태값을 False로 변경
# 해당 수열을 만들 수 없으므로 'NO' 출력
if TOF == False:
    print('NO')
# 만들 수 있는 경우 결과값 출력
else:
    for i in ans:
        print(i)