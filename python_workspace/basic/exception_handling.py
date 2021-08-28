try:                # try 구문 안에서 오류가 발생시 except 안에 있는 코드를 실행
    print(3 / 0)
except Exception as e:  # 오류 메시지 를 e에 담는다.
    print(e)
else:               # try 구문 안에서 오류가 발생하지 않을시 실행
    print('예외 없이 성공적으로 실행되었습니다.')
finally:            # 오류의 여부와 상관없이 예외 처리가 끝났을시 실행되는 구문
    print('예외 처리를 마칩니다.')