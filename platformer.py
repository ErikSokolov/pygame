import pygame, sys

clock = pygame.time.Clock()

from pygame.locals import *

pygame.init()

pygame.display.set_caption('60fps Window')

WINDOW_SIZE = (400, 400)

screen = pygame.display.set_mode(WINDOW_SIZE,0,32)

player_image = pygame.image.load('player.jpg')

while True:

    screen.blit(player_image, (50, 50))
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(60)

