word = input()
sum = 0
phone = [['A','B','C'],['D','E','F'],['G','H','I'],['J','K','L'],['M','N','O'],['P','Q','R','S'],['T','U','V'],['W','X','Y','Z']]
for i in word:
    # phone 리스트 안의 요소를 순회하면서
    for j in range(len(phone)):
        # j번째 인덱스의 요소(리스트)의 길이만큼 반복하면서
        for k in range(len(phone[j])):
            # 해당 좌표에 있는 값 중에 i와 일치하는 것이 있으면
            if i == phone[j][k]:
                # j+3을 더한다(2를 누를 때 3초가 걸리므로)
                sum += j+3
print(sum)