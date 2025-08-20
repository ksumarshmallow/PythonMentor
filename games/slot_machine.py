import pygame
import random

# инициализация движка
pygame.init()

# ширину и длину окна
width, height = 800, 400

# создаем окно с игрой
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Slot')

# создаем "фонт" - шрифт которым будем все печатать (тип и размер)
font = pygame.font.SysFont("arial", 24)

# открыто ли окно с игрой
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == pygame.KEYDOWN:
            slots = [random.choice(['1', '2', '3']) for _ in range(3)]
            if len(set(slots)) == 1:
                message = "Ты выиграл!"
            else:
                message = "Попробуй еще раз"
    
            # цвет фона - черный
            screen.fill((0, 0, 0))

            # словарь соответствия номера символа -> позиции в окне
            idx_to_position = {0: 150, 1: 250, 2: 350}

            # отрисовка каждого символа
            for idx, symbol in enumerate(slots):
                # для каждого нужна позиция: на какой "высоте" и "ширине" его располагать
                x = idx_to_position[idx]
                y = 200

                # передаем то, что хотим отрисовать на наш фонт и цвет (тут он белый)
                text = font.render(symbol, True, (255, 255, 255))

                # создаем прямоугольник куда поместим символ
                rect = text.get_rect(center=(x, y))

                # blit(source, destination) - передаем в окно то, что хотим нарисовать (source)
                # и куда хотим нарисовать (rect)
                screen.blit(text, rect)
            
            # отображаем текст - победили или проиграли
            info = font.render(message, True, (200, 200, 200))
            # также передаем сообщение и то, на какую позицию хотим поместить текст
            screen.blit(info, (80, 330))

            # обновление картинки
            pygame.display.flip()

# задать цвет фона - черный после выхода из игры
screen.fill((0, 0, 0))

# закрытие движка
pygame.quit()