S=input()
arr=list()
res=""
for a in S:
    if a not in arr:
        arr.append(a)
    else:
        arr.append(0)
# chr <-> ord
# chr(97)~chr(122)

# a부터 z까지 순회하면서
for i in range(97,123):
    # 해당 알파벳이 입력받은 문자열 안에 있는 경우
    if chr(i) in arr:
        # 입력받은 문자열 리스트 전체를 돌면서
        for j in range(len(arr)):
            # 문자의 위치를 찾았다면
            if chr(i) == arr[j]:
                # 해당위치의 인덱스와 공백을 res에 더함
                res += str(j)+" "
    # 해당 알파벳이 입력받은 문자열 안에 없다면
    else:
        # -1과 공백을 res에 더함
        res += '-1'+" "
print(res)

# 마음에 드는 다른사람 답안
####################################################################
# S = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#
# word = input()
# for i in range(len(word)):
#     for j in range(len(S)):
#         if S[j] == word[i]:
#             S[j] = i
# for i in range(len(S)):
#     if type(S[i]) != int:
#         S[i] = -1
#
# for i in range(len(S)):
#     print(S[i], end = ' ')