import pygame
import sys

class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.sprites = []
        self.sprites.append(pygame.image.load('animation-master/attack_1.png'))
        self.sprites.append(pygame.image.load('animation-master/attack_2.png'))
        self.sprites.append(pygame.image.load('animation-master/attack_3.png'))
        self.sprites.append(pygame.image.load('animation-master/attack_4.png'))
        self.sprites.append(pygame.image.load('animation-master/attack_5.png'))
        self.sprites.append(pygame.image.load('animation-master/attack_6.png'))
        self.sprites.append(pygame.image.load('animation-master/attack_7.png'))
        self.sprites.append(pygame.image.load('animation-master/attack_8.png'))
        self.sprites.append(pygame.image.load('animation-master/attack_9.png'))
        self.sprites.append(pygame.image.load('animation-master/attack_10.png'))


#General setup
pygame.init()
clock = pygame.time.Clock()

#Game screen
screen_width = 800
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Sprite Animation")

moving_sprites = pygame.sprite.Group()
player = Player(100,100)
moving_sprites.add(player)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #Drawing
    screen.fill((0,0,0))
    moving_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(60)



