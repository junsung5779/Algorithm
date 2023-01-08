# 입력값을 편하게 사용하기 위해 배열로 받는다.
white = list(map(int, input().split()))
# 출력할 결과의 초깃값
ans = ""
# 비교 기준점
black = [1,1,2,2,2,8]
# white의 길이만큼 반복문을 돌면서
for i in range(len(white)):
    black[i] -= white[i]    # black의 i번째 인덱스의 값에서 white의 i번째 인덱스의 값을 빼준값을 black의 [i]번째 인덱스에 저장
    # ans에 black[i]의 값과 공백을 더한다.
    # 단, black[i]는 숫자(int)형, " "는 문자(str)형 이므로 서로다른 타입을 계산할 수 없기 때문에 black[i]를 문자열로 변경해서 더해준다.
    ans += str(black[i]) + " "
print(ans)