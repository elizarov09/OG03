import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Игра Тир")
icon = pygame.image.load("img/tir_icon.png")
pygame.display.set_icon(icon)

target = pygame.image.load("img/target.png")
target_width = 118
target_height = 118

target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

# Скорость движения таргета по осям x и y
speed_x = random.randint(-5, 5)
speed_y = random.randint(-5, 5)

# Функция для генерации нового цвета
def generate_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

color = generate_color()

running = True
clock = pygame.time.Clock()

# ...

while running:
    screen.fill(color)  # Заливка экрана текущим цветом

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            # Проверяем, попал ли клик в область таргета
            if (target_x <= mouse_x <= target_x + target_width) and (target_y <= mouse_y <= target_y + target_height):
                # "Падение" таргета
                while target_y < SCREEN_HEIGHT:
                    target_y += 1  # Перемещаем таргет вниз
                    screen.fill(color)
                    screen.blit(target, (target_x, target_y))
                    pygame.display.update()
                    clock.tick(300)  # Ускоренное "падение"

                # Сброс таргета на новую случайную позицию после "падения"
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
                # Случайная скорость для нового таргета
                speed_x = random.randint(-5, 5)
                speed_y = random.randint(-5, 5)
                color = generate_color()  # Новый случайный цвет фона

    # Движение таргета
    target_x += speed_x
    target_y += speed_y

    # Отражение таргета от краев экрана
    if target_x <= 0 or target_x >= SCREEN_WIDTH - target_width:
        speed_x *= -1
    if target_y <= 0 or target_y >= SCREEN_HEIGHT - target_height:
        speed_y *= -1

    screen.blit(target, (target_x, target_y))  # Отображаем таргет на экране
    pygame.display.update()  # Обновляем экран
    clock.tick(60)  # Частота обновления кадров

pygame.quit()

