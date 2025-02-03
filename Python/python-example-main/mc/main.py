import pygame
import sys
from random import randint

pygame.init()
pygame.mixer.init()

screen_width = 1000 
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))

fon = pygame.image.load("stars-fon.jpg")
ship_img = pygame.image.load("ship.png")
fon_img = pygame.transform.scale(fon, (screen_width, screen_height))
meteor_img = pygame.image.load("meteor.png")
bom_img = pygame.image.load("bom.png")




pygame.mixer.music.load("battle.mp3")
pygame.mixer.music.play(-1)
explosion_sound = pygame.mixer.Sound("bom.wav")

shipX=screen_width/2-57.5
shipY=screen_height - 200  

meteorX = randint(int(shipX-200), int(shipX+200))
meteorY = 0
meteor_speed = 0.2





FONT = pygame.font.Font(None, 48)
def draw_text(text, color, x, y):
    text_surface = FONT.render(text, True, color)
    screen.blit(text_surface, (x, y))
SCORE = 0

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
        shipX -= 2 
    if keys[pygame.K_RIGHT]:
        shipX += 2 
    

    if shipX < 0:
        shipX = 0
    if shipX > screen_width-116:
        shipX = screen_width-116

    meteorY +=meteor_speed
    screen.blit(fon_img, (0,0))
    screen.blit(meteor_img, (meteorX,meteorY))
    screen.blit(ship_img, (shipX,shipY))
    draw_text(f"Счёт: {SCORE}",(255,255,255),50,50)

    if shipX < meteorX and shipX+115 > meteorX + 35 and shipY < meteorY:
        screen.blit(fon_img, (0,0))
        screen.blit(bom_img, (shipX,shipY))
        draw_text(f"Счёт: {SCORE}",(255,255,255),50,50)
        explosion_sound.play()
        pygame.display.update()
        pygame.time.delay(5000)
        meteor_speed = 0.2
        meteorY = 0
        SCORE = 0
        
        

    if(meteorY > screen_height):
        meteor_speed +=0.1
        meteorX = randint(int(shipX-150), int(shipX+150))
        meteorY = 0
        SCORE +=1

    
    pygame.display.flip()
    