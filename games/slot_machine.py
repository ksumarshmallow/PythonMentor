import pygame
import random

width, height = 600, 400

# инициализация движка
pygame.init()

# создаем окно с игрой
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Slot-machine')

# Задаем шрифты
font = pygame.font.Font(None, 36)  # None = стандартный шрифт, 36 = размер

# Кнопка - начать крутить барабан
# контейнер для кнопки
button = pygame.Rect(400, 150, 100, 60)
# меняем расположение кнопки
button.center = (3 * width // 4, height // 2)

color_button = (127, 0, 255)
color_text_button = (255, 255, 255)

# Подгружаем изображения для слот-машины
cherry = pygame.image.load("cherry.png")
peach = pygame.image.load("peach.png")
apple = pygame.image.load("apple.png")
grape = pygame.image.load("grape.png")

# задаем правильный размер
FRUIT_SIZE = (64, 64)
cherry = pygame.transform.smoothscale(cherry, FRUIT_SIZE)
peach = pygame.transform.smoothscale(peach, FRUIT_SIZE)
apple = pygame.transform.smoothscale(apple, FRUIT_SIZE)
grape = pygame.transform.smoothscale(grape, FRUIT_SIZE)

fruit_images = {
    "cherry": cherry,
    "peach": peach,
    "apple": apple,
    "grape": grape
}

# тут будут фрукты которые отрисовываем
fruits = []

# открыто ли окно с игрой
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Проверяем клик мышью
        if event.type == pygame.MOUSEBUTTONDOWN:  # нажата кнопка мыши
            if button.collidepoint(event.pos):   # event.pos = (x, y) клика
                fruits = [
                    random.choice(list(fruit_images.keys())) for _ in range(3)
                ]

    # задать цвет фона
    screen.fill((0, 0, 0))

    # пишем обновление
    # 1. рисуем кнопку
    pygame.draw.rect(screen, color_button, button)
    
    # 2. добавляем текст на кнопку
    text_surface = font.render("SPIN!", True, color_text_button)  # (текст, сглаживание, цвет)
    # получаем прямоугольник текста и центрируем его по кнопке
    text_rect = text_surface.get_rect(center=button.center)
    # рисуем текст поверх кнопки
    screen.blit(text_surface, text_rect)

    if fruits:
        start_x = width // 4  # начало ряда
        y = height // 2       # высота ряда
        spacing = 100         # расстояние между фруктами
    
    for i, fruit in enumerate(fruits):
        image = fruit_images[fruit]
        rect = image.get_rect(
            center=(start_x + i * spacing, y)
        )
        screen.blit(image, rect)


    pygame.display.flip()

# закрытие движка
pygame.quit()