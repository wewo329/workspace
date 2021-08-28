import time
from PIL import ImageGrab

time.sleep(5)

for i in range(1, 11):
    img = ImageGrab.grab() # 현재 스크린 이미지를 가져오는 함수
    img.save("image{}.png".format(i)) # 이미지를 저장하는 함수
    time.sleep(2)