import sys
sys.stdin = open("inputIMTEST.txt")

# 테스트 케이스 횟수를 입력받는다.
T = int(input())
# 테스트케이스횟수를 순회하면서
for tc in range(1,T+1):
    # N, M1, M2를 입력받는다.
    # N : 블록의 갯수
    # M1 : 첫번째 탑의 층
    # M2 : 두번째 탑의 층
    N, M1, M2 = map(int, input().split())
    # 각 상자 크기 초기화
    lst1 = [0]
    lst2 = [0]
    # 각 블록의 무게를 입력받는다
    block = list(map(int, input().split()))
    block.sort(reverse=-1)
    # block 리스트의 요소를 lst1과 lst2의 인덱스에 번갈아 집어넣는다.
    # block 리스트의 길이만큼 반복하며
    # 만약 어느 하나의 리스트의 길이가 최대에 도달한다면
    # if lst1 = M1+1
    # if lst2 = M2+1
    # 반대 리스트에 추가한다.
    for i in range(1, len(block)+1):
        # 리스트1의 길이가 최대에 도달했을 때
        if len(lst1) == M1+1:
            # 홀수 일때
            if i%2 != 0:
                lst2.append(block[i-1])
            # 짝수 일 때
            elif i%2 == 0:
                lst2.append(block[i-1])

        # 리스트2의 길이가 최대에 도달했을 때
        elif len(lst2) == M2+1:
            # 홀수 일때
            if i%2 != 0:
                lst1.append(block[i-1])
            # 짝수 일 때
            elif i%2 == 0:
                lst1.append(block[i-1])

        elif len(lst1) < M1+1 or len(lst2) < M2+1:
            # 홀수 일때
            if i%2 != 0:
                lst1.append(block[i-1])
            # 짝수 일 때
            elif i%2 == 0:
                lst2.append(block[i-1])

    # 해당 리스트의 인덱스에 인덱스 숫자만큼 곱해준다.
    for j in range(M1+1):
        lst1[j] = lst1[j]*j
    for k in range(M2+1):
        lst2[k] = lst2[k]*k

    print("#{} {}".format(tc, sum(lst1)+sum(lst2)))
