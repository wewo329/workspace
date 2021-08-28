# index(원소): 리스트 내 특정한 원소의 인덱스를 찾기
list1 = ['나동빈', '강종구', '이태일', '박한울', '이상욱']
print(list1.index('강종구'))
# reverse(): 리스트의 원소를 뒤집기
list1 = [1, 2, 3]
list1.reverse()
print(list1)
list1.reverse()
print(list1[::-1])
# sum(리스트 자료형): 리스트의 모든 원소의 합
list1 = [1, 5, 10 , 8, 2 ,3]
print(sum(list1))
# range(시작, 끝): 특정 범위를 지정
my_range = range(5, 10)
list1 = list(range(5, 10))
print(list1)
# list(특정 범위): 특정 범위의 원소를 가지는 리스트를 반환
# all() / any(): 리스트의 모든 원소가 참인지 판별 / 하나라도 참인지 판별
list1 = [True, False, True]
print(all(list1))
print(any(list1))
# enumerlate(): 리스트에서 인덱스와 원소를 함께 추출
list1 = ['나동빈', '강종구', '이태일', '박한울', '이상욱']
reusult = list(enumerate(list1))
print(reusult)
for i, k in enumerate(list1):
    print('인덱스: ', i, '값 : ', k)
# sort(): 리스트의 원소를 정렬
my_list = ['나동빈', '강종구', '이태일', '박한울', '이상욱']
my_list.sort()
print(my_list)
# count(): 특정한 원소의 개수를 추출
my_list = ['나동빈', '강종구', '이태일', '강종구', '이상욱']
print(my_list.count('강종구'))
# del: 리스트의 특정 원소를 제거
my_list = ['123', '235', '123479']
del my_list[1]
print(my_list)
# insert(인덱스, 값): 리스트에 특정 원소를 삽입
my_list.insert(1, 'index')
print(my_list)
print(my_list.index('index'))
# append(): 리스트의 가장 마지막 원소로서 원소를 삽입
my_list.append('append')
print(my_list)