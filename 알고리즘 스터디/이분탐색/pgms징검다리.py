# 이 문제가 이분탐색이라고 생각한 이유
# 1. 문제에서 '각 지점 사이의 거리의 최솟값' 이라는 부분
# 2. 제한사항에서 터무니 없이 큰 범위가 있는 경우
#
# 최악의 경우
# distance = 1,000,000,000
# 바위 = 1개
# n = 1 인 경우 바위의 각 지점 사이에 바위 갯수가 0개 이므로
# 최악의 경우는 distance이다.
# 따라서 end = distance
# start = 1

distance = 25
rocks = [2, 14, 11, 21, 17]
n = 2
start = 1
end = distance
def binarySearch(rocks, n, distance):
    answer = 0
    start, end = 0, distance

    rocks.sort()    # 돌 정렬
    while start <= end:
        mid = (start + end) // 2  # 중간값을 구한다.
        del_stones = 0  # 제거한 돌을 카운트하기 위한 변수
        pre_stone = 0  # 기준이되는 돌(시작지점)
        for rock in rocks:  # 징검다리를 돌면서
            if rock - pre_stone < mid:  # 돌사이의 거리가 가정한 값보다 작으면 제거한다.
                del_stones += 1
            else:  # 아니라면 그 돌을 새로운 기준으로 세운다.
                pre_stone = rock

            if del_stones > n:  # 제거된 돌이 문제 조건 보다 크면 for문을 나온다
                break

        if del_stones > n:  # 제거된 돌이 너무 많으면 가정한 값이 큰 것이므로 범위를 작은 쪽으로 줄인다.
            end = mid - 1
        else:  # 반대라면 큰 쪽으로 줄인다.
            answer = mid
            start = mid + 1

    return answer
