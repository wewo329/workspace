# 문자 자료형 뒤집기
str = 'Hello World'
print(str[::-1])
# len(): 문자열의 길이를 출력
# isalpha(): 특정한 문자열이 문자로만 이루어져 있는지 확인
str = 'Hello World'
print(str.isalpha())
# isdigit(): 특정한 문자열이 숫자로만 이루어져 있는지 확인
str = '12345'
print(str.isdigit())
# isalnum(): 특정한 문자열이 문자와 숫자로만 이루여저 있는지 확인
str = 'abc123'
print(str.isalnum())
# join(리스트 자료형): 여러개의 문자열을 구분자와 함께 합치는 함수
list = ['Hello', 'Wolrd', '홍길동']
print(','.join(list))
# sorted(문자열 자료형): 각 문자를 정렬하는 함수
str = 'helloworld'
list = sorted(str)                  # 오름차순
print(''.join(list))
list = sorted(str, reverse=True)    # 내림차순
print(''.join(list))
# split(토큰): 문자열을 토큰에 따라 분리하는 함수
str = "I wanna watch a movie"
list = str.split()
print(list)
# find(서브 문자열): 문자열 내부에 존재하는 서브 문자열이 시작하는 인덱스 번호를 반환
str = 'I like you'
print(str.find('like'))
# upper(), lower(): 문자열을 대문자, 소문자로 변환
str = 'I Love you'
print(str.upper())
print(str.lower())
# strip(): 좌우로 특정한 문자열을 제거하는 함수
str = 'tt Hello World t'
print(str.strip('t'))
# eval(): 문자열 수식을 계산해주는 수식
exp = '(203+502)*3-(30/6)'
print(eval(exp))
