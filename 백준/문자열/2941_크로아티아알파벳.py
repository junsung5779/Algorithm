word = input()
arr1 = ['c=','c-','dz=','d-','lj','nj','s=','z=']
# 리스트를 반복하면서
for i in arr1:
    # 크로아티아 알파벳만 문자열"*"로 대체시킨다
    word = word.replace(i, '*')
# word의 길이를 반환
print(len(word))
