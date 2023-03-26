arr=list(map(str, input().split('-')))
# 55-50+40
ans = 0
for i in range(len(arr)):
    tmp_arr = sum(map(int, arr[i].split('+')))
    if i == 0:
        ans += tmp_arr
    else:
        ans -= tmp_arr
print(ans)

# 55-50+40-50+40+30-20-10+20