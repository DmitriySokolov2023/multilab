import pygame
import sys

# Инициализация Pygame
pygame.init()

# Настройки окна
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Calculator")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
LIGHT_GRAY = (240, 240, 240)

# Шрифты
FONT = pygame.font.Font(None, 48)

# Параметры кнопок
BUTTON_WIDTH, BUTTON_HEIGHT = 80, 60
BUTTON_MARGIN = 10

def draw_text(text, color, x, y):
    text_surface = FONT.render(text, True, color)
    screen.blit(text_surface, (x, y))

# Расположение кнопок
buttons = [
{'label': '1', 'pos': (10, 340),},
{'label': '2', 'pos': (100, 340),}, 
{'label': '3', 'pos': (190, 340),},
{'label': '4', 'pos': (10, 270),}, 
{'label': '5', 'pos': (100, 270),},
{'label': '6', 'pos': (190, 270),}, 
{'label': '7', 'pos': (10, 200),}, 
{'label': '8', 'pos': (100, 200),}, 
{'label': '9', 'pos': (190, 200),}, 
{'label': '0', 'pos': (100, 410),}, 
{'label': '/', 'pos': (280, 200),},
{'label': '*', 'pos': (280, 270),}, 
{'label': '-', 'pos': (280, 340),},
{'label': '=', 'pos': (190, 410),}, 
{'label': '+', 'pos': (280, 410),},
{'label': 'C', 'pos': (10, 410),}, 
]

def main():
    input_text = ""
    result = ""

    # Отрисовка кнопок
    for button in buttons:
        x, y = button['pos']
        pygame.draw.rect(screen, BLACK, (x, y, BUTTON_WIDTH, BUTTON_HEIGHT))
        draw_text(button['label'], BLACK, x + 30, y + 10)


    while True:
        screen.fill(WHITE)

        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = event.pos
                for button in buttons:
                    x, y = button['pos']
                    if x <= mouse_pos[0] <= x + BUTTON_WIDTH and y <= mouse_pos[1] <= y + BUTTON_HEIGHT:
                        label = button['label']
                        if label == 'C':
                            input_text = ""
                            result = ""
                        elif label == '=':
                            try:
                                result = str(eval(input_text))
                            except Exception:
                                result = "Error"
                        else:
                            input_text += label

        pygame.draw.rect(screen, LIGHT_GRAY, (10, 50, WIDTH - 20, 100))
        draw_text(input_text, BLACK, 20, 70)

        # Поле результата
        pygame.draw.rect(screen, GRAY, (10, 150, WIDTH - 20, 40))
        draw_text(result, BLACK, 20, 155)
        pygame.display.flip()
        


main()
