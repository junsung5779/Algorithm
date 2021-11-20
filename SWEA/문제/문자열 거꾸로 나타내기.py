# 문자열 뒤집기
# 뒤에서부터 출력하기
# 실제로 배열만들어서 자리 바꾸기
# 슬라이싱 이용하기
s = "Reverse this Strings1"
s1 = s[::-1]
print(s1)
# 반복문을 사용하려면 리스트를 만들어야 함
sList = list(s)
sList2 = list(s)
reverseStr = list()
# 뒤에서부터 0까지 -1씩 진입하기
for i in range(len(s)-1,-1,-1):
    reverseStr.append(s[i])
print(reverseStr)

for i in range(0, len(s)//2):
    sList2[i], sList2[len(s)-i-1] = sList2[len(s)-i-1], sList2[i]
print(sList2)