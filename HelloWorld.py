import pygame
import sys

pygame.init()

frames_per_second = 60

window_size = (800, 600)

screen = pygame.display.set_mode(window_size)

myriad_font = pygame.font.SysFont("Myriad Pro", 48)

hello_world = pygame.image.load("circle.png")
# hello_world = myriad_font.render("Hello World!", 1, (255, 0, 0), (0, 0, 0))
text_size = hello_world.get_size()
pygame.mouse.set_visible(0)

x, y = 0, 0

x_direction, y_direction = 1, 1
x_step, y_step = 5, 5

clock = pygame.time.Clock()

while True:

    clock.tick(frames_per_second)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    mouse_position = pygame.mouse.get_pos()
    x, y = mouse_position

    if x + text_size[0] > 800:
        x = 800 - text_size[0]

    if y + text_size[1] > 600:
        y = 600 - text_size[1]

    # bouce around
    # x += x_direction * x_step
    # y += y_direction * y_step
    #
    # if x + text_size[0] > 800 or x <= 0:
    # x_direction *= -1
    #
    # if y + text_size[1] > 600 or y <= 0:
    #     y_direction *= -1
    screen.fill((0, 0, 0))
    screen.blit(hello_world, (x, y))
    pygame.display.update()