import math

def solution(progresses, speeds):
    answer = []
    days = []
    for i in range(len(progresses)):
        days.append(math.ceil((100 - progresses[i]) / speeds[i]))
    max_index = 0
    for i in range(1, len(days)):
        if days[i] > days[max_index]:
            answer.append(i - max_index)
            max_index = i
    answer.append(len(progresses) - max_index)
        
    return answer

print(dir(math))