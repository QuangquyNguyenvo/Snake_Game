import pygame
import sys
pygame.init()
screen_size = 600
screen = pygame.display.set_mode((screen_size+2, screen_size+2))
pygame.display.set_caption('PY')
WHITE = (255, 255, 255)
GREEN = (0, 225, 0)
GREEN2 = (0, 250,0)
BLACK = (0, 0, 0)
clock = pygame.time.Clock()
run = True
block= 30
#toa do ran
snakes = [[0,0],[1,0],[2,0]]
direction = 'side'
#game
while run:
    clock.tick(60)
    screen.fill(BLACK)
    #draw
    for i in range((600//block)+1):
        #grid
        pygame.draw.line(screen, WHITE, (0,i*block), (screen_size,i*block))
        pygame.draw.line(screen, WHITE, (i*block, 0), (i*block,screen_size))
        #snake_position
        tmp = 0
        for snake in snakes:
            pygame.draw.rect(screen, GREEN, (snake[0]*block, snake[1]*block, 30, 30))
        pygame.draw.rect(screen, GREEN2, (snake[0]*block, snake[1]*block, 30, 30))
        for snake in snakes:
            if tmp == len(snakes)-1:
                if direction == 'side':
                    pygame.draw.circle(screen, BLACK, (snake[0] * block + 10, snake[1] * block + 10), 2.75)
                    pygame.draw.circle(screen, BLACK, (snake[0] * block + 10, snake[1] * block + 20), 2.75)
                if direction == 'up':
                    pygame.draw.circle(screen, BLACK, (snake[0] * block + 10, snake[1] * block + 10), 2.75)
                    pygame.draw.circle(screen, BLACK, (snake[0] * block + 20, snake[1] * block + 10), 2.75)
            tmp += 1
       
    pygame.display.update()
    #exit game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    direction = 'side'
                #if snake[0]-1>=0:
                    snakes.append([snakes[-1][0]-1, snakes[-1][1]])
                    snakes.pop(0)
                #draw eye
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    direction = 'side'
                #if snake[0]+1<(screen_size//block): 
                    snakes.append([snakes[-1][0]+1, snakes[-1][1]])
                    snakes.pop(0)
                #draw eye
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                    direction = 'up'
                #if snake[1]-1>=0: 
                    snakes.append([snakes[-1][0], snakes[-1][1]-1])
                    snakes.pop(0)
                #draw eye
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    direction = 'up'
                #if snake[1]+1<(screen_size//block):sss 
                    snakes.append([snakes[-1][0], snakes[-1][1]+1])
                    snakes.pop(0)
                #draw eye
    
pygame.quit()
quit()
