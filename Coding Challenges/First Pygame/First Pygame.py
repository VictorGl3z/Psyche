import pygame
from sys import exit
from random import randint

def Display_Score():
    curr_time = int(pygame.time.get_ticks()/1000) - start_time
    score_surf = test_font.render(f'{curr_time}', False, (64,64,64))
    score_rect = score_surf.get_rect(center = (400,50))
    screen.blit(score_surf, score_rect)
    return curr_time

def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5
            
            if obstacle_rect.bottom == 300:
                screen.blit(snail_surf, obstacle_rect)
            else:
                screen.blit(fly_surf, obstacle_rect)
            
        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100 ]
            
        return obstacle_list
    else:
        return []

def collisions(player,obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect):
                return False
    return True

def player_animation():
    global player_surf, player_index
    
    if player_rect.bottom < 300:
        # Jump
        player_surf = player_jump
    else:
        player_index += 0.1
        if player_index >= len(player_walk):
            player_index = 0
        player_surf = player_walk[int(player_index)]
        
        # Walk
        
    # Play Walking Animation if Player on Floor
    # Display Jump Surface when player is not on floor
    
    

pygame.init() # Initiates Pygame

width = 800
height = 400
res = width, height                         # Resolution of the Screen, has to be a tuple

screen = pygame.display.set_mode(res)       # Display surface (Window that players will see)
pygame.display.set_caption('Runner')        # Title Change
clock = pygame.time.Clock()                 # Gives us a clock object
test_font = pygame.font.Font('graphics/font/Pixeltype.ttf', 50)     # Specify (font type, font size)
game_active = False
start_time = 0
score = 0


sky_surf = pygame.image.load("graphics/Sky.png").convert_alpha()                 # Import Sky image from the folder
ground_surf = pygame.image.load("graphics/ground.png").convert_alpha()           # The convert alpha converts the png to files pygame can work with better. Alpha after the convert respects the alpha values

# Score Text & Surface
score_surf = test_font.render('My game', False, (64,64,64))                      # The 3 arguments are the text information, if you want to anti-aliase it and the color
score_rect = score_surf.get_rect(center = (width/2, 50))

# Obstacles
snail_x_pos = 600
snail_surf = pygame.image.load('graphics/snail/snail1.png').convert_alpha()      # Import the Snail image from the folder
fly_surf   = pygame.image.load('graphics/fly/fly1.png').convert_alpha()          # Import the Fly image from the folder


obstacle_rect_list = []

# Player Creation
player_walk_1 = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_walk_2 = pygame.image.load('graphics/player/player_walk_2.png').convert_alpha()
player_walk = [player_walk_1, player_walk_2]
player_index = 0
player_jump = pygame.image.load('graphics/player/jump.png').convert_alpha()
player_rect = player_walk_1.get_rect(midbottom = (80, 300))
player_grav = 0

player_surf = player_walk[player_index]

# Intro Screen
player_stand = pygame.image.load('graphics/player/player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand,0,2)
player_stand_rect = player_stand.get_rect(center = (400,200))

# Text
gameTitle = test_font.render('Pixel Runner', False, (111,196,169))              # Name of the Title
Title_Rect = gameTitle.get_rect(center = (400,50))
instructions = test_font.render('Press SPACE to start', False, (111,196,169))   # Instructions
instructions_Rect= instructions.get_rect(center = (400,350))

# Timer
obstacler_timer = pygame.USEREVENT + 1  # We add + 1 to avoid triggering an already defined event by pygame
pygame.time.set_timer(obstacler_timer, 1400)

while True:
    for event in pygame.event.get():        # Gets all of the events in Pygame and the for looks through each of them
        if event.type == pygame.QUIT:
            pygame.quit()                   # Closes the pygame window
            exit()
        if game_active == True:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                    player_grav = -20
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300:
                    player_grav = -20
        else:
            if event.type == pygame.KEYDOWN and event.key ==pygame.K_SPACE:
                game_active = True
                start_time = int(pygame.time.get_ticks()/1000)
        if event.type == obstacler_timer and game_active:
            if randint(0,2) == 0:
                obstacle_rect_list.append(snail_surf.get_rect(bottomright = (randint(900, 1100),300)))
            else:
                obstacle_rect_list.append(fly_surf.get_rect(bottomright = (randint(900, 1100),210)))
    
    if game_active:
        screen.blit(sky_surf,(0,0))          # Place the sky surface on the screen
        screen.blit(ground_surf,(0,300))     # Place the ground surface just where the sky ends
        
        score = Display_Score()
        # Player 
        player_grav += 1
        player_rect.y += player_grav
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        player_animation()
        screen.blit(player_surf, player_rect)
        
        # Obstacle Movement
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)
        
        # Obstacle Collition
        game_active = collisions(player_rect, obstacle_rect_list)
    else:
        screen.fill((94,129,162))
        screen.blit(player_stand,player_stand_rect)
        screen.blit(gameTitle, Title_Rect)
        player_rect.midbottom = (80,300)
        player_gravity = 0
        obstacle_rect_list.clear()

        
        if score == 0:
            screen.blit(instructions, instructions_Rect)
        else:
            score_msg = test_font.render(f'Your score: {score}', False, (111,196,169))
            score_msg_rect = score_msg.get_rect(center = (400,330))
            screen.blit(score_msg,score_msg_rect)

        
        
    pygame.display.update()                 # Updates the display surface.
    clock.tick(60)                          # Tells Pygame that the while Loop should not run faster than 60 fps
    