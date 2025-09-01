
import pygame
import random

# инициализация движка
pygame.init()

# ширину и длину окна
WIDTH, HEIGHT = 680, 420
BUTTON_COLOR = (255, 0, 0)
FRUIT_WIDTH, FRUIT_HEIGHT = 50, 50

# создаем окно с игрой
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Slot machine')

# кнопка "крутить"
# (левый верхний угол по OX, левый врехний угол по OY, Ширина, Высота)
button_rect = pygame.Rect(400, HEIGHT//2, 200, 100) 

# подгружаем изображения
cherry = pygame.image.load("imgs/cherry.png")
apple = pygame.image.load("imgs/apple.png")
grape = pygame.image.load("imgs/grape.png")
peach = pygame.image.load("imgs/peach.png")

fruits = [cherry, apple, grape, peach]
# пройдемся по списку, у каждого объекта изменим размер и перезапишем его в списке
for idx, fruit in enumerate(fruits):
    fruit = pygame.transform.scale(fruit, (FRUIT_WIDTH, FRUIT_HEIGHT))
    # перехаписываем изначальный объект
    fruits[idx] = fruit

def sample_fruits():
    a = []
    for _ in range(3):
        a.append(random.choice(fruits))
    return a

# открыто ли окно с игрой
sampled_fruits = []
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN and button_rect.collidepoint(event.pos):
            sampled_fruits = sample_fruits() # список из изображений фруктов

    # убираем прошлую картинку (делаем заливку экрана черным)
    screen.fill((0, 0, 0))

    # как-то обновляем элементы
    pygame.draw.circle(
        screen,
        BUTTON_COLOR,
        center=button_rect.center,
        radius=50
    )

    # если нажали на кнопку
    if len(sampled_fruits) > 0:
        for idx, fruit in enumerate(sampled_fruits):
            screen.blit(fruit, (100 * (idx + 1), HEIGHT//2))

    # обновляем screen
    pygame.display.flip()

# закрытие движка
pygame.quit()