import pygame
from random import randint

pygame.init()

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("run away from shit")

clock = pygame.time.Clock()

background  = pygame.image.load("C:/Users/gurdn/Desktop/python_Workspace/pygame_basic/background.png")
player = pygame.image.load("C:/Users/gurdn/Desktop/python_Workspace/pygame_basic/dog.png")
shit = pygame.image.load("C:/Users/gurdn/Desktop/python_Workspace/pygame_basic/ddong.png")

player_size = player.get_rect().size
player_width = player_size[0]
player_height = player_size[1]
player_x_pos = screen_width / 2 - player_width / 2 
player_y_pos = screen_height - player_height

shit_size = shit.get_rect().size
shit_width = shit_size[0]
shit_height = shit_size[1]

shits = []
ran = range(0, 7)
for i in ran:
    shits.append([randint(0, int(screen_width - shit_width)), randint(-1000, -50)])
    
game_font = pygame.font.Font(None, 40)

to_x = 0

shit_speed = 10
player_speed = 0.5

start_time = pygame.time.get_ticks()

running = True

while running:
    FPS = clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= player_speed
            if event.key == pygame.K_RIGHT:
                to_x += player_speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0

    player_x_pos += to_x * FPS

    # 플레이어 경계값 처리
    if player_x_pos < 0:
        player_x_pos = 0
    elif player_x_pos > screen_width - player_width:
        player_x_pos = screen_width - player_width
    
    shits = [ [w[0], w[1] + shit_speed] for w in shits]

    i = 0
    for shit_x_pos, shit_y_pos in shits:
        if shit_y_pos > screen_height:
            shits[i][0] = randint(0, int(screen_width - shit_width))
            shits[i][1] = randint(-500, -50)
        i += 1

    # 충돌 처리
    player_rect = player.get_rect()
    player_rect.left = player_x_pos + 10
    player_rect.top = player_y_pos + 5


    for shit_x_pos, shit_y_pos in shits:
        shit_rect = shit.get_rect()
        shit_rect.left = shit_x_pos
        shit_rect.top = shit_y_pos
        if player_rect.colliderect(shit_rect):
            print("game over")
            running = False 

    # shit_rect = shit.get_rect()
    # shit_rect.left = shit_x_pos
    # shit_rect.top = shit_y_pos

    # if player_rect.colliderect(shit_rect):
    #     print("게임 오버")
    #     running = False

    # 시간 계산(타이머)
    elapsed_time = (pygame.time.get_ticks() - start_time) / 1000

    if elapsed_time <= 11:
        timer = game_font.render(str(int(elapsed_time)), True, (0, 0, 0))
    elif elapsed_time > 11 and elapsed_time <= 26:
        timer = game_font.render(str(int(elapsed_time)), True, (255, 0, 0))
        shit_speed = 14
    elif elapsed_time > 26:
        timer = game_font.render(str(int(elapsed_time)), True, (255, 0, 0))
        shit_speed = 17

    screen.blit(background, (0, 0))
    screen.blit(player, (player_x_pos, player_y_pos))
    
    
    for shit_x_pos, shit_y_pos in shits:
        screen.blit(shit, (shit_x_pos, shit_y_pos))

    screen.blit(timer, (10, 10))

    # screen.blit(shit, (shit_x_pos, shit_y_pos))

    pygame.display.update()

pygame.quit()