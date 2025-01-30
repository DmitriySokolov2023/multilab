
import pygame
import sys
from random import randint

pygame.init()  


screen_width = 800 
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))  

pygame.display.set_caption("Двигающийся квадрат")

square_color = (255, 0, 0)
apple_color = (0, 255, 0)

square_sizeX = 50 
square_sizeY = 20 
square_x = screen_width / 2
square_y = screen_height-square_sizeY

square_speed = 5
apple_speed = 3

appleX = randint(0,screen_width-20)
appleY = 0

SCORE = 0
FONT = pygame.font.Font(None, 48)
def draw_text(text, color, x, y):
    text_surface = FONT.render(text, True, color)
    screen.blit(text_surface, (x, y))

def game_over():
    appleX = randint(0, screen_width-20)
    appleY = 0
    screen.fill((0, 0, 0))
    draw_text('Игра окончена',(255,0,0),screen_width*0.5-100, screen_height*0.5)
    draw_text('Нажмите SPACE для продолжения',(0,255,0),screen_width*0.5-100, screen_height*0.6)
    
    pygame.display.update()

    return appleX, appleY

    
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()    

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]: 
        square_x -= square_speed 
    if keys[pygame.K_RIGHT]:
        square_x += square_speed 
    appleY += apple_speed
    
    #ограничение игровой области
    if square_x < 0:
        square_x = 0
    elif square_x + square_sizeX > screen_width:
        square_x = screen_width - square_sizeX
    
    #ловля яблока
    if square_x < appleX and square_x + square_sizeX > appleX + 20 and square_y+5 < appleY:
        appleX = randint(0, screen_width-20)
        appleY = 0
        SCORE+=1
        square_speed+=0.5
        apple_speed+=0.5
        print(SCORE)

    elif appleY > screen_height+5:
        game_over()
        square_speed = 0
    else: 
        screen.fill((0, 0, 0))

        draw_text(f"Счет: {SCORE}", (255,255,255), 0, 0)

        pygame.draw.rect(screen, apple_color, (appleX, appleY, 20, 20))
        
        pygame.draw.rect(screen, square_color, (square_x, square_y, square_sizeX, square_sizeY))

        pygame.display.update()

    pygame.time.Clock().tick(60)
