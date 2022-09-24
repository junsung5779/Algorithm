# ########## hamoon의 풀이 ##########
import sys
from collections import deque
sys.stdin = open('input18528.txt')
T = int(sys.stdin.readline())   # 테스트케이스 횟수 입력받기
queue = deque([])
for tc in range(T): # 테스트케이스 횟수만큼 반복하면서
    stack = sys.stdin.readline().split() # 띄워쓰기를 구분점으로 입력받는다.
    # push인 경우
    if stack[0] == 'push':
        queue.append(stack[1])  # 숫자를 append
    # pop인 경우
    elif stack[0] == 'pop':
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    # size인 경우
    elif stack[0] == 'size':
        print(len(queue))
    # empty인 경우
    elif stack[0] == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    # front인 경우
    elif stack[0] == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    # back인 경우
    elif stack[0] == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)
        

# # ['push 1', 'push 2', 'front', 'back', 'size', 'empty', 'pop', 'pop', 'pop', 'size', 'empty', 'pop', 'push 3', 'empty', 'front']
# # print(list)


########## hamoon의 풀이 2 ##########
# import sys
# sys.stdin = open('input18528.txt')
#
# # 테스트케이스 반복횟수를 입력받는다.
# T = int(input())
# # 정수를 저장하는 큐 생성 및 초기화
# queue = []
# # word가 pop일 때마다 .pop() 을 쓰지 않고(시간복잡도 때문) 대신에 cnt += 1로 해서 해당 리스트를 읽는다.
# cnt = 0
# #테스트케이스를 반복하면서
# for i in range(T):
#     # 단어를 입력받아
#     word = str(input())
#     # 케이스에 따라 분류한다.
#
#     # push인 경우 (해당 문자열 길이가 push(공백)(숫자) 이기 때문에 최소 길이가 6이다)
#     if len(word) >= 6:
#         # 정수 X를 큐에 넣는다.
#             # 해당 문자열의 마지막 단어(숫자)를 큐에 넣는다.
#         queue.append(word[-1])
#     # pop인 경우
#     elif word == 'pop':
#         if len(queue)-cnt == 0: # 큐에 들어가있는 정수가 없는 경우 -1을 출력
#             print(-1)
#         else:   # 큐에 정수가 들어있는 경우
#             print(queue[cnt]) #cnt만큼의 인덱스를 제외하고 큐의 가장 앞에 있는 정수를 출력
#             cnt += 1
#     # size인 경우
#     elif word == 'size':
#         print(len(queue))   # 큐에 들어있는 정수의 개수를 출력
#     # empty인 경우
#     elif word == 'empty':
#         # 큐가 비어있으면 1, 아니면 0을 출력
#         if len(queue)-cnt == 0:
#             print(1)
#         else:
#             print(0)
#     # front인 경우
#     elif word == 'front':
#         if len(queue)-cnt == 0:  # 큐에 들어가있는 정수가 없는 경우 -1을 출력
#             print(-1)
#         else:  # 큐에 정수가 들어있는 경우
#             print(queue[cnt])     #cnt만큼의 인덱스를 제외하고 큐의 가장 앞에 있는 정수를 출력
#     # back인 경우
#     elif word == 'back':
#         if len(queue)-cnt == 0:  # 큐에 들어가있는 정수가 없는 경우 -1을 출력
#             print(-1)
#         else:  # 큐에 정수가 들어있는 경우
#             print(queue[-1])  # 큐의 가장 뒤에 있는 정수를 출력

########## 해설 ##########
# import sys
# input = sys.stdin.readline
#
# # 테스트케이스 반복횟수를 입력받는다.
# T = int(input())
# # 정수를 저장하는 큐 생성 및 초기화
# queue = []
# # pop명령어가 나올 시 리스트에서 .pop()하지 않고 인덱스를 읽기 위해 cnt값 생성 및 초기화
# cnt = 0
# for i in range(T):
#     comm = input().strip()
#     # push인 경우
#     if comm.split()[0] =='push':
#         queue.append(int(comm.split()[1]))
#     # pop인 경우
#     # comm이 pop일 때마다 .pop() 을 쓰지 않고(시간복잡도 때문) 대신에 cnt += 1로 해서 해당 리스트를 읽는다
#     elif comm.split()[0]=='pop':
#         if len(queue)-cnt ==0:  # 큐에 들어가있는 정수가 없는 경우 -1을 출력
#             print(-1)
#         else:   # 큐에 정수가 들어있는 경우
#             print(queue[cnt])   #cnt만큼의 인덱스를 제외하고 큐의 가장 앞에 있는 정수를 출력
#             cnt += 1
#     # size인 경우
#     elif comm.split()[0]=='size':
#         print(len(queue)-cnt)   #cnt만큼의 인덱스를 제외하고 큐의 길이를 출력
#     # empty인 경우
#     elif comm.split()[0] =='empty':
#         # 큐가 비어있으면 1, 아니면 0을 출력
#         if len(queue)-cnt ==0:
#             print(1)
#         else:
#             print(0)
#     # front인 경우
#     elif comm.split()[0]=='front':
#         if len(queue)-cnt ==0:  # 큐에 들어가있는 정수가 없는 경우 -1을 출력
#             print(-1)
#         else:
#             print(queue[cnt])   #cnt만큼의 인덱스를 제외하고 큐의 가장 앞에 있는 정수를 출력
#     # back인 경우
#     elif comm.split()[0]=='back':
#         if len(queue)-cnt==0:   # 큐에 들어가있는 정수가 없는 경우 -1을 출력
#             print(-1)
#         else:
#             print(queue[-1])    # 큐의 가장 뒤에 있는 정수를 출력