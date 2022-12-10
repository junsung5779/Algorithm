def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0 for _ in range(bridge_length)]  # 다리 길이와 같은 길이의 값이 0으로 된 리스트 생성

    while bridge:   # 트럭의 대기열의 길이가 0이 되면 반복문 종료

        answer += 1     # 경과한 시간(다리를 건널 때 1초가 걸린다.)
        bridge.pop(0)   # 트럭이 다리를 건넌다.

        if truck_weights:
            if sum(bridge) + truck_weights[0] <= weight:    # 다리 위에 있는 트럭의 총 무게(sum(bridge)) + 다음 대기열에 있는 트럭의 무게(truck_weights) <= 다리가 감당할 수 있는 무게(weight) 인 경우
                t = truck_weights.pop(0)    # 트럭의 대기열의 첫 번째 트럭을
                bridge.append(t)    # 다리로 지나가게 한다.
            else:   # 아니라면,
                bridge.append(0)    # 0 을 인위적으로 추가해서 다리의길이를 유지 

    return answer