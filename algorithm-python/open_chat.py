def solution(record):
        STATUS = 0
        UID = 1
        NAME = 2
        splited = [once.split(" ") for once in record]
        logs = []
        inform = dict()
        for once in splited:
            if once[STATUS] == "Enter":
                logs.append((once[STATUS], once[UID]))
                inform[once[UID]] = once[NAME]
            elif once[STATUS] == "Leave":
                logs.append((once[STATUS], once[UID]))
            else:
                inform[once[UID]] = once[NAME]

        result = []
        for log in logs:
            if log[STATUS] == "Enter":
                result.append(inform[log[UID]]+"님이 들어왔습니다.")
            else:
                result.append(inform[log[UID]]+"님이 나갔습니다.")
        # ==
        # result = [inform[log[UID]]+("님이 들어왔습니다." if log[STATUS] == "Enter" else "님이 나갔습니다.") for log in logs]

        return result

records = [["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234",\
    "Enter uid1234 Prodo", "Change uid4567 Ryan"]]

results = [solution(record) for record in records]
print(results)