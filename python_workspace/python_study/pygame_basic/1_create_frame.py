import pygame

pygame.init() # 반드시 필요

# 화면 크기
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))


# 화면 타이틀 설정
pygame.display.set_caption("Nado Game") # 게임 이름

# 이벤트 루프
running = True # 게임이 진행중인가 확인

while running:
    for event in pygame.event.get(): # pygame에서 이벤트가 발생하면 event 변수에 저장
        if event.type == pygame.QUIT: # 발생한 이벤트가 창이 닫히는 이벤트인가 확인
            running = False # 게임이 진행중이 아님

# while 문이 끝나면(running = False) pygame 종료
pygame.quit()