# 함수 : 특정한 입력을 받아 처리 후 특정한 출력을 하는 모듈을 말함
# 함수를 이용하면 코드의 반복을 줄일 수 있음
# 전역 변수 : 소스코드 전체에서 사용
# 지역 변수 : 특정한 함수(블록) 안에서만 사용 가능
a = 1       # 전역 변수
b = 1
c = '전역 변수'
sum = 0
multiply = 1

def add(a, b):      # 지역 변수
    global c        # 함수 내에서 전역 변수 사용
    sum = a + b
    print(c)
    return (sum)
print(add(a, b))


# 가변 인자 : 함수의 매개 변수가 가변적일 때 사용
def function(*a):
    global sum
    global multiply
    sum, multiply = 0, 1

    for k in a:
        sum += k
        multiply *= k

# sum, multiply = function(1, 2, 3, 8, 15)
function(1, 2, 61, 2)
print(sum, multiply)
