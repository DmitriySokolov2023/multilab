import pygame
import random
import sys

# Инициализация Pygame
pygame.init()

# Размеры окна
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20

# Цвета
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Змейка")

# Часы для управления FPS
clock = pygame.time.Clock()

# Скорость змейки
snake_speed = 5

# Функция для отображения текста
def draw_text(text, size, color, x, y):
    font = pygame.font.Font(None, size)
    surface = font.render(text, True, color)
    screen.blit(surface, (x, y))

# Основная игра
def game():
    # Параметры змейки
    snake_pos = [100, 50]  # Начальная позиция головы змейки
    snake_body = [[100, 50], [90, 50], [80, 50]]  # Тело змейки
    direction = "RIGHT"  # Начальное направление
    change_to = direction

    # Еда
    food_pos = [random.randrange(1, (WIDTH // CELL_SIZE)) * CELL_SIZE,
                random.randrange(1, (HEIGHT // CELL_SIZE)) * CELL_SIZE]
    food_spawn = True

    score = 0

    while True:
        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != "DOWN":
                    change_to = "UP"
                elif event.key == pygame.K_DOWN and direction != "UP":
                    change_to = "DOWN"
                elif event.key == pygame.K_LEFT and direction != "RIGHT":
                    change_to = "LEFT"
                elif event.key == pygame.K_RIGHT and direction != "LEFT":
                    change_to = "RIGHT"
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        # Направление движения
        direction = change_to
        if direction == "UP":
            snake_pos[1] -= CELL_SIZE
        if direction == "DOWN":
            snake_pos[1] += CELL_SIZE
        if direction == "LEFT":
            snake_pos[0] -= CELL_SIZE
        if direction == "RIGHT":
            snake_pos[0] += CELL_SIZE

        # Рост змейки
        snake_body.insert(0, list(snake_pos))
        if snake_pos == [food_pos[1]+10, food_pos[0]+10]:
            print(snake_pos)
            score += 1
            food_spawn = False
        else:
            snake_body.pop()

        if not food_spawn:
            food_pos = [random.randrange(1, (WIDTH // CELL_SIZE)) * CELL_SIZE,
                        random.randrange(1, (HEIGHT // CELL_SIZE)) * CELL_SIZE]
        food_spawn = True

        # Окончание игры при столкновении
        if (snake_pos[0] < 0 or snake_pos[0] >= WIDTH or
                snake_pos[1] < 0 or snake_pos[1] >= HEIGHT):
            break

        for block in snake_body[1:]:
            if snake_pos == block:
                break

        # Отрисовка
        screen.fill(BLACK)

        for block in snake_body:
            pygame.draw.rect(screen, GREEN, pygame.Rect(block[0], block[1], CELL_SIZE, CELL_SIZE))

        pygame.draw.rect(screen, RED, pygame.Rect(food_pos[0], food_pos[1], CELL_SIZE, CELL_SIZE))

        draw_text(f"Счёт: {score}", 25, WHITE, 10, 10)

        pygame.display.flip()

        # Задержка
        clock.tick(snake_speed + score)  # Скорость увеличивается с увеличением счёта

    return score

# Главный цикл
def main():
    while True:
        screen.fill(BLACK)
        draw_text("Нажмите пробел для старта", 36, WHITE, WIDTH // 4, HEIGHT // 3)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    score = game()
                    draw_text(f"Игра окончена! Ваш счёт: {score}", 36, WHITE, WIDTH // 6, HEIGHT // 2)
                    pygame.display.flip()
                    pygame.time.wait(3000)

                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

if __name__ == "__main__":
    main()