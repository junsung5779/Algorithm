arr=["Enter uid1234 Muzi", "Enter uid4567 Prodo"]
split_arr=[]
for i in range(len(arr)):
    split_arr.append(arr[i].split())
print(arr[0].split())
print(arr[1].split())
print(split_arr)
data = []
data.append(f"{split_arr[0][2]}")
data.append(f"{split_arr[0][2]}")
print(f"{split_arr[0][2]}")
print(data)


### 풀이
def solution(record):
    answer = []
    ans = []
    # 일단 record 리스트 데이터부터 사용하기 편하게 가공하자.
    arr = []
    # ex) [["Enter", "uid1234", "Muzi"], ["Enter", "uid4567", "Prodo"]]
    for i in range(len(record)):
        arr.append(record[i].split())
    # 가공된 데이터 arr를 순회하며
    # 경우의 수에 따라 정해진 형태로 result 배열에 메세지를 append하자
    for i in arr:
        data = []
        # 입장, 닉변, 퇴장은 arr[0]에 따라 결정된다.
        # 입장한 경우
        # 닉변한 경우를 고려하여 데이터에 유저 아이디 값을 포함한 배열을 answer에 삽입
        # data = ["Enter", "uid1234", "Muzi님이 들어왔습니다."]
        if i[0] == "Enter":
            data.append(f"{i[0]}")
            data.append(f"{i[1]}")
            data.append(f"{i[2]}님이 들어왔습니다.")
            # answer = [["Enter", "uid1234", "Muzi님이 들어왔습니다."]]
            answer.append(data)
        # 퇴장한 경우
        if i[0] == "Leave":
            data.append(f"{i[0]}")
            data.append(f"{i[1]}")
            data.append(f"{i[2]}님이 나갔습니다.")
            answer.append(data)
        # 닉변한 경우
        if i[0] == "Change":
            # 닉변한 유저의 유저 아이디 값의 다음 인덱스 값의 닉네임을 전부 변경
            for j in answer:
                if j[1] == i[1]:
                    # 입장 메세지인 경우
                    if j[0] == "Enter":
                        j[2] = f"{i[2]}님이 들어왔습니다."
                    # 퇴장 메세지인 경우
                    if j[0] == "Leave":
                        j[0] = f"{i[2]}님이 나갔습니다."
    for k in answer:
        ans.append(k[2])
    return ans