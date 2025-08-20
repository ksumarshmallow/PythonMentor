import pygame

# инициализация движка
pygame.init()

# ширину и длину окна
width, height = 1200, 800

# создаем окно с игрой
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('My Game')

# открыто ли окно с игрой
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# задать цвет фона - черный после выхода из игры
screen.fill((0, 0, 0))

# закрытие движка
pygame.quit()