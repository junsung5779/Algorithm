def solution(a, b, g, s, w, t):
    answer = (10 ** 9) * (10 ** 5) * 4

    start = 0
    # 최악의 경우
    # 걸리는 최소 시간(왕복) : 2
    # 금 따로 은 따로(한 도시에 금,은만 있을 경우) : 2
    # 광물의 최대 무게 : 10**9
    # 도시의 최대 개수 : 10**5

    end = (10 ** 9) * (10 ** 5) * 4 # 최악의 경우에 걸리는 시간!

    while start <= end: # 종료 조건 설정
        mid = (start + end) // 2    # 단위: 시간
        # 신 도시의 현재 금, 은, 금+은 갯수
        gold = 0
        silver = 0
        total = 0

        for i in range(len(g)): # 도시의 갯수 만큼 반복문 돌기
            # i번째 도시의 현재 정보
            now_gold = g[i]
            now_silver = s[i]
            now_weight = w[i]
            now_time = t[i]

            # 주어진 시간 내에서 왕복할 수 있는 횟수
            move_cnt = mid // (now_time * 2)

            # 편도로 이동할 수 있으면 편도 추가
            if mid % (now_time * 2) >= now_time:
                move_cnt += 1

            gold += now_gold if (now_gold < move_cnt * now_weight) else move_cnt * now_weight
            silver += now_silver if (now_silver < move_cnt * now_weight) else move_cnt * now_weight
            total += now_gold + now_silver if (now_gold + now_silver < move_cnt * now_weight) else move_cnt * now_weight

        # 만약 신 도시의 현재 금 갯수가 필요한 금 갯수 보다 같거나 많거나
        # 신 도시의 현재 은 갯수가 필요한 은 갯수 보다 같거나 많거나
        # 신 도시의 현재 금 + 은 갯수가 필요한 은 + 금 갯수 보다 같거나 많다면
        # 이분 탐색
        if gold >= a and silver >= b and total >= a + b:
            end = mid - 1
            # 제일 처음: 최악의 시간과 mid 중 작은 것이 answer
            # 이후 while문 돌 때 마다: answer값과 이번 mid 값 중 더 작은 값이 answer
            answer = min(answer, mid)
        else:   # 신도시에 필요한 금, 은, 금+은 의 갯수중 어느 하나라도 부족하다면
            # 이분탐색
            start = mid + 1

    return answer

# 다른 사람들의 풀이를 보고 깨달은점: start=0, 최악인 경우에 걸리는 초를 end로 두고 start와 end 값으로 중단점(mid)를 찍고
# 이분 탐색을 하는것이 큰 전제