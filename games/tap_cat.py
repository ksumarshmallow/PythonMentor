import pygame

pygame.init()

#### Константы ####
WIDTH, HEIGHT = 640, 480
HEIGHT_CAT = 300
FPS = 60

# Цвета
COLOR_BG = (30, 30, 30)        # темно-серый фон
COLOR_TEXT = (255, 255, 255)   # белый текст

#### Главный экран ####
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cat tap game")
clock = pygame.time.Clock()

#### Загружаем изображение кота ####
cat = pygame.image.load("imgs/cat.jpg").convert_alpha()

# ресайзим с сохранением пропорций
cat_width, cat_height = cat.get_size()
aspect_ratio = cat_width / cat_height
WIDTH_CAT = int(HEIGHT_CAT * aspect_ratio)
cat = pygame.transform.scale(cat, (WIDTH_CAT, HEIGHT_CAT))

# Контейнер кота
rect_cat = cat.get_rect(center=(WIDTH//2, HEIGHT//2))   # рисуем посередине

#### Текст ####
font = pygame.font.SysFont("Arial", 24, bold=True)
num_taps = 0

#### Игровой цикл ####
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and rect_cat.collidepoint(event.pos):
            num_taps += 1

    # очистка экрана
    screen.fill(COLOR_BG)

    # обновляем позицию кота
    rect_cat = cat.get_rect(center=(WIDTH//2, HEIGHT//2))   # рисуем посередине

    # рисуем кота
    screen.blit(cat, rect_cat)

    # рисуем текст
    text_surface = font.render(f"Taps: {num_taps}", True, COLOR_TEXT)
    text_rect = text_surface.get_rect(topleft=(10, 10))
    screen.blit(text_surface, text_rect)

    # обновляем экран
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
