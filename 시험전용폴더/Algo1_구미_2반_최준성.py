import sys
sys.stdin = open("문제1_input.txt")

def baby_gin(num_lst):
    cnt = 0
    number = [0,0,0,0,0,0,0,0,0,0]
    # num_lst를 순회하면서
    for i in num_lst:
        # 해당 값을 1회 올린다.
        number[i] += 1
    # 모든 카운팅이 끝나고 난 후
    run = 0
    triplet = 0
    # number리스트를 순회하면서
    for j in number:
        # 트리플렛부터 먼저 검사한다
        if j == 3:
            triplet += 1
            cnt = 0
        # run을 검사한다
        # 만약 j번째 카드가 1개 있다면
        elif j == 1:
            # 카운트 횟수를 1회 올려준다.
            cnt += 1
            # 만약 카운트 횟수가 3에 도달했다면
            if cnt == 3:
                # run횟수를 1회 올려주고
                run += 1
                # 카운트 횟수를 초기화한다.
                cnt = 0
        # 연속되지 않았다면
        else:
            # 카운트 횟수를 0으로 해준다.
            cnt = 0

    # 베이비진인 모든 경우의 수
    # run이 2회인 경우
    if run == 2:
        return 1
    # run이 1회이고 triplet이 1회인 경우
    elif run == 1 and triplet == 1:
        return 1
    # triplet이 2회인 경우
    elif triplet == 2:
        return 1
    else:
        return 0





for tc in range(1,int(input())+1):
    num = input()
    num_lst = list()
    for i in range(len(num)):
        num_lst.append(int(num[i]))
    num_lst.sort()
    print("#{} {}".format(tc, baby_gin(num_lst)))