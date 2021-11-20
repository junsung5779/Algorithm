from collections import deque

# 계산하는 함수
# BFS
def cal(a,b):
    # deque가 시간복잡도가 1이기때문에 시간초과를 안나게 하려고 썼다
    a = deque(a)
    tmp_lst = [0]*1000001
    while a:
        deque
        num,count = a.popleft()
        # 한번 사용한 숫자를 다시 사용하면 도돌이표 되었다는 뜻이므로
        # 한번 사용한 숫자를 다시 사용하지 않기 위해 tmp_lst의 인덱스값을 사용한 값으로 설정한다.
        if tmp_lst[num] == 0:
            tmp_lst[num] = 1
            # 만약 이전단계에서 연산했던 결과값이 내가 찾고자 하는 갑소가 같다면
            if num == b:
                # 연산횟수를 반환
                return count
            # 이 숫자로 네가지 연산해주기
            # 리스트에 추가
            if 1 <= num+1 <= 1000000:
                a.append((num+1,count+1))
            if 1 <= num-1 <= 1000000:
                a.append((num-1,count+1))
            if 1 <= num*2 <= 1000000:
                a.append((num*2,count+1))
            if 1 <= num-10 <= 1000000:
                a.append((num-10,count+1))
    return 0


T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    tmp = [(N,0)]
    res = cal(tmp,M)
    print('#{} {}'.format(tc, res))