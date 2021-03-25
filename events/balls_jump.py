import pygame
import random

# initial the game:
pygame.init()

# set screen:
screen_width = 800
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

# loop until the user clicks the close button:
done = False
clock = pygame.time.Clock()
max_FPS = 120

radius_circle = 25
# variables for random born balls:
ball_x = random.randint(0+radius_circle, screen_width-radius_circle)
ball_y = random.randint(0+radius_circle, screen_height-radius_circle)
screen_width_begin = 0
screen_height_begin = 0
# variables for random go:
random_vector_x = random.choice([-1, 1])
random_vector_y = random.choice([-1, 1])


while not done:
    # this limits the while loop to a max of XXX times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(max_FPS)
    # exit cycle:
    for event in pygame.event.get():  # user did something
        if event.type == pygame.QUIT:  # if user clicked close
            done = True  # change flag; exit from loop

    # drawing...
    # set screen background:
    screen.fill(BLACK)
    # draw circle:
    pygame.draw.circle(screen, WHITE, (ball_x, ball_y), radius_circle)
    # after all drawing commands update screen:
    pygame.display.update()
    # ball going random:
    ball_x = ball_x + 1 * random_vector_x
    ball_y = ball_y + 1 * random_vector_y
    # condition for walls:
    if ball_x - radius_circle == screen_width_begin or ball_x + radius_circle == screen_width:
        random_vector_x = -random_vector_x
    if ball_y - radius_circle == screen_height_begin or ball_y + radius_circle == screen_height:
        random_vector_y = -random_vector_y



# be IDLE friendly
pygame.quit()
