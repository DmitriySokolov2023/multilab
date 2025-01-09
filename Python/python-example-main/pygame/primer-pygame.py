import pygame

# Инициализация pygame
pygame.init()

# Создаем окно
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pygame Example")

# Устанавливаем шрифт
font = pygame.font.Font(None, 36)

# Основной цикл игры
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Заполнение экрана цветом
    screen.fill((255, 255, 255))

    # Рисуем текст
    text_surface = font.render("Hello, Pygame!", True, (0, 0, 0))
    screen.blit(text_surface, (200, 250))

    # Обновляем экран
    pygame.display.update()

# Закрываем pygame
pygame.quit()