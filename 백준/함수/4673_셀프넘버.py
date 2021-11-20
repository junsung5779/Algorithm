# 생성자를 넣으면 다음 수를 만드는 함수
def next(T):
    sum1 = T // 10000
    sum2 = (T // 1000) - (sum1 * 10)
    sum3 = (T // 100) - (sum1 * 100) - (sum2 * 10)
    sum4 = (T // 10) - (sum1 * 1000) - (sum2 * 100) - (sum3 * 10)
    sum5 = T % 10
    # 5자리인경우
    if T//10000 != 0:
        sum = T+sum1+sum2+sum3+sum4+sum5
    # 4자리인경우
    elif T//1000 != 0:
        sum = T+sum2+sum3+sum4+sum5
    # 3자리인경우
    elif T//100 != 0:
        sum = T+sum3+sum4+sum5
    # 2자리인경우
    elif T//10 != 0:
        sum = T+sum4+sum5
    # 1자리인경우
    elif T//10 == 0:
        sum = T+sum5
    return sum

arr=list()
# 1부터 10000까지 순회하면서
for i in range(1,10001):
    # 생성자를 arr리스트에 추가한다
    arr.append(next(i))
    # i가 생성자가 들어있는 리스트에 없는경우(=생성자가 아닌 경우)
    if i not in arr:
        # i를 출력한다.
        print(i)
# print(extract(39))