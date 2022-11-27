def solution(record):
    answer = []
    ans = []
    # 일단 record 리스트 데이터부터 사용하기 편하게 가공하자.
    arr = []
    for i in range(len(record)):
        arr.append(record[i].split())
    # arr = [["Enter", "uid1234", "Muzi"], ["Enter", "uid4567", "Prodo"]]

    # 가공된 데이터 arr를 순회하며
    for i in arr:  # i == ["Enter", "uid4567", "Prodo"]
        # 경우의 수에 따라 정해진 형태로 data 배열에 메세지를 append하자
        data = []  # 데이터는 for문을 도는 동안 계속 사용되어야 하므로 초기화
        # 입장, 닉변, 퇴장은 arr[0]에 따라 결정된다.
        # 입장한 경우
        if i[0] == "Enter":

            # 신규유저인 경우
            # 복귀유저인 경우

            # 닉변한 경우를 고려하여 데이터에 유저 아이디 값을 포함한 배열을 answer에 삽입
            data.append(f"{i[0]}")
            data.append(f"{i[1]}")
            data.append(f"{i[2]}님이 들어왔습니다.")
            # data = ["Enter", "uid4567", "Prodo님이 들어왔습니다."]
            answer.append(data)
            print(answer)
            # answer = [["Enter", "uid4567", "Prodo님이 들어왔습니다."]]
        # 퇴장한 경우
        elif i[0] == "Leave":
            data.append(f"{i[0]}")
            data.append(f"{i[1]}")
            data.append(f"{i[2]}님이 나갔습니다.")
            answer.append(data)
        # 닉변한 경우
        elif i[0] == "Change":  # i == ["Change", "uid4567", "Ryan"]
            # 닉변한 유저의 유저 아이디 값과 같은 메세지의 닉네임을 전부 변경
            # 입장 또는 퇴장 메세지 == j, 닉변했다는 메세지 == i
            for j in answer:  # j == ["Enter", "uid4567", "Prodo님이 들어왔습니다."]
                if j[1] == i[1]:  # 닉변하기 전 메세지의 유저 아이디와 닉변 한 유저아이디가 같을 경우
                    # 입장 메세지인 경우
                    if j[0] == "Enter":
                        j[2] = f"{i[2]}님이 들어왔습니다."
                    # 퇴장 메세지인 경우
                    if j[0] == "Leave":
                        j[2] = f"{i[2]}님이 나갔습니다."
    for k in answer:  # k == ["Enter", "uid4567", "Prodo님이 들어왔습니다."]
        ans.append(k[2])
    return ans  # ans = ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]