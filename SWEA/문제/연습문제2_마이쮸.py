# 마이쮸의 개수
N = 20

# 튜플형태로 queue초기화
#(0,0) [0]: 사람 번호, [1]: 직전까지 받았던 마이쮸의 개수
queue = [(1,0)] # 초기화

new_people = 1
last_people = 0

while N > 0:
    # num: 받으러온 사람
    # cnt: 저번까지 받은 개수
    num, cnt = queue.pop(0)

    # 마지막으로 받으러 온 사람
    last_people = num
    # 저번 보다는 하나 더 챙겨가자
    cnt += 1
    # num이라는 친구가 cnt개수만큼 가져감
    N -= cnt
    new_people += 1
    # 맨뒤로가서 다시 줄을 섬
    queue.append((num,cnt))
    # 새로운 사람도 줄섬
    queue.append((new_people, 0))
print(last_people)