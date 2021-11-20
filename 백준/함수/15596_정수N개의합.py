def solve(a):
    ans = 0
    # 리스트 a의 0번째 인덱스부터 마지막인덱스(=리스트a의 길이)까지 순회하면서
    for i in a:
        # ans에다가 a리스트의 i번째 인덱스의 값을 차례대로 저장한다 
        ans += i
    # ans값을 반환
    return ans