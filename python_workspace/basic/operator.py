# 축약형 => 증감 연산자
# 증감 연산자 : 기존에 사용하던 증가/감소 기능을 짧게 사용
a = 0
a /= 10 # a = a + 10과 동일
print(a)

# 관계 연산자 : 두 개의 값을 비교
A = 1
B = 2
'''
A >= B
A == B      # 같은지 판단  A = B 와 혼동하지 않기
A !=B       # 다른지 판단
A > B
'''

A = 'A'
B = 'B'
A >= B      # 문자의 경우  사전순


#논리 연산자 : 여러 개의 수식을 논리적으로 연산
a = False
b = True
print(a and b)
print(a or b)
print(not a)

if 3 > 5 or 7 < 10:
    print('야호')