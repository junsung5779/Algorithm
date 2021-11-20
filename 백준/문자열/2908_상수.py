A, B = input().split()
tmp_A = ''
tmp_B = ''
for i in range(len(A)-1,-1,-1):
    tmp_A += A[i]
    # 둘 다 세자리수이므로 그냥 인덱스 자체는 같이 받아준다
    tmp_B += B[i]
A,B = int(tmp_A), int(tmp_B)
if A >= B:
    print(A)
else:
    print(B)

# 마음에 드는 풀이
##############################
# # a와b를 문자열으로 받은 다음
# a, b = input().split()
# # 앞뒤를 뒤집은 다음 정수형으로 각각 c, d에 저장했다
# c = int(a[::-1])
# d = int(b[::-1])
# if c >= d:
#     print(c)
# else:
#     print(d)