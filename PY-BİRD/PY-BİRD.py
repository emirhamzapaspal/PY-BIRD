import pygame, random

pygame.init()

height = 1000
width = 500
running = True
player_x = 255
player_y = 300
walldown_x = 400
walldown_y = 500
wallup_x = 400
wallup_y = 0
wallup_high = 100
walldown_high = 500
jump = False
game_over = False
score = 0
font = pygame.font.SysFont("arialblack", 40)

game_over_text = font.render("GAME OVER", True, (255,255,255))
game_over_text_pos = game_over_text.get_rect()
game_over_text_pos.topleft = (10, 50)

game_over_text_2 = font.render("Press R to Restart", True, (255,255,255))
game_over_text_pos_2 = game_over_text_2.get_rect()
game_over_text_pos_2.topleft = (10, 100)

pencere = pygame.display.set_mode((width, height))

while running == True:
    score_text = font.render("Score: " + str(score), True, (255,255,255))
    score_text_pos = score_text.get_rect()
    score_text_pos.topleft = (10, 600)
    if jump == False:
        player_y = player_y + 0.8
    keys = pygame.key.get_pressed()
    pencere.fill((0,200,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                jump = True
                player_y = player_y - 60
        else:
            jump = False
    if player_y > 730 or player_y < 0:
        game_over = True
    if game_over == True:
        jump = True
        score = 0
        player_y = 300
        pencere.blit(game_over_text, game_over_text_pos)
        pencere.blit(game_over_text_2, game_over_text_pos_2)

        if keys[pygame.K_r]:
            game_over = False
    if game_over == False:
        walldown_x = walldown_x - 1
        wallup_x = wallup_x - 1
    player = pygame.draw.circle(pencere, ((255,255,255)), (player_x, player_y), 10, 0)   
    walldown = pygame.draw.rect(pencere, ((255,255,0)),(walldown_x,walldown_y,100,walldown_high), 0, -1)
    wallup = pygame.draw.rect(pencere, ((255,255,0)),(wallup_x,wallup_y,100,wallup_high), 0, -1)
    if player.colliderect(walldown):
        game_over = True
    if player.colliderect(wallup):
        game_over = True
    
    if walldown_x < 0:
        wallup_random = random.randint(100, 300)
        if wallup_random < 200:
            walldown_random = random.randint(300, 600)
        else:
            walldown_random = random.randint(400, 600)
        wallup_x = 400
        walldown_x = 400
        wallup_high = wallup_random
        walldown_y = walldown_random
    if player_x == wallup_x:
        score = score + 1
    
    pencere.blit(score_text, score_text_pos)
    pygame.display.update()