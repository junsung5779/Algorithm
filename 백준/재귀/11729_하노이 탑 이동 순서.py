def hanoi(num, start, end, sub):
    if num == 1:    # 이동해야 할 원반 갯수가 하나만 있다면
        print('{} {}'.format(start, end))   # 그 하나를 이동시키고
        return  # 바로 함수 종료
    # 시작 기둥에서 목표 기둥까지 옮기는 스텝
    # 1. 시작 기둥의 제일 아래 원판 빼고 나머지 원판이 보조기둥에 가 있어야 함
    # 따라서 원판이 num개라면 num-1개의 원판을 보조기둥으로 옮기는 하노이 재귀가 필요함
    hanoi(num-1, start, sub, end)
    # 2. 시작 기둥의 제일 아래 원판을 목표기둥으로 이동
    print('{} {}'.format(start, end))
    # 3. 보조기둥에 꽂혀있는 나머지 원판들을 목표기둥으로 이동시켜야 한다.
    # 따라서 하노이 재귀에 들어갈 때는
    # 원래 보조기둥을 시작기둥으로 사용
    # 원래 목표기둥을 목표기둥으로 사용
    # 원래 시작기둥을 보조기둥으로 사용
    hanoi(num-1, sub, end, start)

num=int(input())
print(2**num-1)
hanoi(num, 1, 3, 2)