import sys
sys.stdin = open('input1427.txt')
lst=[]
ans=''
num=str(input())
for i in num:
    lst.append(int(i))
lst.sort(reverse=True)
# 리스트를 그대로 숫자로
for j in lst:
    ans += str(j)
print(int(ans))
# 이거 왜틀림?