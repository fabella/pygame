import pygame, sys

pygame.init()

window_size = (800, 600)

screen = pygame.display.set_mode(window_size)

myriad_font = pygame.font.SysFont("Myriad Pro", 48)

hello_world = myriad_font.render("Hello World!", 1, (255, 0, 0), (0, 0, 0))

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.blit(hello_world, (0, 0))

    pygame.display.update()