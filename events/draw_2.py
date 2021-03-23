import pygame
from random import randint

# initial the game:
pygame.init()

# set screen:
screen_width = 1000
screen_height = 800
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
    global x, y, r
    x = randint(100, screen_width)
    y = randint(100, screen_height)
    r = randint(10, 100)
    color = COLORS[randint(0,5)]
    pygame.draw.circle(screen, color, (x, y), r)

def click(event):
    '''
    Функция для получения координат круга
    '''
    return x, y, r

def calculate_and_compare(x1, y1, R1, x2, y2):
    '''
    Функция для подсчета и сравнения расстояния между двумя точками
    :param x1: координата x круга
    :param y1: координата y круга
    :param R1: значение радиуса круга
    :param x2: координата x нажатия
    :param y2: координата y нажатия
    :return: результат, попал ли в круг
    '''
    R2 = (((x2-x1)**2) + ((y2-y1)**2))**(0.5) # length between point
    if R2 <= R1:
        print('good')
    else:
        print ('no good')

# loop until the user clicks the close button:
done = False
clock = pygame.time.Clock()
max_FPS = 0.8

while not done:
    # this limits the while loop to a max of 10 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(max_FPS)
    # exit cycle:
    for event in pygame.event.get():    # user did something
        if event.type == pygame.QUIT:   # if user clicked close
            done = True                 # change flag; exit from loop

        #   что должно происходить при нажатии кнопки?
        #   1) необходимо вычислить координаты круга и его радиус, зафиксировав эти значения
        #   2) необходимо вычислить позицию нажатия мыши
        #   3) вычислить расстояние между двумя точками - результат добавляет очко, если оно меньше или равно радиусу круга
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click(event)
            event.pos
            calculate_and_compare(x, y, r, event.pos[0], event.pos[1])

    # drawing...
    # set screen background:
    screen.fill(BLACK)
    # drawing ball:
    new_ball()

    # after all drawing commans update screen:
    pygame.display.update()

# be IDLE friendly
pygame.quit()