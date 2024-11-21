import pygame
from sys import exit
from random import randint

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('UltimatePygameIntro-main/graphics/Player/player_walk_1.png').convert_alpha
        self.rect = self.image.get_rect(midbottom = (200, 300))

def display_score():
    current_time = int((pygame.time.get_ticks() - start_time)/1000)
    score_surf = test_font.render(f'Score: {current_time}', False, (64,64,64))
    score_rect = score_surf.get_rect(center = (400, 50))
    screen.blit(score_surf, score_rect)
    return current_time

def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5
            if obstacle_rect.bottom == 300:
                screen.blit(snail_surf, obstacle_rect)
            elif obstacle_rect.bottom == 200:
                screen.blit(fly_surf, obstacle_rect)
            screen.blit(snail_surf, obstacle_rect)
        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]
        return obstacle_list
    else:
        return []

def collisions(player, obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect):
                return False
    return True
    

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('UltimatePygameIntro-main/font/Pixeltype.ttf', 50)
game_active = True
start_time = 0
score = 0


player = Player()


sky_surface = pygame.image.load('../clearcode/UltimatePygameIntro-main/graphics/Sky.png').convert()
ground_surface = pygame.image.load('UltimatePygameIntro-main/graphics/ground.png').convert()

#score_surf = test_font.render('My game', False,(64, 64, 64)) 
#score_rect = score_surf.get_rect(center = (400, 50))

snail_frame_1 = pygame.image.load('UltimatePygameIntro-main/graphics/snail/snail1.png').convert_alpha()
snail_frame_2 = pygame.image.load('UltimatePygameIntro-main/graphics/snail/snail1.png').convert_alpha()
snail_frames = [snail_frame_1, snail_frame_2]
snail_frame_index = 0
snail_surf = snail_frames[snail_frame_index]

fly_surf = pygame.image.load('UltimatePygameIntro-main/graphics/Fly/Fly1.png').convert_alpha()
fly_rect = fly_surf.get_rect(midbottom = (550, 200))


obstacle_rect_list = []

player_walk_1= pygame.image.load('UltimatePygameIntro-main/graphics/Player/player_walk_1.png').convert_alpha()
player_walk_2 = pygame.image.load('UltimatePygameIntro-main/graphics/Player/player_walk_2.png').convert_alpha()
player_walk = [player_walk_1, player_walk_2]
player_index = 0 

def player_animation():
    #play walking animation
    #play jump animation when flying
    global player_surf, player_index

    if player_rect.bottom < 300:
        player_surf = player_jump 
    else:
        player_index += 0.1
        if player_index >= len(player_walk):player_index = 0
        player_surf = player_walk[int(player_index)]

player_surf = player_walk[player_index]
player_jump = pygame.image.load('UltimatePygameIntro-main/graphics/Player/jump.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80, 300))
player_gravity = 0
player_stand = pygame.image.load('UltimatePygameIntro-main/graphics/Player/player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand,0,2)
player_stand_rect = player_stand.get_rect(center = (400,200))

game_message = test_font.render('Press space to run', False, (111, 169, 196))
game_message_rect = game_message.get_rect(center= (400, 320))

obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 900)

snail_animation_timer = pygame.USEREVENT +2
pygame.time.set_timer(snail_animation_timer, 500)




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                    player_gravity = -20
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos):
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_active = True
                    start_time = pygame.time.get_ticks()

    if game_active:
        if event.type == obstacle_timer:
            if randint(0,2):
                obstacle_rect_list.append(snail_surf.get_rect(bottomright = (randint(900,1100), 300)))
            else:
                obstacle_rect_list.append(snail_surf.get_rect(bottomright = (randint(900,1100), 210)))
            if event.type == snail_animation_timer:
                if snail_frame_index == 0: snail_frame_index = 1 
            else:
                snail_frame_index = 0
                snail_surf = snail_frames[snail_frame_index]





    if game_active:
        screen.blit(sky_surface,(0,0))
        screen.blit(ground_surface,(0,300))
        display_score()
        score = display_score()

        fly_rect.left -= 4
        screen.blit(fly_surf, fly_rect)

        #foo
        #foo
        player_gravity += 1 
        player_rect.y += player_gravity
        if player_rect.bottom >= 300: player_rect.bottom = 300
        player_animation()
        screen.blit(player_surf, player_rect)

        obstacle_rect_list = obstacle_movement(obstacle_rect_list)
        
        #collision
            
        game_active = collisions(player_rect, obstacle_rect_list)



    else:

        screen.fill((94, 129, 162))
        screen.blit(player_stand, player_stand_rect)
        player_rect.midbottom = (80, 300)

        obstacle_rect_list.clear()

        title_surf = test_font.render('My game', False,(64, 64, 64)) 
        title_rect = title_surf.get_rect(center = (400, 50))
        screen.blit(title_surf, title_rect)        



        score_message = test_font.render(f'{score}', False, (222, 222, 222))
        score_message_rect = score_message.get_rect(center = (400, 340))
        screen.blit(score_message, score_message_rect)
        

        



    pygame.display.update()
    clock.tick(60)
