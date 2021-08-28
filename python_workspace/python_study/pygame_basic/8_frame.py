# import pygame
# ##################################################################
# # 기본 초기화 (반드시 해야 하는 부분)
 
# pygame.init() # 반드시 필요

# # 화면 크기
# screen_width = 480 # 가로 크기
# screen_height = 640 # 세로 크기
# screen = pygame.display.set_mode((screen_width, screen_height))
# # screen.fill((0, 0, 255))
# # screen.blit(background, (0, 0)) # 배경 그리기


# # 화면 타이틀 설정
# pygame.display.set_caption("Nado Game") # 게임 이름

# # FPS
# clock = pygame.time.Clock()

# ##################################################################

# # 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트 등)

# running = True

# while running:
#     dt = clock.tick(60) # 게임화면의 초당 프레임 수 설정

#     # 2. 이벤트 처리 (키보드, 마우스 등)

#     # 3. 게임 캐릭터 위치 처리

#     # 4. 충돌 처리

#     # 5. 화면에 그리기

#     pygame.display.update() # 게임화면을 다시 그리기! (반드시 계속 호출되야댐)

# pygame.quit()

from random import randint
while True:
    print(randint(1, 100))