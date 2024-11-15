import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

player = pygame.Rect((350, 375, 50, 50))
mirror_player = pygame.Rect((400, 375, 50, 50))

run = True
while run:
	
	pygame.draw.rect(screen, (255, 0, 0), player)
	
	key = pygame.key.get_pressed()
	if key[pygame.K_s] == True:
		player.move_ip(-1,0)
	elif key[pygame.K_g] == True:
		player.move_ip(1,0)
	elif key[pygame.K_d] == True:
		player.move_ip(0,-1)
	elif key[pygame.K_f] == True:
		player.move_ip(0,1)

	pygame.draw.rect(screen, (0, 0, 255), mirror_player)
	
	key = pygame.key.get_pressed()
	if key[pygame.K_s] == True:
		mirror_player.move_ip(1,0)
	elif key[pygame.K_g] == True:
		mirror_player.move_ip(-1,0)
	elif key[pygame.K_f] == True:
		mirror_player.move_ip(0,1)
	elif key[pygame.K_d] == True:
		mirror_player.move_ip(0,-1)


	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	pygame.display.update()

pygame.quit()

