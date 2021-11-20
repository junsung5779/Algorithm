# 테스트케이스 개수를 입력받는다.
T = int(input())
# 1부터 T까지 테스트케이스를 순회하면서
for tc in range(1,T+1):
    # 길이가 N인 문자열 str1을 입력받고
    str1 = str(input())
    # 길이가 M인 문자열 str2를 입력받는다.
    str2 = str(input())
    # 최대 결과값을 초기화한다.
    max_res = 0
    # str1의 문자열을 순회하면서
    for i in range(len(str1)):
        # 결과값을 초기화한다.
        res = 0
        # str2의 문자열을 순회하면서
        for j in range(len(str2)):
            # str2와 비교해서 같다면 결과값(res)에 1을 더한다.
            if str1[i] == str2[j]:
                res += 1
        # 만약 최대 결과값(max_res)이 결과값(res)보다 작다면,
        if max_res < res:
        # 최대 결과값(max_res)에 결과값(res)이 저장된다.
            max_res = res
    print("#{} {}".format(tc, max_res))