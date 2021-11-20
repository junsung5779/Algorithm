import pprint
import sys
sys.stdin = open('input210412.txt')


# 해당 인덱스의 암호코드
num_list = [
    [0,0,0,1,1,0,1],
    [0,0,1,1,0,0,1],
    [0,0,1,0,0,1,1],
    [0,1,1,1,1,0,1],
    [0,1,0,0,0,1,1],
    [0,1,1,0,0,0,1],
    [0,1,0,1,1,1,1],
    [0,1,1,1,0,1,1],
    [0,1,1,0,1,1,1],
    [0,0,0,1,0,1,1],
]

def cal(lst):
    sum = (lst[0]+lst[2]+lst[4]+lst[6])*3+(lst[1]+lst[3]+lst[5])+lst[7]
    return sum

def find_num(lst):
    global num_list
    res1 = list()
    for i in range(0,len(lst),7):
        for j in range(len(num_list)):
            if [lst[i],lst[i+1],lst[i+2],lst[i+3],lst[i+4],lst[i+5],lst[i+6]] == num_list[j]:
                res1.append(j)
    return res1


T = int(input())
for tc in range(1,T+1):
    N,M=map(int, input().split())
    arr = [list(str(input())) for _ in range(N)]
    res = list()
    lst1 = list()
    # 이차원배열을 순회하면서 대조리스트에 값 집어넣기
    for i in range(N):
        if len(res)==56:
            break
        for j in range(M):
            # 만약 lst1의 길이가 7보다 작다면
            if len(lst1) < 7:
                # 리스트에 현재값 추가
                lst1.append(int(arr[i][j]))
            # 만약 lst1의 길이가 7이라면
            elif len(lst1) == 7:
                # lst1의 첫번째 인덱스의 값을 빼고
                del lst1[0]
                # 뒤에 하나씩 append하는식으로 lst1의 길이를 7로 유지한다.
                lst1.append(int(arr[i][j]))
            # 만약 lst1이 다음과 같은 형태가 된다면
            if lst1 == [1,0,0,0,0,0,0]:
                # [해당 인덱스 - 61]의 인덱스부터 [해당 인덱스 - 6]의 인덱스까지 리스트에 저장
                for k in range(j-61,j-6+1):
                    res.append(int(arr[i][k]))
                break

    sum = find_num(res)
    # print(sum)
    if cal(sum)%10 == 0:
        print("#{} {}".format(tc,sum[0]+sum[1]+sum[2]+sum[3]+sum[4]+sum[5]+sum[6]+sum[7]))
    else:
        print("#{} {}".format(tc,0))
