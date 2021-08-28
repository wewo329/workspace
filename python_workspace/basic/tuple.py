# 튜플은 리스트와 비슷한 자료형
# 변경이 불가함
my_tuple = 1, 2, 3
for i in my_tuple:
    print(i)

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
my_tuple = list1, list2
print(my_tuple)

my_tuple[1][2] = 50
print(my_tuple)
