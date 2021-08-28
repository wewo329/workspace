# dictionary (사전) : 키(Key)와 값(Value) 한 쌍을 원소로 가지는 자료형
my_dict = {}
my_dict['안녕'] = 'Hello'
my_dict['기적'] = 'Miracle'
my_dict['노력'] = 'Effort'
my_dict['안녕'] = 'Hi'
print(my_dict)
del my_dict['기적']

for i, k in enumerate(my_dict):
    print('[인덱스 : ', i, '] 한글: ', k, '/ 영어: ', my_dict[k])

keys = my_dict.keys()
key_list = list(keys)
print(key_list)

values = my_dict.values()
value_list = list(values)
print(value_list)

if '노력' in my_dict:
    print('[노력] 이라는 키가 존재합니다')

# my_dict.clear()
# print(my_dict)


scores = {}
scores['나동빈'] = 78
scores['이태일'] = 99
scores['박한울'] = 89
print(sorted(scores)) # 키로 정렬하기
print(sorted(scores, reverse=True)) # 키로 내림차순 정렬하기
print(sorted(scores.values())) # 값으로 정렬하기
print(sorted(scores.values(), reverse=True)) # 값으로 내림차순 정렬하기