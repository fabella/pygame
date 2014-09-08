import pygame
import time
import random

pygame.init()

# display dimension
display_width = 800
display_height = 600

# Color definitions
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('A bit Race')
clock = pygame.time.Clock()

carImg = pygame.image.load('img/racecar.png')
car_width = 57

def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(game_display, color, [thingx, thingy, thingw, thingh])

def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: " + str(count), True, black)
    game_display.blit(text, (0, 0))

def car(location):
    game_display.blit(carImg, location)

def text_objects(text, font):
    text_surface = font.render(text, True, red)
    return text_surface, text_surface.get_rect()

def message_display(text):
    large_text = pygame.font.Font('freesansbold.ttf', 115)
    text_surf, text_rect = text_objects(text, large_text)
    text_rect.center = ((display_width / 2), (display_height / 2))
    game_display.blit(text_surf, text_rect)
    pygame.display.update()
    time.sleep(2)
    game_loop()

def crash():
    message_display('You Crashed')

def game_loop():
    game_exit = False
    x = (display_width * 0.45)
    y = (display_height * 0.8)
    x_change = 0
    car_speed = 5
    dodged = 0

    thing_starty = -600
    thing_speed = 3
    thing_widh = 100
    thing_height = 100
    thing_startx = random.randrange(0, display_width - thing_widh)

    while not game_exit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -car_speed
                elif event.key == pygame.K_RIGHT:
                    x_change = car_speed
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
        x += x_change
        game_display.fill(white)

        things(thing_startx, thing_starty, thing_widh, thing_height, green)
        thing_starty += thing_speed
        car((x, y))
        things_dodged(dodged)

        if x > display_width - car_width or x < 0:
            crash()
        if thing_starty > display_height:
            thing_startx = random.randrange(0, display_width - thing_widh)
            thing_starty = 0 - thing_height
            dodged += 1
            thing_speed += 1

        # y crossover
        if y < thing_starty + thing_height:
            # x crossover
            if thing_startx < x < thing_startx + thing_widh or thing_startx < x + car_width < thing_startx + thing_widh:
                crash()

        pygame.display.update()
        clock.tick(60)


game_loop()