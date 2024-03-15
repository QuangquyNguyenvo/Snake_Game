def single_mode(Game_state, snake_speed):
    import pygame
    import random
    import time
    # Khởi tạo Pygame
    pygame.init()
    screen_size = 700
    screen = pygame.display.set_mode((screen_size+2, screen_size+2))
    pygame.display.set_caption('SNAKE GAME BY THANH & QUY__SINGLE PLAYER MODE')
    clock = pygame.time.Clock()
    #Màu sắc
    WHITE = (255, 255, 255)
    WHITE2 = (100, 100, 100)
    BLACK = (0, 0, 0)
    GREEN = (0, 255, 0)
    RED = (200, 0, 0)
    ORANGE = (255,128,0)
    YELLOW = (255,255,0)
    GREEN2 = (0, 153, 0)
    BLUE = (0,0,255)
    BLUE2 = (0,204,204)
    BP = (120,0,255)
    PURPLE = (153,0,153)
    PINK = (255,0,255)
    colors = [RED,ORANGE,YELLOW,GREEN2,BLUE2,BP,PURPLE]
    # Khởi tạo trò chơi
    font = pygame.font.Font(None, 30)
    change_to = ''
    direction = ''
    point = 0
    table = 0
    block = 20
    foodx = random.randint(0, screen_size//block - 1)
    foody = random.randint(0, screen_size//block - 1)
    run = True
    snakes = [[screen_size // block // 4, 17], [screen_size // block // 4, 16], [screen_size // block // 4, 15]]
    turn_on_rainbow = False
    check_pause = False
    speed_original = snake_speed
    def Start_menu():
        global Game_state
        font_start = pygame.font.Font(None, 50)
        screen.fill(BLACK)
        text_start = font_start.render("Press 'Space' to start",True, WHITE)
        screen.blit(text_start,(screen_size // 2 -  text_start.get_width() // 2 ,screen_size // 2))
        pygame.display.update()

    def draw_grid():
        for i in range(screen_size // block):
            pygame.draw.line(screen, WHITE2, (0, i * block), (screen_size, i * block))
            pygame.draw.line(screen, WHITE2, (i * block, 0), (i * block, screen_size))
    
    #def single_mode():
    while run:
        if Game_state == 'Start':
            Start_menu()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        Game_state = ''
                        run = False
                    if event.key == pygame.K_SPACE:
                        Game_state = 'Game'
        if Game_state == 'Over':
            screen.fill(BLACK)
            game_over_font = pygame.font.Font(None, 50)
            game_over_text = game_over_font.render("Game Over! Your score: " + str(point), True, WHITE)
            restart_text = game_over_font.render("Press R to restart", True, WHITE)
            screen.blit(game_over_text, (screen_size//2 - game_over_text.get_width()//2, screen_size//2 - game_over_text.get_height()//2))
            screen.blit(restart_text, (screen_size//2 - restart_text.get_width()//2, screen_size//2 + restart_text.get_height()))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        single_mode('Game',speed_original)
                    if event.key == pygame.K_ESCAPE:
                        Game_state = ''
                        run = False
        if Game_state == 'Game':    
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        if turn_on_rainbow == False:
                            turn_on_rainbow = True
                        else:
                            turn_on_rainbow = False
                    if event.key == pygame.K_ESCAPE:
                        Game_state = ''
                        run = False
                    if event.key == pygame.K_SPACE and Game_state == 'Game':
                        if not check_pause:
                            check_pause = True
                        else:
                            check_pause = False
                    if check_pause == False:
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
            if check_pause == False:
                if change_to == 'up' and direction != 'down':
                    direction = 'up'
                if change_to == 'down' and direction != 'up' and direction != '':
                    direction = 'down'
                if change_to == 'left' and direction != 'right':
                    direction = 'left'
                if change_to == 'right' and direction != 'left':
                    direction = 'right'
            else:
                direction = ''
            if snakes[-1][0] == foodx and snakes[-1][1] == foody:
                snakes.insert(0, [foodx, foody])  # Thêm phần tử mới vào đầu danh sách
                foodx = random.randint(0, screen_size//block - 1)
                foody = random.randint(0, screen_size//block - 1)
                point += 1
                snake_speed += 1
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
            
            screen.fill(BLACK)
            if table == 1:
                draw_grid()
            text_score = font.render("Score: " + str(point), True, WHITE)
            screen.blit(text_score, (5, 5))
            color_cnt = 0
            for snake in snakes:
                if turn_on_rainbow == False:
                    pygame.draw.rect(screen, GREEN, (snake[0]*block, snake[1]*block, block, block))
                else:
                    pygame.draw.rect(screen, colors[color_cnt], (snake[0]*block, snake[1]*block, block, block))
                    if color_cnt == len(colors) - 1:
                        color_cnt = 0
                    else:
                        color_cnt += 1
            pygame.draw.rect(screen, RED, (foodx*block, foody*block, block, block))
            tmp=0
            for i, snake in enumerate(snakes):
                if tmp == len(snakes) - 1:
                    if direction == 'left' or direction == 'right' or direction == '' and change_to == 'left' or direction == '' and change_to == 'right':
                        pygame.draw.circle(screen, BLACK, (snake[0]*block+14, snake[1]*block+6), 2.75) #(mắt trái, độ cao x)
                        pygame.draw.circle(screen, BLACK, (snake[0]*block+14, snake[1]*block+14), 2.75) 
                    if direction == 'up' or direction == 'down' or direction == '' and change_to == 'up' or direction == '' and change_to == 'down' or direction == '' and change_to == '':
                        pygame.draw.circle(screen, BLACK, (snake[0]*block+6, snake[1]*block+14), 2.75) #(độ cao)
                        pygame.draw.circle(screen, BLACK, (snake[0]*block+14, snake[1]*block+14), 2.75)
                tmp+=1
            
            # Kiểm tra nếu đầu rắn chạm vào thân
            for s in range(len(snakes) - 1):
                if snakes[s][0] == snakes[-1][0] and snakes[s][1] == snakes[-1][1]:
                    Game_state = 'Over'
            #Truong hop ran 1 dung vao tuong
            if snakes[-1][0] < 0 or snakes[-1][0] > screen_size // block - 1 or snakes[-1][1] < 0 or snakes[-1][1] > screen_size // block - 1:
                Game_state = "Over"
            # Trở lại viền
            #if snakes[-1][0] < 0:
            #    snakes.append([screen_size//block - 1, snakes[-1][1]])
            #    snakes.pop(0)
            #if snakes[-1][0] > screen_size//block - 1:
            #    snakes.append([0, snakes[-1][1]])
            #    snakes.pop(0)
            #if snakes[-1][1] < 0:
            #    snakes.append([snakes[-1][0], screen_size//block - 1])
            #    snakes.pop(0)
            #if snakes[-1][1] > screen_size//block - 1:
            #    snakes.append([snakes[-1][0], 0])
            #    snakes.pop(0)
        pygame.display.update()
        clock.tick(snake_speed)