import pygame
import sys
from random import randint

pygame.init()

#Параметры экрана
WIDTH = 425
HEIGHT = 600


#Переменные цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_GRAY = (224, 224, 224)

# Размеры кнопок
BUTTON_WIDTH, BUTTON_HEIGHT = 80, 60
BUTTON_MARGIN = 10

# Шрифты
FONT = pygame.font.Font(None, 48)

def draw_text(text, color, x, y):
    text_surface = FONT.render(text, True, color)
    screen.blit(text_surface, (x, y))

buttons = [
{'label': '1', 'pos': (10, 340)}, 
{'label': '2', 'pos': (100, 340)}, 
{'label': '3', 'pos': (190, 340)},
{'label': '4', 'pos': (10, 270)}, 
{'label': '5', 'pos': (100, 270)},
{'label': '6', 'pos': (190, 270)}, 
{'label': '7', 'pos': (10, 200)}, 
{'label': '8', 'pos': (100, 200)}, 
{'label': '9', 'pos': (190, 200)}, 
{'label': '0', 'pos': (100, 410)}, 

{'label': '/', 'pos': (280, 200)},
{'label': '*', 'pos': (280, 270)}, 
{'label': '-', 'pos': (280, 340)},
{'label': '=', 'pos': (190, 410)}, 
{'label': '+', 'pos': (280, 410)},
{'label': 'C', 'pos': (10, 410)}, 
]


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Calculator")

while True:
	screen.fill(LIGHT_GRAY)
	for button in buttons:
		x, y = button['pos']
		pygame.draw.rect(screen, WHITE,(x, y, BUTTON_WIDTH, BUTTON_HEIGHT))
		draw_text(button['label'],BLACK, x + 30, y + 10)

	pygame.display.flip()

	for event in pygame.event.get():

		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				pygame.quit()
				sys.exit()

	

		




























# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# GRAY = (200, 200, 200)
# LIGHT_GRAY = (240, 240, 240)

# screen = pygame.display.set_mode((800, 600))
# pygame.display.set_caption("Calculator")



# x = 0
# y = 0
# x1 = 20
# y1 = 20
# clock = pygame.time.Clock()

# while True:
# 	screen.fill(BLACK)
# 	snake_pos = [100, 50] 
# 	pygame.draw.rect(screen, LIGHT_GRAY, (20, 20, 50, 50))
# 	for event in pygame.event.get():
# 		if event.type == pygame.QUIT:
# 			pygame.quit()
# 			sys.exit()
# 		if event.type == pygame.KEYDOWN:
# 			if event.key == pygame.K_ESCAPE:
# 				pygame.quit()
# 				sys.exit()

# 	keys = pygame.key.get_pressed()
	
# 	if keys[pygame.K_RIGHT]:
# 		x +=10
# 	if keys[pygame.K_LEFT]:
# 		x -=10
# 	if keys[pygame.K_UP]:
# 		y -=10
# 	if keys[pygame.K_DOWN]:
# 		y +=10
# 	if x == 20:
# 		x1 +=10
# 		y1 +=10
	
# 	pygame.draw.rect(screen, LIGHT_GRAY, (x, y, x1, y1))
# 	print(x, y)
# 	pygame.time.delay(10)
# 	pygame.display.flip()

		
		
			

	

