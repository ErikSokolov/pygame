import pygame
from random import randint

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

player = pygame.Rect((350, 375, 50, 50))
mirror_player = pygame.Rect((400, 375, 50, 50))

#Colors
color = (randint(0, 255), randint(0, 255), randint(0, 255))

run = True
while run:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
	

	
	key = pygame.key.get_pressed()
	
	if key[pygame.K_s] or key[pygame.K_g] or key[pygame.K_d] or key[pygame.K_f]:
		background_color = (255, 255, 255)
	else:
		background_color = (0, 0, 0)

	screen.fill(background_color)

	if key[pygame.K_s]:
		player.move_ip(-1,0)
		color = (randint(0, 255), randint(0, 255), randint(0,255))
	elif key[pygame.K_g]:
		player.move_ip(1,0)
		color = (randint(0, 255), randint(0, 255), randint(0,255))
	elif key[pygame.K_d]:
		player.move_ip(0,-1)
		color = (randint(0, 255), randint(0, 255), randint(0,255))
	elif key[pygame.K_f]:
		player.move_ip(0,1)
		color = (randint(0, 255), randint(0, 255), randint(0,255))


	pygame.draw.rect(screen, color, player)
	
	if key[pygame.K_s]:
		mirror_player.move_ip(1,0)
	elif key[pygame.K_g]:
		mirror_player.move_ip(-1,0)
	elif key[pygame.K_d]:
		mirror_player.move_ip(0,1)
	elif key[pygame.K_f]:
		mirror_player.move_ip(0,-1)

	pygame.draw.rect(screen, (0, 0, 255), mirror_player)

	pygame.display.update()

pygame.quit()

