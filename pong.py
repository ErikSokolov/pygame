import pygame

pygame.init()

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


paddle_width = 10
paddle_height = 100
paddle_speed = 2


ball_size = 10
ball_speed_x = 0.2
ball_speed_y = 0.2


paddle1_x = 10
paddle1_y = (SCREEN_HEIGHT - paddle_height) // 2
paddle2_x = SCREEN_WIDTH - paddle_width - 10
paddle2_y = (SCREEN_HEIGHT - paddle_height) //2
ball_x = SCREEN_WIDTH // 2
ball_y = SCREEN_HEIGHT // 2

run = True


screen.fill((0, 0, 0))


while run:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
	ball_x += ball_speed_x
	ball_y += ball_speed_y

	if ball_y <= 0 or ball_y >= SCREEN_HEIGHT - ball_size:
		ball_speed_y = -ball_speed_y

	if (ball_x <= paddle1_x + paddle_width and paddle1_y <= ball_y <= paddle1_y + paddle_height) or (ball_x + ball_size >= paddle2_x and paddle2_y <= ball_y <= paddle2_y + paddle_height):
		ball_speed_x = -ball_speed_x

	keys = pygame.key.get_pressed()
	if keys[pygame.K_f] and paddle1_y > 0:
		paddle1_y -= paddle_speed
	if keys[pygame.K_d] and paddle1_y < SCREEN_HEIGHT - paddle_height:
		paddle1_y += paddle_speed
	if keys[pygame.K_k] and paddle2_y > 0:
		paddle2_y -= paddle_speed
	if keys[pygame.K_j] and paddle2_y < SCREEN_HEIGHT - paddle_height:
		paddle2_y += paddle_speed
	

	screen.fill((0, 0, 0))


	pygame.draw.rect(screen, (255, 255, 200), (paddle1_x, paddle1_y, paddle_width, paddle_height))
	pygame.draw.rect(screen, (200, 255, 255), (paddle2_x, paddle2_y, paddle_width, paddle_height))
	pygame.draw.rect(screen, (255, 200, 255), (ball_x, ball_y, ball_size, ball_size))


	pygame.display.update()

