import sys
sys.stdin = open("문제1_input1.txt")

T=int(input())
arr=[]
for tc in range(T):
    N,M = map(int, input().split())
    for n in range(N):
        arr.append(list(map(int, input().split())))