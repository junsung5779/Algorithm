import sys
sys.stdin = open('input4344.txt')

# 테스트케이스 반복횟수를 입력받는다.
T = int(input())
# 테스트케이스를 반복하면서
for tc in range(T):
    # 평균을 구하기 위해 총합 초기값을 설정한다.
    sum=0
    # 비율을 구하기 위해 카운트 초기값을 설정한다.
    cnt=0
    # 주어지는 값을 공백을 기준으로 리스트에 저장한다
    arr=list(map(int, input().split()))
    # 리스트의 첫 번째 요소는 점수의 개수이기 때문에 첫번째를 제외하고 1부터 반복문을 시작한다
    for i in range(1, len(arr)):
        # 첫번째 인덱스에 저장된 값부터 마지막 인덱스에 저장된 값까지 sum에 더한다
        sum += arr[i]
    # 평균을 낸다
    avg = sum/(len(arr)-1)
    # 평균을 구했으므로 비율을 구하기 위해 다시 반복문을 돌린다.
    for j in range(1, len(arr)):
        # 만약 해당 점수가 평균보다 높으면
        if arr[j] > avg:
            # 카운트를 1회 올린다.
            cnt+=1
    # 결과를 작성한다
    ans = cnt/(len(arr)-1)*100
    # 소수점 셋째 자리까지 나타내기 위해 %0.3를 사용했다.
    print("{}%".format('%0.3f'%ans))