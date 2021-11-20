
def btc(data,cnt):
    global i
    # 남은 충전횟수 = 리스트의 i번 인덱스의 값
    charged = data[i]
    i += 1
    # 충전횟수가 남은경우
    if charged >= 1:
        # 충전을 하는 경우
        # 해당 인덱스의 값(충전지 용량)을 저장
        btc(data,cnt)
        # 충전을 안하는 경우
        charged -= 1
        btc(data,cnt)
    # 충전횟수가 안남은경우 충전을 하는 경우
    else:



# 테스트케이스 입력받기
for tc in range(1, int(input())+1):
    # 충전되어있는 용량의 인덱스
    i = 0
    # 충전횟수 초기화
    count = 0
    # N : 정류장 수
    tmp = list(map(int, input().split()))
    # N: 정류장 횟수
    N = tmp[0]
    # arr: 정류장 별 배터리 용량 리스트
    arr = tmp[1:]
    # 입력값에 마지막 정류장이 없었으므로 마지막 정류장 인덱스를 사용하기 위해 append 해준다.
    arr.append(0)
    btc(arr,cnt)



