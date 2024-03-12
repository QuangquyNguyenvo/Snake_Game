import pygame
import random
import time

# Khởi tạo Pygame
pygame.init()
screen_size = 700
screen = pygame.display.set_mode((screen_size+2, screen_size+2))
pygame.display.set_caption('Game con rắn')
clock = pygame.time.Clock()

# Màu sắc
WHITE = (255, 255, 255)
GREEN = (0, 225, 0)
GREEN2 = (0, 250, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Khởi tạo trò chơi
font = pygame.font.Font(None, 30)
snake_speed = 15
snakes = [[0, 0], [1, 0], [2, 0]]
change_to = 'right'
direction = 'side'
point = 0
table = 0
block = 20
foodx = random.randint(0, screen_size//block - 1)
foody = random.randint(0, screen_size//block - 1)

def game_over():
    time.sleep(3)
    pygame.quit()
    quit()

def draw_grid():
    for i in range(screen_size // block):
        pygame.draw.line(screen, WHITE, (0, i * block), (screen_size, i * block))
        pygame.draw.line(screen, WHITE, (i * block, 0), (i * block, screen_size))

def update_snake():
    global point, snake_speed, foodx, foody
    if snakes[-1][0] == foodx and snakes[-1][1] == foody:
        snakes.insert(0, [foodx, foody])  # Thêm phần tử mới vào đầu danh sách
        foodx = random.randint(0, screen_size//block - 1)
        foody = random.randint(0, screen_size//block - 1)
        point += 1
        snake_speed += 1

def draw_game():
    screen.fill(BLACK)
    if table == 1:
        draw_grid()
    text_score = font.render("Score: " + str(point), True, WHITE)
    screen.blit(text_score, (5, 5))
    for snake in snakes:
        pygame.draw.rect(screen, GREEN, (snake[0]*block, snake[1]*block, block, block))
    pygame.draw.rect(screen, GREEN2, (snakes[-1][0]*block, snakes[-1][1]*block, block, block))
    pygame.draw.rect(screen, RED, (foodx*block, foody*block, block, block))
    tmp=0
    for i, snake in enumerate(snakes):
        if tmp == len(snakes) - 1:
            if direction == 'left' or direction == 'right':
                pygame.draw.circle(screen, BLACK, (snake[0]*block+8, snake[1]*block+8), 2.75)
                pygame.draw.circle(screen, BLACK, (snake[0]*block+8, snake[1]*block+14), 2.75)
            if direction == 'up' or direction == 'down':
                pygame.draw.circle(screen, BLACK, (snake[0]*block+8, snake[1]*block+8), 2.75)
                pygame.draw.circle(screen, BLACK, (snake[0]*block+14, snake[1]*block+8), 2.75)
        tmp+=1
    pygame.display.update()

def handle_events():
    global run, change_to, table
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                change_to = 'left'
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                change_to = 'right'
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                change_to = 'up'
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                change_to = 'down'
            if event.key == pygame.K_TAB:
                table = 1 - table

def change_direction():
    global direction
    if change_to == 'up' and direction != 'down':
        direction = 'up'
    if change_to == 'down' and direction != 'up':
        direction = 'down'
    if change_to == 'left' and direction != 'right':
        direction = 'left'
    if change_to == 'right' and direction != 'left':
        direction = 'right'

def move_snake():
    global direction
    if direction == 'left':
        snakes.append([snakes[-1][0]-1, snakes[-1][1]])
        snakes.pop(0)
    if direction == 'right':
        snakes.append([snakes[-1][0]+1, snakes[-1][1]])
        snakes.pop(0)
    if direction == 'up':
        snakes.append([snakes[-1][0], snakes[-1][1]-1])
        snakes.pop(0)
    if direction == 'down':
        snakes.append([snakes[-1][0], snakes[-1][1]+1])
        snakes.pop(0)

def check_game_over():
    if snakes[-1][0] < 0 or snakes[-1][0] >= screen_size//block or snakes[-1][1] < 0 or snakes[-1][1] >= screen_size//block:
        game_over()
    for s in range(len(snakes)-1):
        if snakes[s][0] == snakes[-1][0] and snakes[s][1] == snakes[-1][1]:
            game_over()

def draw_menu():
    screen.fill(BLACK)
    title_font = pygame.font.Font(None, 72)
    title_text = title_font.render("SNAKE GAME", True, WHITE)
    title_rect = title_text.get_rect(center=(screen_size//2, screen_size//4))
    screen.blit(title_text, title_rect)

    menu_font = pygame.font.Font(None, 36)
    play_text_normal = menu_font.render("Play", True, WHITE)
    play_text_selected = pygame.font.Font(None, 40).render("Play", True, RED)
    play_rect = play_text_normal.get_rect(midleft=(screen_size//3, screen_size//2))
    screen.blit(play_text_selected if selected_option == 0 else play_text_normal, play_rect)

    settings_text_normal = menu_font.render("Settings", True, WHITE)
    settings_text_selected = pygame.font.Font(None, 40).render("Settings", True, RED)
    settings_rect = settings_text_normal.get_rect(midright=(screen_size*2//3, screen_size//2))
    screen.blit(settings_text_selected if selected_option == 1 else settings_text_normal, settings_rect)

    pygame.display.update()

def settings_menu():
    global snake_speed
    screen.fill(BLACK)
    title_font = pygame.font.Font(None, 48)
    title_text = title_font.render("Settings", True, WHITE)
    title_rect = title_text.get_rect(midtop=(screen_size//2, screen_size//4))
    screen.blit(title_text, title_rect)

    speed_font = pygame.font.Font(None, 36)
    speed_text = speed_font.render(f"Snake Speed: _____", True, WHITE)
    speed_rect = speed_text.get_rect(midtop=(screen_size//2, screen_size//2))
    screen.blit(speed_text, speed_rect)

    pygame.display.update()

    input_speed = ""
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
                elif event.key == pygame.K_BACKSPACE:
                    input_speed = input_speed[:-1]
                elif event.key == pygame.K_RETURN:
                    if input_speed.isdigit():
                        snake_speed = int(input_speed)
                    return
                else:
                    input_speed += event.unicode

        speed_text = speed_font.render(f"Snake Speed: {input_speed.rjust(5, '_')}", True, WHITE)
        screen.blit(speed_text, speed_rect)
        pygame.display.update()

# Vòng lặp chính
run = True
menu_option = 0  # 0: Menu chính, 1: Chơi game, 2: Cài đặt
selected_option = 0  # 0: Play, 1: Settings

while run:
    if menu_option == 0:  # Menu chính
        draw_menu()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    selected_option = 0  # Chọn Play
                elif event.key == pygame.K_RIGHT:
                    selected_option = 1  # Chọn Settings
                elif event.key == pygame.K_RETURN:
                    if selected_option == 0:  # Chọn Play
                        menu_option = 1
                    else:  # Chọn Settings
                        menu_option = 2

    elif menu_option == 1:  # Chơi game
        handle_events()
        change_direction()
        update_snake()  # Cập nhật rắn trước khi di chuyển
        move_snake()
        draw_game()
        check_game_over()
        clock.tick(snake_speed)

    elif menu_option == 2:  # Cài đặt
        settings_menu()
        menu_option = 0  # Quay lại menu chính sau khi thoát cài đặt

pygame.quit()
quit()
