import pygame
import random

pygame.init()

#### Константы ####
WIDTH, HEIGHT = 720, 420
FPS = 60

# Цвета
COLOR_BG = (30, 30, 30)
COLOR_BUTTON = (127, 0, 255)
COLOR_BUTTON_HOVER = (170, 50, 255)
COLOR_BUTTON_PRESSED = (100, 0, 200)
COLOR_TEXT = (255, 255, 255)
COLOR_SLOT = (160, 160, 160)

# Размеры
BUTTON_SIZE = (160, 70)
FRUIT_SIZE = (64, 64)
FRUITS_COUNT = 3
FRUITS_SPACING = 120
SLOT_SIZE = (80, 80)

#### Экран ####
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Slot-machine")
clock = pygame.time.Clock()

#### Шрифт ####
font = pygame.font.Font(None, 36)

#### Кнопка ####
button = pygame.Rect(0, 0, *BUTTON_SIZE)
button.center = (4 * WIDTH // 5, HEIGHT // 2)

#### Фрукты ####
fruit_files = ["cherry.png", "peach.png", "apple.png", "grape.png"]
fruit_images = {}

for file in fruit_files:
    img = pygame.image.load(f"imgs/{file}").convert_alpha()
    img = pygame.transform.smoothscale(img, FRUIT_SIZE)
    fruit_images[file.split(".")[0]] = img

fruits = []  # текущий результат

#### Функции ####
def draw_button(color_button):
    """Рисует кнопку с текстом"""
    pygame.draw.rect(screen, color_button, button, border_radius=15)    # border_radius - закругленные края
    text_surface = font.render("SPIN!", True, COLOR_TEXT)
    text_rect = text_surface.get_rect(center=button.center)
    screen.blit(text_surface, text_rect)

def draw_fruits():
    """Рисует фрукты на экране"""
    if not fruits:
        return

    start_x = WIDTH // 4
    y = HEIGHT // 2

    for i, fruit in enumerate(fruits):
        slot_rect = pygame.Rect(0, 0, *SLOT_SIZE)
        slot_rect.center = (start_x + i * FRUITS_SPACING, y)

        # Слот (рамка + фон)
        pygame.draw.rect(screen, COLOR_SLOT, slot_rect, border_radius=4, width=0)

        image = fruit_images[fruit]
        img_rect = image.get_rect(center=slot_rect.center)
        screen.blit(image, img_rect)

def spin():
    """Генерирует случайные фрукты"""
    return [random.choice(list(fruit_images.keys())) for _ in range(FRUITS_COUNT)]

#### Игровой цикл ####
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and button.collidepoint(event.pos):
            color_button = COLOR_BUTTON_PRESSED
            fruits = spin()
        elif event.type == pygame.MOUSEBUTTONUP and button.collidepoint(event.pos):
            color_button = COLOR_BUTTON_HOVER
        else:
            color_button = COLOR_BUTTON

    # рендер
    screen.fill(COLOR_BG)
    draw_button(color_button)
    draw_fruits()

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
