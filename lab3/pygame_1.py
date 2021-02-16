import pygame
#from pygame.draw import *

# Initialize library:
pygame.init()

# Set screen:
screen_width = 400
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])

# Переменные с цветами:
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# drawing...
screen.fill(BLACK)
x1 = 100
y1 = 100
dx = 200
dy = 200
# для rect параметра, от левого верхнего угла: [влево, вниз, длина по X, длина по Y]:
pygame.draw.rect(screen, WHITE, [x1, y1, dx, dy], 1)
# рисуем штриховку:
h = 10
N = dx // h
x = x1 + h
for i in range(N):
    pygame.draw.line(screen, WHITE, [x, y1], [x, y1 + dy], 1)
    x += h

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