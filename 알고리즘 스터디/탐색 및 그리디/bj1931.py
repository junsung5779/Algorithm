N = int(input())
time = []
last = 0 # 회의의 마지막 시간
cnt = 0
S, E = 0, 0
for i in range(N):
    S, E = map(int, input().split());
    time.append([S,E])

time = sorted(time, key=lambda a: a[0]) # 시작 시간을 기준으로 오름차순 정렬
print(time)
print('-----------------------------------------------------')
time = sorted(time, key=lambda a: a[1]) # 종료 시간을 기준으로 다시 오름차순 정렬
print(time)

for i,j in time:
    if i >= last:   # 다음 회의의 시작시간이 현재 회의의 마지막 시간보다 크거나 같을 경우
        cnt += 1
        last = j
print(cnt)