def solution(s):
    LENGTH = len(s)
    max_zip = int(LENGTH/2) # 문자열 길이의 1/2길이까지만 압축해도 됨
    cand = [LENGTH] # 압축된 크기별로 문자열의 길이를 보관할 리스트

    # 1부터 전체 문자열의 1/2길이까지 압축하기 위해 for문으로 반복함
    # 압축하는 크기는 zip_size라는 변수에 할당
    for zip_size in range(1, max_zip+1):
        splited = [s[i:i+zip_size] for i in range(0, LENGTH, zip_size)] # zip_size에 할당된 압축크기로 문자열을 분할해서 리스트로 반환 
                                                                        # (2일때 "ababbabb" -> "ab", "ab", "ba", "bb")
        count = 1 # 같은 문자가 몇번 반복 되었는지 체크할 변수
        string = "" # splited된 문자열을 압축시키기 위해 준비한 변수

        # 압축크기별로 분할된 문자열을 압축하기 위해 처음부터 마지막 인덱스만 제외하고 i에 받음
        # 분할된 문자열의 앞부분과 뒷부분이 일치하는지 확인하기 위해 splited 리스트값 자체를 받지 않고 인덱스로 받음
        for i in range(len(splited)-1):
            cur, nex = splited[i], splited[i+1] # 현재 분할문자와 다음 분할문자를 비교하기 위해 변수로 할당
            # 만약 현재 분할문자와 다음 분할문자가 같다면 문자의 반복 횟수(count)를 1 추가함
            if cur == nex:
                count += 1
            # 다르다면 현재까지 반복된 횟수를 분할문자와 함께 string에 이어붙임 
            else:
                string += (str(count) if count != 1 else "") + cur # 반복횟수(count)가 1이라면 분할문자만 이어붙임
                count = 1 # 반복횟수를 초기화

        string += (str(count) if count != 1 else "") + nex # 마지막 인덱스의 분할문자를 string에 이어붙임
                                                           # 위에서 압축할때 count가 초기화 된 상태라면 분할문자만,
                                                           # count가 초기화되지 않았다면 count와 함께 분할문자를 이어붙임
        cand.append(len(string)) # 압축된 문자열의 길이를 cand리스트(압축크기별 문자열 길이 보관 리스트)에 append

    answer = min(cand) # 압축된 문자열들의 길이중 가장 짧은 것을 answer에 할당

    return answer # answer 반환


print(solution("abcabcabcabcdededededede"))