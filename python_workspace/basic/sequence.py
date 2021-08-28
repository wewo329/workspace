# 시퀀스 : 문자열, 리스트, 튜플 등의 인덱스를 가지는 자료형

string1 = 'Hello Wolrd'
string2 = ", Python"
list = ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'l', 'r', 'd']
tuple = 'H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'l', 'r', 'd'

print(len(string1 + string2))
print('H' in string1)
print(tuple.count('l'))

for i in string1:
    print(i)

print(string1[0: 5])
print(list[0: 5])
print(tuple[0: 5])
