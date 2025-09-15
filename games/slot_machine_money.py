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
big_font = pygame.font.Font(None, 64)  # крупный для сообщения

# Кнопка - начать крутить барабан
# контейнер для кнопки
button = pygame.Rect(400, 150, 100, 60)
# меняем расположение кнопки
button.center = (3 * width // 4, height // 2)

color_button = (127, 0, 255)
color_text_button = (255, 255, 255)

# Подгружаем изображения для слот-машины
img_fld = 'imgs'
cherry = pygame.image.load(f"{img_fld}/cherry.png")
peach = pygame.image.load(f"{img_fld}/peach.png")
apple = pygame.image.load(f"{img_fld}/apple.png")
grape = pygame.image.load(f"{img_fld}/grape.png")

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

# счет игрока
score = 0
game_over = False


# снача

# ввод начального депозита
input_active = True
user_text = ""

# открыто ли окно с игрой
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if input_active:
            # экран ввода депозита
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if user_text.isdigit() and int(user_text) > 0:
                        score = int(user_text)
                        input_active = False
                    else:
                        user_text = ""  # сброс если ввели фигню
                elif event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                else:
                    if event.unicode.isdigit():  # только цифры
                        user_text += event.unicode
        else:
            if not game_over:
                # Проверяем клик мышью
                if event.type == pygame.MOUSEBUTTONDOWN:  # нажата кнопка мыши
                    if button.collidepoint(event.pos):   # event.pos = (x, y) клика
                        fruits = [
                            random.choice(list(fruit_images.keys())) for _ in range(3)
                        ]
                    
                    if fruits[0] == fruits[1] == fruits[2]:
                        score *= 2   # удвоение
                    else:
                        score -= 10  # проигрыш
                    
                    if score <= 0:
                        game_over = True
            
            else:
                # ждем нажатия R для рестарта
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        input_active = True
                        user_text = ""

                        fruits = []
                        game_over = False

    # задать цвет фона
    screen.fill((0, 0, 0))

    if input_active:
        # текст "Введите сумму"
        prompt_surface = font.render(
            "Введите депозит и нажмите Enter:", True, (255, 255, 255)
        )
        
        screen.blit(
            prompt_surface,
            (width//2 - prompt_surface.get_width()//2, height//2 - 50)
        )

        # поле ввода
        input_surface = big_font.render(
            user_text, True, (0, 255, 0)
        )
        screen.blit(
            input_surface,
            (width//2 - input_surface.get_width()//2, height//2)
        )

    else:
        if not game_over:

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

            score_surface = font.render(f"Score: {score}", True, (255, 255, 0))
            screen.blit(score_surface, (20, 20))
        
        else:
            game_over_surface = big_font.render("Ты проиграл!", True, (255, 0, 0))
            restart_surface = font.render("Нажми R чтобы начать заново", True, (255, 255, 255))

            screen.blit(
                game_over_surface,
                game_over_surface.get_rect(center=(width//2, height//2 - 30))
            )
            screen.blit(
                restart_surface,
                restart_surface.get_rect(center=(width//2, height//2 + 30))
            )

    pygame.display.flip()

# закрытие движка
pygame.quit()