T=int(input())
for tc in range(1,T+1):
    res = ""
    repeat, word = map(str, input().split())
    for i in word:
        for j in range(int(repeat)):
            res += i
    print(res)

# 마음에 드는 다른사람 정답
#######################
# n=int(input())
# while n>0:
#     a,b=input().split(' ')
#     for i in b:
#         print(i*int(a), end='')
#     print()
#     n-=1