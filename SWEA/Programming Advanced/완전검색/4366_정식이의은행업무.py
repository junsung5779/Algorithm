import sys
sys.stdin = open('input_4366.txt')

# 2진수
# 1개만 틀린 리스트의 요소중 하나만 바꾼 모든 리스트를 임시리스트에 저장
# 3진수
# 1개만 틀린 리스트의 요소중 하나만 바꾼 모든 리스트를 임시리스트에 저장

for tc in range(1, int(input())+1):
    binary_list = list()
    ternary_list = list()
    tmp_list1 = list()
    tmp_list2 = list()
    tmp_list3 = list()
    tmp_list4 = list()
    A = input()
    B = input()
    for i in A:
        binary_list.append(int(i))
    for j in B:
        ternary_list.append(int(j))

    for a in range(len(binary_list)):
        for b in range(2):
            if b != binary_list[a]:
                n = binary_list[a]
                binary_list[a] = b
                tmp_list1.append(list(binary_list))
                binary_list[a] = n

    for c in range(len(ternary_list)):
        for d in range(3):
            if d != ternary_list[c]:
                m = ternary_list[c]
                ternary_list[c] = d
                tmp_list2.append(list(ternary_list))
                ternary_list[c] = m
    num_list = list()
    for q in range(len(tmp_list1)):
        num = 0
        for w in range(len(tmp_list1[q])):
            num += (tmp_list1[q][w]*pow(2,len(tmp_list1[q])-w-1))
        num_list.append(num)
    # print(num_list)

    num_list1 = list()
    for q in range(len(tmp_list2)):
        num = 0
        for w in range(len(tmp_list2[q])):
            num += (tmp_list2[q][w]*pow(3,len(tmp_list2[q])-w-1))
        num_list1.append(num)
    # print(num_list1)

    for a in num_list:
        for b in num_list1:
            if a == b:
                res = a
    print("#{} {}".format(tc, res))
