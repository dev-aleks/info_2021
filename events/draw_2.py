import pygame
from random import randint

# initial the game:
pygame.init()

# set screen:
screen_width = 1200
screen_height = 900
screen = pygame.display.set_mode([screen_width, screen_height])

# variable color:
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

def new_ball():
    '''
    Функция для рисования нового шарика. 
    Размеры рандомные и автоматические.
    Координаты рисования автоматические
    '''
    x = randint(100, 1100)
    y = randint(100, 900)
    r = randint(10, 100)
    color = COLORS[randint(0,5)]
    pygame.draw.circle(screen, color, (x, y), r)

# loop until the user clicks the close button:
done = False
clock = pygame.time.Clock()
max_FPS = 2

while not done:
    # this limits the while loop to a max of 10 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(max_FPS)
    # exit cycle:
    for event in pygame.event.get():    # user did something
        if event.type == pygame.QUIT:   # if user clicked close
            done = True                 # change flag; exit from loop

    # drawing...
    # set dcreen background:
    screen.fill(BLACK)
    # drawing ball:
    new_ball()

    # after all drawing commans update screen:
    pygame.display.update()

# be IDLE friendly
pygame.quit()