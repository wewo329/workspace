# 동일한 위치에 파일이 있을시 바로 읽을 수 있음
# open(): 파일을 특정한 모드로 여는 함수, 읽을 때는 r, 쓸 때는 w
# read(): 파일 객체로부터 모든 내용을 읽는 함수
# readline(): 파일 객체로부터 한 줄씩 내용을 읽음
# readlines(): 전체내용을 한 번에 리스트에 담는 함수
f = open('input.txt', 'r', encoding='UTF-8')        # 파일에 한글이 포함되어 있을 경우 encoding 구문을 써주어야 함
f.seek(9)   # 9바이트를 뛰고 읽기 시작함
data = f.read()
print(data)
f.close()


f = open('input.txt', 'r', encoding='UTF-8')
count = 0
while count < 3:
    data = f.readline()
    count += 1
    print('%d번째 줄: %s' %(count, data), end='')
f.close()
print('\n')

f = open('input.txt', 'r', encoding='UTF-8')
list1 = f.readlines()
for i, data in enumerate(list1):
    print('%d번째 줄: %s' % (i + 1, data), end='')
f.close()

# with: 파일의 클로즈 부분을 안써도 됨
with open('input.txt', 'r', encoding='UTF-8') as f:
    list1 = f.readlines()
    for i, data in enumerate(list1):
        print('%d번째 줄 : %s' % (i + 1, data), end='')

def process(filename):
    with open(filename, 'r') as f:
        my_dict = {}
        data = f.read()
        for i in data:
            if i in my_dict:
                my_dict[i] += 1
            else:
                my_dict[i] = 1
    return my_dict

dict = process('input.txt')
dict = sorted(dict.items(), key=lambda a:a[1], reverse=True)
print(dict)
for data, count in dict:
    if data == '\n' or data == ' ':
        continue
    print('{}번째 출현 : {}'.format(count, data))