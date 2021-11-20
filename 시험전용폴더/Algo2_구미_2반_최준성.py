import sys
sys.stdin = open("문제2_input.txt")

def binary_search(num_lst, search_num):
    l = 0
    r = len(num_lst)
    m = (l+r)//2
    l_lst = num_lst[:m]
    r_lst = num_lst[m+1:r]
    pass


for tc in range(1,int(input())+1):
    N,M = map(int, input().split())
    arr = list()
    search_num = list(map(int, input().split()))
    num_lst = list(map(int, input().split()))
    print(search_num)
    print(num_lst)