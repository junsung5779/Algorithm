
# # 문자열을 입력받는다
# word = input()
# # 사용되었는지 여부를 확인할 임시리스트를 초기화한다.
# tmp_lst=list()
# # 결과와 카운트값을 저장할 임시리스트2를 초기화한다.
# # 입력받은 문자열을 순회하면서
# for i in word:
#     # 해당 알파벳이 임시리스트 안에 대문자형태로든 소문자형태로든 존재하지 않으면
#     if i not in tmp_lst:
#         # 대문자인경우
#         if 65 <= ord(i) <= 90:
#             # 해당문자와 소문자도 tmp_lst에 추가
#             tmp_lst.append(i)
#             tmp_lst.append(chr(ord(i)+32))
#         # 소문자인경우
#         if 97 <= ord(i) <= 122:
#             # 해당문자와 대문자도 tmp_lst에 추가
#             tmp_lst.append(i)
#             tmp_lst.append(chr(ord(i)-32))
#     # 해당 알파벳이 임시리스트안에 대문자형태로든 소문자형태로든 존재한다면
#     else:
#         # 해당 알파벳이 대문자인경우
#         if 65 <= ord(i) <= 90:
#             # 그대로 임시리스트2에 추가
#
#         # 해당 알파벳이 소문자인경우
#         else:
#             # 대문자로 바꾼 후 임시리스트2에 추가
#
# print(tmp_lst)



# 새 풀이
########################
# 문자열을 입력받는다.
word = input()
# A~Z알파벳이 문자열에 몇개 있는지 확인할 수 있는 리스트
alphabet = [0]*26
# 입력받은 문자열을 순회하면서
for i in word:
    # 해당 문자가 대문자라면
    if 65 <= ord(i) <= 90:
        # 위치에 해당하는 인덱스의 값을 1증가
        alphabet[ord(i)-65] += 1
    # 해당 문자가 소문자라면
    else:
        # 대문자로 바꾸고 그 위치에 해당하는 인덱스의 값을 1증가
        alphabet[ord(i)-32-65] += 1

# alphabet리스트를 반복하면서 최대횟수 찾기
max_cnt = -9999
for j in alphabet:
    if j > max_cnt:
        max_cnt = j

# alphabet리스트를 반복하면서 최대횟수인 알파벳의 갯수를 카운트
same = 0
for k in alphabet:
    if k == max_cnt:
        same += 1

# 최대횟수인 알파벳이 2개이상 있을 시
if same > 1:
    # ? 출력
    print('?')
# 최대횟수인 알파벳이 유일할시
else:
    # alphabet리스트를 돌면서 최댓값이 있는 인덱스를 알아내어 해당 알파벳 출력
    for n in range(len(alphabet)):
        if max_cnt == alphabet[n]:
            print(chr(n+65))