# class BigNumberError(Exception):
#     def __init__(self, msg):
#         self.msg = msg
    
#     def __str__(self):
#         return self.msg

# try:
#     print("한 자리 숫자 나누기 전용 계산기")
#     num1 = int(input("첫 번째 숫자를 입력하세요: "))
#     num2 = int(input("두 번째 숫자를 입력하세요: "))
#     if num1 >= 10 or num2 >= 10:
#         raise BigNumberError("입력값 : {}, {}".format(num1, num2))
#     print("{} / {} = {}".format(num1, num2, int(num1 / num2)))
# except ValueError:
#     print("잘못된 값을 입력하셨습니다. 한 자리 숫자만 입력하세요")
# except BigNumberError as err:
#     print("에러가 발생하였습니다. 한 자리 숫자만 입력하세요.")
#     print(err)
# finally:
#     print("계산기를 종료합니다.")

# class SoldOutError(Exception):
#     def __init__(self):
#         print("재고가 소진되어 더 이상 주문을 받지 않습니다.")


# chicken = 10
# waiting = 1
# while(True):
#     try:
#         print("[남은 치킨 : {}]".format(chicken))
#         order = int(input("치킨 몇 마리 주문하시겠습니까? >>> "))
#         if order <= 0:
#             raise ValueError
#         if order > chicken:
#             print("재료가 부족합니다")
#         else:
#             print("[대기번호 {}번] {} 마리 주문 완료되었습니다.".format(waiting, order))
#             chicken -= order
#             waiting += 1
#         if chicken == 0:
#             raise SoldOutError     
#     except SoldOutError:
#         break
#     except ValueError:
#         print("잘못된 값을 입력하였습니다.")









# import Traver.Thailand
# from Traver import *
# trip_to = Vietnam.VietnamPackeage()
# trip_to_tha = Thailand.ThailandPackage()
# trip_to.detail()
# trip_to_tha.detail()




# import inspect
# import random
# print(inspect.getfile(Thailand))




# import random
# print(dir(random))
# lst = [1, 2, 3]
# print(dir(list))


# 파이썬 제공 외장함수
# import glob
# import os
# import time
# import datetime

# today = datetime.date.today()
# td = datetime.timedelta(days=100)
# print("우리가 만난지 100일째는", today + td)
# print("오늘 날짜는 ", datetime.date.today())
# # print(time.localtime())
# print(time.strftime("%Y-%m-%d %H:%M:%S"))
# print(os.getcwd())
# folder = "sample_dir"

# if os.path.exists(folder):
#     print(folder)
#     os.rmdir(folder)
#     print("폴더를 삭제 하였습니다.")
# else:
#     os.makedirs(folder)
#     print(folder, "폴더를 생성하였습니다.", sep=",")
# print(glob.glob("*.py"))

# print(os.listdir())





# byme 모듈 만들고 불러오기
from byme import sign
sign()