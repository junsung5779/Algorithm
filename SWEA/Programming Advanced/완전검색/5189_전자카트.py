import sys
sys.stdin = open("input5189.txt")

# 배열의 가로 길이를 size로 받는다.
# 1부터 size까지 순회하면서
# 만약 임시리스트에 해당 숫자가 없으면
# append
# 재귀
# pop

def pick():
    global min_num_lst
    # 만약 tmp_lst의 길이와 한 변의 길이가 같다면
    if len(tmp_lst) == size:
        # tmp_lst 출력
        # print(tmp_lst)
        min_num = 9999
        # 임시리스트에 있는 인덱스 순서대로 방문하고 마지막에 0을 넣어야 하는데 append(0) 하니 오류나서 그냥
        # num에 마지막 방문값 넣은채로 시작했다.
        num = arr[tmp_lst[size-1]][0]
        for j in range(1,size):
            num += arr[tmp_lst[j-1]][tmp_lst[j]]
        min_num_lst.append(num)
        # tmp_lst 반환
        return tmp_lst
    # 1부터 한 변의 길이까지 순회하면서
    for i in range(1,size):
        # 해당 숫자가 tmp_lst에 없으면
        if i not in tmp_lst:
            # tmp_lst에 추가
            tmp_lst.append(i)
            # tmp_lst에 i를 추가한 상태로 재귀
            pick()
            # tmp_lst에 append한 i 다시 삭제
            tmp_lst.pop()

T=int(input())
for tc in range(1,T+1):
    min_num_lst = list()
    tmp_lst = [0]
    # 배열의 사이즈를 입력받는다.
    size = int(input())
    used = [0]*size
    # 입력값을 이차원배열로 저장
    arr = [list(map(int, input().split())) for _ in range(size)]
    #   [[0, 18, 34],
    #    [48, 0, 55],
    #    [18, 7, 0 ]] .....
    pick()
    print("#{} {}".format(tc, min(min_num_lst)))


