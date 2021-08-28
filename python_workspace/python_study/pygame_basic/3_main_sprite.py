import pygame

pygame.init() # 반드시 필요

# 화면 크기
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))
# screen.fill((0, 0, 255))
# screen.blit(background, (0, 0)) # 배경 그리기


# 화면 타이틀 설정
pygame.display.set_caption("Nado Game") # 게임 이름

# 배경 이미지 불러오기
background = pygame.image.load("C:/Users/gurdn/Desktop/python_Workspace/pygame_basic/background.png")

# 캐릭터(스프라이트) 불러오기
character = pygame.image.load("C:/Users/gurdn/Desktop/python_Workspace/pygame_basic/character.png")
character_size = character.get_rect().size # 이미지의 크기 구해옴
character_width = character_size[0] # 캐릭터의 가로 크기
character_height = character_size[1] # 캐릭터의 세로 크기
character_x_pos = screen_width / 2 - character_width / 2 # x위치가 화면 가로의 절반에 해당하는 곳에 위치
character_y_pos = screen_height - character_height # y위치가 화면 세로의 가장 아래에 해당하는 곳에 위치



# 이벤트 루프
running = True # 게임이 진행중인가 확인

while running:
    for event in pygame.event.get(): # pygame에서 이벤트가 발생하면 event 변수에 저장
        if event.type == pygame.QUIT: # 발생한 이벤트가 창이 닫히는 이벤트인가 확인
            running = False # 게임이 진행중이 아님

    # screen.fill((0, 0, 255))
    screen.blit(background, (0, 0)) # 배경 그리기

    screen.blit(character, (character_x_pos, character_y_pos)) # 캐릭터 그리기

    pygame.display.update() # 게임화면을 다시 그리기! (반드시 계속 호출되야댐)



# while 문이 끝나면(running = False) pygame 종료
pygame.quit()