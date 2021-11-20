sentence = input()
counting = False
word_count = 0
# 문장을 순회하면서
for alphabet in sentence:
    # 만약 알파벳이 있어야 할 자리에 공백(스페이스)이 있을때
    if alphabet == " ":
        # 알파벳을 세고 있는 상태였다면
        if counting == True:
            # 세는것을 종료
            counting = False
        
    # 알파벳이 있어야 할 자리에 알파벳이 존재한다면
    elif alphabet != " ":
        # 만약 알파벳을 세고있지 않는 상태라면
        if counting == False:
            # 알파벳을 세고있는 상태로 변환해주고
            counting = True
            # 카운팅 횟수를 1회 증가시킨다
            word_count += 1
print(word_count)




# 마음에 드는 풀이
#######################################################
# word = input().split()
# print(len(word))