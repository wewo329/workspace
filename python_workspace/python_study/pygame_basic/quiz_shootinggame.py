import pygame
import os

pygame.init()

# 스크린 크기 정의
screen_width = 600
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))

# 게임 타이틀 처리
pygame.display.set_caption("Shoot")

# 이미지 파일 위치 처리
path = os.path.dirname(__file__)
image_path = os.path.join(path, "shooting_images")

# 이미지 불러오기
backscreen = pygame.image.load(os.path.join(image_path, "backscreen.png"))
player = pygame.image.load(os.path.join(image_path, "player.png"))
enemy = pygame.image.load(os.path.join(image_path, "enemy.png"))

# 스크린 크기 정의
backscreen_size = backscreen.get_rect().size
backscreen_width = backscreen_size[0]
backscreen_height = backscreen_size[1]

# 플레이어 크기, 위치 정의
player_size = player.get_rect().size
player_width = player_size[0]
player_height = player_size[1]
player_x_pos = screen_width / 2 - player_width / 2
player_y_pos = screen_height + 10

player_speed = 3

player_to_x = 0
player_to_y = 0

player_Fy_pos = screen_height - player_height - 20

# 몹 크기, 위치 정의
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = screen_width / 2 - enemy_width / 2
enemy_y_pos = -1 * enemy_height

# 실행 코드 값
end_code = 0
running = True
emergence = True

# 시작 부분
while emergence:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end_code = 1
            emergence = False

    # 플레이어 등장
    if player_y_pos != player_Fy_pos:
        player_y_pos -= 1

    # 몹 등장
    elif player_y_pos == player_Fy_pos and enemy_y_pos != 20:
        enemy_y_pos += 1
    
    else:
        emergence = False

    screen.blit(backscreen, (0, 0))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))
    screen.blit(player, (player_x_pos, player_y_pos))

    pygame.display.update()

while running:
    if end_code == 1:
        print("you exited game")
        running = False

    # 이벤트 체크
    for event in pygame.event.get():
        # 종료 버튼 클릭시
        if event.type == pygame.QUIT:
            end_code = 1
            # print("you exited game")
            # running = False
        
        # 키보드 입력값 처리
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_to_x -= player_speed
            if event.key == pygame.K_RIGHT:
                player_to_x += player_speed
            if event.key == pygame.K_UP:
                player_to_y -= player_speed
            if event.key == pygame.K_DOWN:
                player_to_y += player_speed
            #if event.key == pygame.K_SPACE:
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player_to_y = 0

    player_x_pos += player_to_x
    player_y_pos += player_to_y

    screen.blit(backscreen, (0, 0))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))
    screen.blit(player, (player_x_pos, player_y_pos))
    

    pygame.display.update()


pygame.quit()