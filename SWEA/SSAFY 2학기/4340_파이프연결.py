import sys, pprint
sys.stdin = open("input4340.txt")
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    pipe = [list(map(int, input().split())) for _ in range(N)]
    pprint.pprint(pipe)
