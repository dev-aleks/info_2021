import pygame
#from pygame.draw import *

# Initialize library:
pygame.init()

# Set screen:
screen_width = 400
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])

# Переменные с цветами:
BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
RED = [255, 0, 0]
GREEN = [0, 255, 0]
BLUE = [0, 0, 255]
YELLOW = [255, 255, 0]
BACKGROUND = [128, 128, 128]

# Переменная для координат:
SET_FACE = [200, 200]
SET_LEFT_EYE = [125, 150]
SET_RIGHT_EYE = [275, 150]

# drawing...
# добавляем фон:
screen.fill(BACKGROUND)
# draw the face:
pygame.draw.circle(screen, BLACK, SET_FACE, 153)
pygame.draw.circle(screen, YELLOW, SET_FACE, 150)
# draw the left eye:
pygame.draw.circle(screen, BLACK, SET_LEFT_EYE, 30)
pygame.draw.circle(screen, RED, SET_LEFT_EYE, 28)
pygame.draw.circle(screen, BLACK, SET_LEFT_EYE, 10)
# draw the right eye:
pygame.draw.circle(screen, BLACK, SET_RIGHT_EYE, 25)
pygame.draw.circle(screen, RED, SET_RIGHT_EYE, 23)
pygame.draw.circle(screen, BLACK, SET_RIGHT_EYE, 10)
# draw the mouth:
pygame.draw.rect(screen, BLACK, [100, 250, 200, 30])
# draw angry BROVS:
pygame.draw.line(screen, BLACK, [75, 75], [175, 140], 15)
pygame.draw.line(screen, BLACK, [225, 140], [350, 75], 15)

# Обновить экран для отображения
pygame.display.update()

# Create an object to help track time (объект для отслеживания времени)
clock = pygame.time.Clock()
max_FPS = 30

# Loop
while True:
    clock.tick(max_FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

# Be IDLE friendly
pygame.quit()