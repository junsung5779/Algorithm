answer = 0
N = 0
visited = []

# k: 현재 피로도
# cnt: 던전을 돈 횟수
# dungeons[i][0]: 던전을 돌기 위한 최소 필요 피로도
# dungeons[i][1]: 던전을 돌고난 후 소모되는 소모 필요도
def dfs(k, cnt, dungeons):
    global answer
    if cnt > answer:  # 던전을 돈 횟수가 최댓값보다 크다면
        answer = cnt  # 최댓값 갱신

    for i in range(N):  # 시작던전을 0부터 마지막 인덱스 까지 설정하기
        # 현재 피로도가 던전의 최소 필요 피로도보다 같거나 크고
        # 방문하지 않은 상태라면
        if k >= dungeons[i][0] and not visited[i]:
            visited[i] = 1  # 방문한 상태로 변경
            # 현재 피로도에서 소모 피로도 만큼 차감
            # 카운트 횟수 1회 증가
            dfs(k - dungeons[i][1], cnt + 1, dungeons)
            # 위에서 dfs 돌아간 이후 for문의 다음 i에 대해서 탐색해야 하므로 방문조건 초기화
            visited[i] = 0


def solution(k, dungeons):
    global N, visited
    N = len(dungeons)  # 던전의 개수
    visited = [0] * N  # 방문한 던전 표시
    dfs(k, 0, dungeons)
    return answer