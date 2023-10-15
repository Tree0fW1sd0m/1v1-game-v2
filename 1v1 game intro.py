import pygame,sys
import random

#python setup
screen_width = 1280
screen_height = 720
pygame.init()
screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()
screen.fill("white")

bkImg = pygame.image.load('1v1 game v2/sprites/zuko_p1card.png') #loads image into pygame
screen.blit(bkImg, (300, 200)) #displays image on surface

bkImg = pygame.image.load('1v1 game v2/sprites/zuko_p2card.png') #loads image into pygame
screen.blit(bkImg, (700, 200)) #displays image on surface
optionp1 = 0
optionp2 = 0
game_beginp1 = False
game_beginp2 = False

while game_beginp1 == False or game_beginp2 == False:
    pygame.display.update()
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    pygame.quit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
                optionp1 += -1
                if optionp1 <= 0:
                    optionp1 = 6
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_d:
                optionp1 += 1
                if optionp1 >= 7:
                    optionp1 = 1
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                optionp2 += -1
                if optionp2 <= 0:
                    optionp2 = 6
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                optionp2 += 1
                if optionp2 >= 7:
                    optionp2 = 1
                
        if optionp1 == 1:
            bkImg = pygame.image.load('1v1 game v2/sprites/zuko_p1card.png') #loads image into pygame
            screen.blit(bkImg, (300, 200)) #displays image on surface
        elif optionp1 == 2:
            bkImg = pygame.image.load('1v1 game v2/sprites/katara_p1card.png') #loads image into pygame
            screen.blit(bkImg, (300, 200)) #displays image on surface
        elif optionp1 == 3:
            bkImg = pygame.image.load('1v1 game v2/sprites/aang_p1card.png') #loads image into pygame
            screen.blit(bkImg, (300, 200)) #displays image on surface
        elif optionp1 == 4:
            bkImg = pygame.image.load('1v1 game v2/sprites/toph_p1card.png') #loads image into pygame
            screen.blit(bkImg, (300, 200)) #displays image on surface
        elif optionp1 == 5:
            bkImg = pygame.image.load('1v1 game v2/sprites/sokka_p1card.png') #loads image into pygame
            screen.blit(bkImg, (300, 200)) #displays image on surface
        elif optionp1 == 6:
            bkImg = pygame.image.load('1v1 game v2/sprites/random_card.png') #loads image into pygame
            screen.blit(bkImg, (300, 200)) #displays image on surface
            
        if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
            random_option = 0 
            if optionp1 == 6:
                random_option = random.randint(1,5)
            if optionp1 == 1 or random_option == 1:
                player1_sprite = '1v1 game v2/sprites/zuko.png'
            elif optionp1 == 2 or random_option == 2:
                player1_sprite = '1v1 game v2/sprites/katara.png'
            elif optionp1 == 3 or random_option == 3:
                player1_sprite = '1v1 game v2/sprites/aang.png'
            elif optionp1 == 4 or random_option == 4:
                player1_sprite = '1v1 game v2/sprites/toph.png'
            elif optionp1 == 5 or random_option == 5:
                player1_sprite = '1v1 game v2/sprites/sokka.png'
            game_beginp1 = True
        
        if optionp2 == 1:
            bkImg = pygame.image.load('1v1 game v2/sprites/zuko_p2card.png') #loads image into pygame
            screen.blit(bkImg, (700, 200)) #displays image on surface
        elif optionp2 == 2:
            bkImg = pygame.image.load('1v1 game v2/sprites/katara_p2card.png') #loads image into pygame
            screen.blit(bkImg, (700, 200)) #displays image on surface
        elif optionp2 == 3:
            bkImg = pygame.image.load('1v1 game v2/sprites/aang_p2card.png') #loads image into pygame
            screen.blit(bkImg, (700, 200)) #displays image on surface
        elif optionp2 == 4:
            bkImg = pygame.image.load('1v1 game v2/sprites/toph_p2card.png') #loads image into pygame
            screen.blit(bkImg, (700, 200)) #displays image on surface
        elif optionp2 == 5:
            bkImg = pygame.image.load('1v1 game v2/sprites/sokka_p2card.png') #loads image into pygame
            screen.blit(bkImg, (700, 200)) #displays image on surface
        elif optionp2 == 6:
            bkImg = pygame.image.load('1v1 game v2/sprites/random_card.png') #loads image into pygame
            screen.blit(bkImg, (700, 200)) #displays image on surface
            
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            random_option = 0 
            if optionp2 == 6:
                random_option = random.randint(1,5)
            if optionp2 == 1 or random_option == 1:
                player2_sprite = '1v1 game v2/sprites/zuko_frame2.png'
            elif optionp2 == 2 or random_option == 2:
                player2_sprite = '1v1 game v2/sprites/katara_frame2.png'
            elif optionp2 == 3 or random_option == 3:
                player2_sprite = '1v1 game v2/sprites/aang_frame2.png'
            elif optionp2 == 4 or random_option == 4:
                player2_sprite = '1v1 game v2/sprites/toph_frame2.png'
            elif optionp2 == 5 or random_option == 5:
                player2_sprite = '1v1 game v2/sprites/sokka_frame2.png'
            game_beginp2 = True



while True:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    pygame.quit()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
            
    
    pygame.display.update()
    clock.tick(60)