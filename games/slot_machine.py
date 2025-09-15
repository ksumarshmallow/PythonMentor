
import pygame
import random

# инициализация движка
pygame.init()

# ширину и длину окна
WIDTH, HEIGHT = 680, 420
BUTTON_COLOR = (255, 0, 0)
FRUIT_WIDTH, FRUIT_HEIGHT = 50, 50
TEXT_COLOR = (255, 255, 255) 

# создаем окно с игрой
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Slot machine')

# Шрифт
font = pygame.font.SysFont("Arial", 24, bold=True)

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
    # перезаписываем изначальный объект
    fruits[idx] = fruit

def sample_fruits():
    a = []
    for _ in range(3):
        a.append(random.choice(fruits))
    return a

# открыто ли окно с игрой
sampled_fruits = []
running = True
score = 0

# задать переменную user_text, которая будет содержать депозит
# изначально она пустая
# но когда мы входоим в цикл игры, мы "спрашиваем пользователя его стартовый депозит
# событие написания: pygame.KEYDOWN, и считаем что он завершил писать, когда нажал Enter (K_RETURN)

# депозит
user_text = ''     # заместо score будет преобразованный user_text
input_active = True

# input_active - будет True, когда пользователь еще имеет возможность что-то ввести
# и в самом начале игры он как раз True

# как только он нажал на Enter -> мы сттавим input_active = False
# и тогда уже начинаем игру

# человек набрал score <0
game_over = False
# в этот момент нам нужно перестать показывать картинку игры
# и нарисовать окно, где спрашиваем, хотим ли продолжит

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # 1 часть: когда только спрашиваем депозит
        if score >= 0: 
            if input_active:
                if event.type == pygame.KEYDOWN:
                    # event.unicode - возвращает ввод с клавиатуры (строка)
                    # проверить является ли строка числом можно через .isdigit()
                    if event.unicode.isdigit():
                        user_text += event.unicode
   
                    # завершаем ввод клавишей ENTER (K_RETURN)
                    if event.key == pygame.K_RETURN:
                        score = int(user_text)
                        input_active = False
            else:
                # 2 часть: УЖЕ ЗНАЕМ что пользователь все ввел
                # поэтому можем начинать игру
                if event.type == pygame.MOUSEBUTTONDOWN and button_rect.collidepoint(event.pos):
                    sampled_fruits = sample_fruits() # список из изображений фруктов
                    
                    # условие победы
                    if sampled_fruits[0] == sampled_fruits[1] == sampled_fruits[2]:
                        score *= 2
                    else:
                        score -= 10
        
        else:
            # случшать событие нажатия на клавишу R (~restart)
            running = False

    # убираем прошлую картинку (делаем заливку экрана черным)
    screen.fill((0, 0, 0))

    # если game_over -> мы рисуем окно, где спрашиваем, хочем ли человек продолжить
    # и если хочет, то пусть нажмет R

    # Если человек уже что-то ввел - орисовываем фрукты
    if not input_active:
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
        
        text_surface = font.render(f"Score: {score}", True, TEXT_COLOR)
        screen.blit(text_surface, (10, 10))

    # то что будем рисовать, когда спрашиваем пользователя о его депозите
    if input_active:
        # спросить о его сумме депозита
        # сделать окно с вопросом о депозите
        text = font.render("Укажите депозит и нажмите Enter:", True, TEXT_COLOR)
        screen.blit(text, (WIDTH // 4, HEIGHT // 2))

        # также нужно окно где отображается депозит пользователя
        # нужно отображать `user_text`
        text2 = font.render(user_text, True, TEXT_COLOR)
        screen.blit(text2, ((WIDTH // 3, 3 * HEIGHT // 4)))

    # обновляем screen
    pygame.display.flip()

# закрытие движка
pygame.quit()