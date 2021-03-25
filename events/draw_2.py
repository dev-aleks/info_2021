import pygame
from random import randint

# initial the game:
pygame.init()
pygame.font.init()

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

# common variable
count = 0  # for calculate count (score)
count_ball = 0  # for calculate - how many i get new_ball()


def new_ball():
    """
    Функция для рисования нового шарика. 
    Размеры рандомные и автоматические.
    Координаты рисования автоматические
    """
    global x, y, r
    x = randint(100, screen_width)
    y = randint(100, screen_height)
    r = randint(10, 100)
    color = COLORS[randint(0, 5)]
    pygame.draw.circle(screen, color, (x, y), r)


def click(event):
    """
    Функция для получения координат круга
    """
    return x, y, r


def calculate_and_compare(x1, y1, x2, y2):
    """
    Функция для подсчета расстояния между двумя точками
    :param x1: координата x круга
    :param y1: координата y круга
    :param R1: значение радиуса круга
    :param x2: координата x нажатия
    :param y2: координата y нажатия
    :return: результат, попал ли в круг
    """
    length_between_point = (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** (0.5)  # length between point
    return length_between_point


def draw_text(text, size, x, y):
    """
    Функция для отрисовки динамичного текста

    :param text: текст для отображения
    :param size: размер шрифта
    :param x, y: привязка от левого верхнего угла для размещения текста
    """
    my_font = pygame.font.Font(None, size)
    my_text = my_font.render(text, True, WHITE, None)
    screen.blit(my_text, (x, y))  # blit для отображения текста в координатах


# loop until the user clicks the close button:
done = False
clock = pygame.time.Clock()
max_FPS = 0.8

while not done:
    # this limits the while loop to a max of 10 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(max_FPS)
    # exit cycle:
    for event in pygame.event.get():  # user did something
        if event.type == pygame.QUIT:  # if user clicked close
            done = True  # change flag; exit from loop
            print(count, ' / ', count_ball)  # show result

        # if event is mouse "button down":
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click(event)  # show option BALL from new_ball()
            event.pos  # calculate position my mouse
            length = calculate_and_compare(x, y, event.pos[0], event.pos[1])  # calculate length between two point
            # give count:
            if length <= r:
                count += 1

    # drawing...
    # set screen background:
    screen.fill(BLACK)
    # drawing ball:
    new_ball()
    count_ball += 1
    # visual score:
    draw_text(str(count), 30, 10, 10)

    # after all drawing commans update screen:
    pygame.display.update()

# be IDLE friendly
pygame.font.quit()
pygame.quit()
