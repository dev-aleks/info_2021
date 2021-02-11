import pygame
#from pygame.draw import *

# Initialize library:
pygame.init()

# Set screen:
screen_width = 700
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
pygame.draw.circle(screen, RED, (350, 200), 100)

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