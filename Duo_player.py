def duo_mode(game_state, snakes_speed):    
    import pygame, sys, random
    # Khởi tạo
    pygame.init()
    res = 700
    block = 20
    screen = pygame.display.set_mode((res, res))
    pygame.display.set_caption("SNAKE GAME BY THANH & QUY__DUO PLAYER MODE")
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
    # Khởi tạo các biến
    run = True
    snake1_direction = ""
    snake1_check_direction = ""
    snake2_direction = ""
    snake2_check_direction = ""
    snakes1_save_direction = ""
    snakes2_save_direction = ""
    snakes = [[res // block // 4, 17], [res // block // 4, 16], [res // block // 4, 15]]
    snakes2 = [[res// block - res // block // 4, 17],[res// block - res // block // 4, 16],[res// block - res // block // 4, 15]]
    foodx = random.randint(0, res // block - 1)
    foody = random.randint(0, res // block - 1)
    point_player1 = 0
    point_player2 = 0
    turn_on_table = 0
    snakes1_turn_on_rainbow = False
    snakes2_turn_on_rainbow = False
    player_win = 0
    check_pause = False
    def reset_all_attribute():
        global snakes,snakes2,point_player1, point_player2, snake1_direction, snake1_check_direction,snake2_direction,snake2_check_direction,player_win,foodx,foody
        snakes = [[res // block // 4, 17], [res // block // 4, 16], [res // block // 4, 15]]
        snakes2 = [[res// block - res // block // 4, 17],[res// block - res // block // 4, 16],[res// block - res // block // 4, 15]]
        point_player1 = 0
        point_player2 = 0
        snake1_direction = ""
        snake1_check_direction = ""
        snake2_direction = ""
        snake2_check_direction = ""
        player_win = 0
        foodx = random.randint(0,res // block - 1)
        foody = random.randint(0,res // block - 1)


    #Man hinh truoc khi bat dau
    def Start_menu():
        font_start = pygame.font.Font(None, 50)
        screen.fill(BLACK)
        text_start = font_start.render("Bam space de bat dau",True, WHITE)
        screen.blit(text_start,(res // 2 -  text_start.get_width() // 2 ,res // 2))
        pygame.display.update()


    #hàm khởi động lại game
    def screen_restart(player_win):
        font_restart = pygame.font.Font(None, 50)
        font_restart_point = pygame.font.Font(None, 45)
        screen.fill(BLACK)
        text_point = font_restart_point.render("Score p1: " + str(point_player1), True, GREEN)
        text_point_2 = font_restart_point.render("Score p2: " + str(point_player2), True, BLUE)
        if player_win == 0:
            if point_player1 > point_player2:
                player_win = 1
            if point_player2 > point_player1:
                player_win = 2
        if player_win != 0:
            text_restart = font_restart.render("Nguoi choi " + str(player_win) + " thang, bam 'r' de choi lai", True, WHITE)
        else:
            text_restart = font_restart.render("Ket qua hoa, bam 'r' de choi lai", True, WHITE)
        screen.blit(text_point,(res // 2 - text_point.get_width() // 2 - 120, res // 2 - text_point.get_height() - 20))
        screen.blit(text_point_2,(res - res // 2 - text_point.get_width() // 2 + 120,res - res // 2 - text_point.get_height() - 20))
        screen.blit(text_restart,(res // 2 - text_restart.get_width() // 2, res // 2))
        pygame.display.update()


    while run:
        if game_state == "Start":
            Start_menu()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        game_state = "Game"
                    if event.key == pygame.K_ESCAPE:
                        run = False
                
    
        if game_state == "Over":
            screen_restart(player_win)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        duo_mode('Game',snakes_speed)
                    if event.key == pygame.K_ESCAPE:
                        run = False
                        #reset_all_attribute()


        if game_state == "Game":
            #Truong hop ran 1 dung vao tuong
            #if snakes[-1][0] < 0 or snakes[-1][0] > res // block - 1 or snakes[-1][1] < 0 or snakes[-1][1] > res // block - 1:
                #game_state = "Over"
                #player_win = 2
            #Truong hop ran 2 dung vao tuong
            #if snakes2[-1][0] < 0 or snakes2[-1][0] > res // block - 1 or snakes2[-1][1] < 0 or snakes2[-1][1] > res // block - 1:
                #game_state = "Over"  
                #player_win = 1
            #ran 1
            if snakes[-1][0] < 0:
                snakes.append((res // block - 1,snakes[-1][1]))
                snakes.pop(0)  
            if snakes[-1][0] > res // block - 1:
                snakes.append((0,snakes[-1][1]))
                snakes.pop(0)  
            if snakes[-1][1] < 0:
                snakes.append((snakes[-1][0],res // block - 1))
                snakes.pop(0)  
            if snakes[-1][1] > res // block - 1:
                snakes.append((snakes[-1][0],0))
                snakes.pop(0)      
            #ran 2
            if snakes2[-1][0] < 0:
                snakes2.append((res // block - 1,snakes2[-1][1]))
                snakes2.pop(0)  
            if snakes2[-1][0] > res // block - 1:
                snakes2.append((0,snakes2[-1][1]))
                snakes2.pop(0)    
            if snakes2[-1][1] < 0:
                snakes2.append((snakes2[-1][0],res // block - 1))
                snakes2.pop(0)  
            if snakes2[-1][1] > res // block - 1:
                snakes2.append((snakes2[-1][0],0))
                snakes2.pop(0)  


            #Truong hop dau ran 1 dung vao than
            #for s in range(len(snakes) - 1):
                #if snakes[s][0] == snakes[-1][0] and snakes[s][1] == snakes[-1][1]:
                    #game_state = "Over"
                    #player_win = 2


            #Truong hop dau ran 2 dung vao than
            #for s in range(len(snakes2) - 1):
                #if snakes2[s][0] == snakes2[-1][0] and snakes2[s][1] == snakes2[-1][1]:
                    #game_state = "Over"
                # player_win = 1
            #2 ran dung dau nhau
            if snakes[-1][0] == snakes2[-1][0] and snakes[-1][1] == snakes2[-1][1]:
                game_state = "Over"
                player_win = 0
            else:
                #Ran 1 dung than ran 2
                for s in range(len(snakes2) - 1):
                    if snakes2[s][0] == snakes[-1][0] and snakes2[s][1] == snakes[-1][1]:
                        game_state = "Over"
                        player_win = 2
                #Ran 2 dung than ran 1
                for s in range(len(snakes) - 1):
                    if snakes[s][0] == snakes2[-1][0] and snakes[s][1] == snakes2[-1][1]:
                        game_state = "Over"
                        player_win = 1


            screen.fill(BLACK)
            snake1_check_point = 0
            snake2_check_point = 0
            #Ran 1 an duoc moi
            if snakes[-1][0] == foodx and snakes[-1][1] == foody:
                foodx = random.randint(0,res // block - 1)
                foody = random.randint(0,res // block - 1)
                point_player1 += 1
                snake1_check_point = 1
            #Ran 2 an duoc moi
            if snakes2[-1][0] == foodx and snakes2[-1][1] == foody:
                foodx = random.randint(0,res // block - 1)
                foody = random.randint(0,res // block - 1)
                point_player2 += 1
                snake2_check_point = 1


            #Sinh moi    
            pygame.draw.rect(screen, RED, (foodx * block, foody * block, block, block))


            #Hien diem
            font = pygame.font.Font(None, 30)
            text_score = font.render("Score p1: " + str(point_player1), True, WHITE)
            screen.blit(text_score,(5,5))
            text_score_2 = font.render("Score p2: " + str(point_player2), True, WHITE)
            screen.blit(text_score_2,(res - 115,5))


            #Bat - tat o vuong
            if turn_on_table == 1:
                for i in range(int(res / block) + 1):
                    pygame.draw.line(screen, WHITE2, (0, i * block), (res, i * block))
                    pygame.draw.line(screen, WHITE2, (i * block, 0), (i * block, res))


            #Ve ran
            snakes1_color_cnt = 0
            for snake in snakes:
                if snakes1_turn_on_rainbow == False:
                    pygame.draw.rect(screen, GREEN, (snake[0] * block, snake[1] * block, block, block))
                else:
                    pygame.draw.rect(screen, colors[snakes1_color_cnt], (snake[0] * block, snake[1] * block, block, block))
                    if snakes1_color_cnt == len(colors) - 1:
                        snakes1_color_cnt = 0
                    else:
                        snakes1_color_cnt += 1
            snakes2_color_cnt = 0
            for snake in snakes2:
                if snakes2_turn_on_rainbow == False:
                    pygame.draw.rect(screen, BLUE2, (snake[0] * block, snake[1] * block, block, block))
                    
                else:
                    pygame.draw.rect(screen, colors[snakes2_color_cnt], (snake[0] * block, snake[1] * block, block, block))
                    if snakes2_color_cnt == len(colors) - 1:
                        snakes2_color_cnt = 0
                    else:
                        snakes2_color_cnt += 1
            #Ve mat ran
            tmp=0
            for i, snake in enumerate(snakes):
                if tmp == len(snakes) - 1:
                    if snake1_direction == 'left' or snake1_direction == 'right':
                        pygame.draw.circle(screen, BLACK, (snake[0]*block+15, snake[1]*block+6), 2.75) #(mắt trái, độ cao x)
                        pygame.draw.circle(screen, BLACK, (snake[0]*block+15, snake[1]*block+15), 2.75) 
                    if snake1_direction == 'foward' or snake1_direction == 'backward' or snake1_direction == '':
                        pygame.draw.circle(screen, BLACK, (snake[0]*block+6, snake[1]*block+6), 2.75) #(độ cao)
                        pygame.draw.circle(screen, BLACK, (snake[0]*block+15, snake[1]*block+6), 2.75)
                tmp+=1

            tmp=0
            for i, snake in enumerate(snakes2):
                if tmp == len(snakes2) - 1:
                    if snake2_direction == 'left' or snake2_direction == 'right':
                        pygame.draw.circle(screen, BLACK, (snake[0]*block+15, snake[1]*block+6), 2.75) #(mắt trái, độ cao x)
                        pygame.draw.circle(screen, BLACK, (snake[0]*block+15, snake[1]*block+15), 2.75) 
                    if snake2_direction == 'foward' or snake2_direction == 'backward' or snake2_direction == '':
                        pygame.draw.circle(screen, BLACK, (snake[0]*block+6, snake[1]*block+6), 2.75) #(độ cao)
                        pygame.draw.circle(screen, BLACK, (snake[0]*block+15, snake[1]*block+6), 2.75)
                tmp+=1        


            #Xu li su kien
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        run = False
                    #Bat tat o vuong
                    if event.key == pygame.K_TAB:
                        if turn_on_table == 0:
                            turn_on_table = 1
                        else:
                            turn_on_table = 0
                    #Bat tat rainbow_color
                    if event.key == pygame.K_r:
                        if snakes1_turn_on_rainbow == False:
                            snakes1_turn_on_rainbow = True
                        else:
                            snakes1_turn_on_rainbow = False
                    if event.key == pygame.K_RCTRL:
                        if snakes2_turn_on_rainbow == False:
                            snakes2_turn_on_rainbow = True
                        else:
                            snakes2_turn_on_rainbow = False
                    #Pause game
                    if event.key == pygame.K_SPACE and game_state == 'Game':
                        if not check_pause:
                            check_pause = True
                        else:
                            check_pause = False
                    if not check_pause:    
                        #Huong di chuyen ran 1
                        if event.key == pygame.K_w:
                                snake1_check_direction = "foward"
                        if event.key == pygame.K_s:
                                snake1_check_direction = "backward"  
                        if event.key == pygame.K_a:
                                snake1_check_direction = "left"
                        if event.key == pygame.K_d:
                                snake1_check_direction ="right"
                        #Huong di chuyen ran 2
                        if event.key == pygame.K_UP:
                                snake2_check_direction = "foward"
                        if event.key == pygame.K_DOWN:
                                snake2_check_direction = "backward"  
                        if event.key == pygame.K_LEFT:
                                snake2_check_direction = "left"
                        if event.key == pygame.K_RIGHT:
                                snake2_check_direction ="right"
            #Check huong ran 1
            if snake1_direction != "backward" and snake1_check_direction == "foward":
                snake1_direction = "foward"
            if snake1_direction != "foward" and snake1_direction != "" and snake1_check_direction == "backward":
                snake1_direction = "backward"
            if snake1_direction != "right" and snake1_check_direction == "left":
                snake1_direction = "left"
            if snake1_direction != "left" and snake1_check_direction == "right":
                snake1_direction = "right"
            #Check huong ran 2
            if snake2_direction != "backward" and snake2_check_direction == "foward":
                snake2_direction = "foward"
            if snake2_direction != "foward" and snake2_direction != "" and snake2_check_direction == "backward":
                snake2_direction = "backward"
            if snake2_direction != "right" and snake2_check_direction == "left":
                snake2_direction = "left"
            if snake2_direction != "left" and snake2_check_direction == "right":
                snake2_direction = "right"


            if not check_pause:
                #Di chuyen ran 1
                if snake1_direction == "foward":
                    snakes.append([snakes[-1][0],snakes[-1][1] - 1])
                    if snake1_check_point == 0:
                        snakes.pop(0)
                if snake1_direction == "backward":
                    snakes.append([snakes[-1][0],snakes[-1][1] + 1])
                    if snake1_check_point == 0:
                        snakes.pop(0);  
                if snake1_direction == "left":
                    snakes.append([snakes[-1][0] - 1,snakes[-1][1]])
                    if snake1_check_point == 0:
                        snakes.pop(0);
                if snake1_direction == "right":
                    snakes.append([snakes[-1][0] + 1,snakes[-1][1]])
                    if snake1_check_point == 0:
                        snakes.pop(0);
                #Di chuyen ran 2
                if snake2_direction == "foward":
                    snakes2.append([snakes2[-1][0],snakes2[-1][1] - 1])
                    if snake2_check_point == 0:
                        snakes2.pop(0)
                if snake2_direction == "backward":
                    snakes2.append([snakes2[-1][0],snakes2[-1][1] + 1])
                    if snake2_check_point == 0:
                        snakes2.pop(0);  
                if snake2_direction == "left":
                    snakes2.append([snakes2[-1][0] - 1,snakes2[-1][1]])
                    if snake2_check_point == 0:
                        snakes2.pop(0);
                if snake2_direction == "right":
                    snakes2.append([snakes2[-1][0] + 1,snakes2[-1][1]])
                    if snake2_check_point == 0:
                        snakes2.pop(0);  

            pygame.display.update()
            clock.tick(snakes_speed)
