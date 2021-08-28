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

# FPS
clock = pygame.time.Clock()

# 배경 이미지 불러오기
background = pygame.image.load("C:/Users/k24m13/Desktop/python_Workspace/pygame_basic/background.png")

# 캐릭터(스프라이트) 불러오기
character = pygame.image.load("C:/Users/k24m13/Desktop/python_Workspace/pygame_basic/character.png")
character_size = character.get_rect().size # 이미지의 크기 구해옴
character_width = character_size[0] # 캐릭터의 가로 크기
character_height = character_size[1] # 캐릭터의 세로 크기
character_x_pos = screen_width / 2 - character_width / 2 # x위치가 화면 가로의 절반에 해당하는 곳에 위치
character_y_pos = screen_height - character_height # y위치가 화면 세로의 가장 아래에 해당하는 곳에 위치

# 이동할 좌표
to_x = 0
to_y = 0

# 이동 스피드
cahracter_speed = 0.5

# 적 캐릭터
enemy = pygame.image.load("C:/Users/k24m13/Desktop/python_Workspace/pygame_basic/enemy.png")
enemy_size = enemy.get_rect().size # 이미지의 크기 구해옴
enemy_width = enemy_size[0] # 캐릭터의 가로 크기
enemy_height = enemy_size[1] # 캐릭터의 세로 크기
enemy_x_pos = screen_width / 2 - enemy_width / 2 # x위치가 화면 가로의 절반에 해당하는 곳에 위치
enemy_y_pos = screen_height / 2 - enemy_height / 2 # y위치가 화면 세로의 가장 아래에 해당하는 곳에 위치


# 이벤트 루프
running = True # 게임이 진행중인가 확인

while running:
    dt = clock.tick(60) # 게임화면의 초당 프레임 수 설정

    for event in pygame.event.get(): # pygame에서 이벤트가 발생하면 이벤트를 event 변수에 저장
        if event.type == pygame.QUIT: # 발생한 이벤트가 창이 닫히는 이벤트인가 확인
            running = False # 게임이 진행중이 아님

        if event.type == pygame.KEYDOWN: # 키가 눌렸는지 확인
            if event.key == pygame.K_LEFT: # 왼쪽 방향키를 눌렀다면
                to_x -= cahracter_speed
            if event.key == pygame.K_RIGHT:
                to_x += cahracter_speed
            if event.key == pygame.K_UP:
                to_y -= cahracter_speed
            if event.key == pygame.K_DOWN:
                to_y += cahracter_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0
                
    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    # 가로 경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # 세로 경계값 처리
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    # 충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    if character_rect.colliderect(enemy_rect):
        print("충돌했어요")
        running = False

    # screen.fill((0, 0, 255))
    screen.blit(background, (0, 0)) # 배경 그리기

    screen.blit(character, (character_x_pos, character_y_pos)) # 캐릭터 그리기

    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))

    pygame.display.update() # 게임화면을 다시 그리기! (반드시 계속 호출되야댐)



# while 문이 끝나면(running = False) pygame 종료
pygame.quit()