import pygame,sys
import random
import time

#python Setup
screen_width = 1280
screen_height = 720
pygame.init()
screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()
screen.fill("white")

pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.
my_font = pygame.font.SysFont('viga', 30)
title = pygame.font.SysFont('viga', 50)
player1_text1 = title.render('Player 1', False, (0, 0, 0))
player1_text2 = my_font.render('WASD', False, (0, 0, 0))
player1_text3 = my_font.render('"a" and "d" to move', False, (0, 0, 0))
player1_text4 = my_font.render('"w" to jump and "s" to attack', False, (0, 0, 0))
screen.blit(player1_text1, (380,50))
screen.blit(player1_text2, (410,100))
screen.blit(player1_text3, (350,130))
screen.blit(player1_text4, (310,160))

player2_text1 = title.render('Player 2', False, (0, 0, 0))
player2_text2 = my_font.render('Arrow Keys', False, (0, 0, 0))
player2_text3 = my_font.render('"LEFT" and "RIGHT" to move', False, (0, 0, 0))
player2_text4 = my_font.render('"UP" to jump and "DOWN" to attack', False, (0, 0, 0))
screen.blit(player2_text1, (780,50))
screen.blit(player2_text2, (790,100))
screen.blit(player2_text3, (720,130))
screen.blit(player2_text4, (680,160))

bkImg = pygame.image.load('1v1-game-v2/sprites/zuko_p1card.png') #loads image into pygame
screen.blit(bkImg, (300, 200)) #displays image on surface

bkImg = pygame.image.load('1v1-game-v2/sprites/zuko_p2card.png') #loads image into pygame
screen.blit(bkImg, (700, 200)) #displays image on surface
optionp1 = 1
optionp2 = 1
game_beginp1 = False
game_beginp2 = False

while game_beginp1 == False or game_beginp2 == False:
        pygame.display.update()
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                        pygame.quit()
            if game_beginp1 == False:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
                        optionp1 += -1
                        if optionp1 <= 0:
                            optionp1 = 6
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_d:
                        optionp1 += 1
                        if optionp1 >= 7:
                            optionp1 = 1
            else:
                bkImg = pygame.image.load('1v1-game-v2/sprites/ready_card.png') #loads image into pygame
                screen.blit(bkImg, (370, 30)) #displays image on surface
            if game_beginp2 == False:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                        optionp2 += -1
                        if optionp2 <= 0:
                            optionp2 = 6
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                        optionp2 += 1
                        if optionp2 >= 7:
                            optionp2 = 1
            else:
                bkImg = pygame.image.load('1v1-game-v2/sprites/ready_card.png') #loads image into pygame
                screen.blit(bkImg, (770, 30)) #displays image on surface
                    
            if optionp1 == 1:
                bkImg = pygame.image.load('1v1-game-v2/sprites/zuko_p1card.png') #loads image into pygame
                screen.blit(bkImg, (300, 200)) #displays image on surface
            elif optionp1 == 2:
                bkImg = pygame.image.load('1v1-game-v2/sprites/katara_p1card.png') #loads image into pygame
                screen.blit(bkImg, (300, 200)) #displays image on surface
            elif optionp1 == 3:
                bkImg = pygame.image.load('1v1-game-v2/sprites/aang_p1card.png') #loads image into pygame
                screen.blit(bkImg, (300, 200)) #displays image on surface
            elif optionp1 == 4:
                bkImg = pygame.image.load('1v1-game-v2/sprites/toph_p1card.png') #loads image into pygame
                screen.blit(bkImg, (300, 200)) #displays image on surface
            elif optionp1 == 5:
                bkImg = pygame.image.load('1v1-game-v2/sprites/sokka_p1card.png') #loads image into pygame
                screen.blit(bkImg, (300, 200)) #displays image on surface
            elif optionp1 == 6:
                bkImg = pygame.image.load('1v1-game-v2/sprites/random_card.png') #loads image into pygame
                screen.blit(bkImg, (300, 200)) #displays image on surface
                
            if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
                random_option = 1
                if optionp1 == 6:
                    optionp1 = random.randint(1,5)
                    continue
                if optionp1 == 1 or random_option == 1:
                    player1_sprite = 1
                elif optionp1 == 2 or random_option == 2:
                    player1_sprite = 2
                elif optionp1 == 3 or random_option == 3:
                    player1_sprite = 3
                elif optionp1 == 4 or random_option == 4:
                    player1_sprite = 4
                elif optionp1 == 5 or random_option == 5:
                    player1_sprite = 5
                game_beginp1 = True
                


            if optionp2 == 1:
                bkImg = pygame.image.load('1v1-game-v2/sprites/zuko_p2card.png') #loads image into pygame
                screen.blit(bkImg, (700, 200)) #displays image on surface
            elif optionp2 == 2:
                bkImg = pygame.image.load('1v1-game-v2/sprites/katara_p2card.png') #loads image into pygame
                screen.blit(bkImg, (700, 200)) #displays image on surface
            elif optionp2 == 3:
                bkImg = pygame.image.load('1v1-game-v2/sprites/aang_p2card.png') #loads image into pygame
                screen.blit(bkImg, (700, 200)) #displays image on surface
            elif optionp2 == 4:
                bkImg = pygame.image.load('1v1-game-v2/sprites/toph_p2card.png') #loads image into pygame
                screen.blit(bkImg, (700, 200)) #displays image on surface
            elif optionp2 == 5:
                bkImg = pygame.image.load('1v1-game-v2/sprites/sokka_p2card.png') #loads image into pygame
                screen.blit(bkImg, (700, 200)) #displays image on surface
            elif optionp2 == 6:
                bkImg = pygame.image.load('1v1-game-v2/sprites/random_card.png') #loads image into pygame
                screen.blit(bkImg, (700, 200)) #displays image on surface
                
            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                random_option = 2
                if optionp1 == 6:
                    optionp1 = random.randint(1,5)
                    continue
                if optionp2 == 1 or random_option == 1:
                    player2_sprite = 1
                elif optionp2 == 2 or random_option == 2:
                    player2_sprite = 2
                elif optionp2 == 3 or random_option == 3:
                    player2_sprite = 3
                elif optionp2 == 4 or random_option == 4:
                    player2_sprite = 4
                elif optionp2 == 5 or random_option == 5:
                    player2_sprite = 5
                game_beginp2 = True

selector_map = 0
time.sleep(1)
screen.fill('white')
map_begin = False
optionmap = 1
while map_begin == False:
        pygame.display.update()
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                        pygame.quit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
                    optionmap += -1
                    if optionmap <= 0:
                        optionmap = 6
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_d:
                    optionmap += 1
                    if optionmap >= 7:
                        optionmap = 1
                
            if optionmap == 1:
                selector_map = 1
                screen.fill('white')
                bkImg = pygame.image.load('1v1-game-v2/sprites/the_map_card.png') #loads image into pygame
                screen.blit(bkImg, (500, 200)) #displays image on surface
            elif optionmap == 2:
                selector_map = 2
                screen.fill('white')
                bkImg = pygame.image.load('1v1-game-v2/sprites/deathmatch_card.png') #loads image into pygame
                screen.blit(bkImg, (500, 200)) #displays image on surface
            elif optionmap == 3:
                selector_map = 3
                screen.fill('white')
                bkImg = pygame.image.load('1v1-game-v2/sprites/bonk_card.png') #loads image into pygame
                screen.blit(bkImg, (500, 200)) #displays image on surface
            elif optionmap == 4:
                selector_map = 4
                screen.fill('white')
                bkImg = pygame.image.load('1v1-game-v2/sprites/dualarena_card.png') #loads image into pygame
                screen.blit(bkImg, (500, 200)) #displays image on surface
            elif optionmap == 5:
                selector_map = 5
                screen.fill('white')
                bkImg = pygame.image.load('1v1-game-v2/sprites/platform_card.png') #loads image into pygame
                screen.blit(bkImg, (500, 200)) #displays image on surface
            elif optionmap == 6:
                selector_map = 6
                screen.fill('white')
                bkImg = pygame.image.load('1v1-game-v2/sprites/random_card.png') #loads image into pygame
                screen.blit(bkImg, (500, 200)) #displays image on surface
            map_text1 = title.render('Map Selector', False, (0, 0, 0))
            screen.blit(map_text1, (545,100))
                
            if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
                random_option = 1
                if optionmap == 6:
                    optionmap = random.randint(1,5)
                    continue
                if optionmap == 1 or selector_map == 1:
                    map = 1
                elif optionmap == 2 or  selector_map  == 2:
                    map = 2
                elif optionmap == 3 or  selector_map  == 3:
                    map = 3
                elif optionmap == 4 or  selector_map  == 4:
                    map = 4
                elif optionmap == 5 or  selector_map  == 5:
                    map = 5
                map_begin = True
#-------------------------------------------------------------------------------SETTINGS

if map == 1:
    #OG map
    level_map = ['XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    'X                                                                              X',
    'X                                                                              X',
    'X                                                                              X',
    'X                                                                              X',
    'X                                                                              X',
    'X                                                                              X',
    'X                                                                              X',
    'X                                                                              X',
    'X                                                                              X',
    'X                                                                              X',
    'X                                                                              X',
    'X                                                                              X',
    'X                              XXXXXXXXXXXXXXXXX                               X',
    'X                              XXXXXXXXXXXXXXXXX                               X',
    'X                                                                              X',
    'X                                                                              X',
    'X                                                                              X',
    'X                                                                              X',
    'X                                                                              X',
    'X                                                                              X',
    'X   P                                                                      T   X',
    'X                                                                              X',
    'X                                                                              X',
    'X                                                                              X',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX               XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX               XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'X                                                                              X',
    'X                                                                              X',
    'X                                                                              X',
    'X                                                                              X',
    'X                                                                              X',
    'X                                                                              X',
    'X                                                                              X',
    'X                                                                              X',
    'X                                                                              X',
    'X                                                                              X',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',]
elif map == 2:
    #deathmatch map
    level_map = [
        'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    'X                                                                              X',
    'X                                                                              X',
    'X                                                                              X',
    'X                                                                              X',
    'X                                                                              X',
    'X                                                                              X',
    'X                                                                              X',
    'X                                                                              X',
    'X                                                                              X',
    'X                                                                              X',
    'X                                                                              X',
    'X                                                                              X',
    'X                                                                              X',
    'X                                                                              X',
    'X                                                                              X',
    'X                                                                              X',
    'X                                                                              X',
    'X                                                                              X',
    'X                                                                              X',
    'X                                                                              X',
    'X                                                                              X',
    'X                                                                              X',
    'X                                                                              X',
    'X                                                                              X',
    'X                                                                              X',
    'X                                                                              X',
    'X                                                                              X',
    'X                                                                              X',
    'X                                                                              X',
    'X                                                                              X',
    'X                                                                              X',
    'X                                                                              X',
    'X   P                                                                       T  X',
    'X                                                                              X',
    'X                                                                              X',
    'X                                                                              X',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',]
elif map == 3:
    #bonk
    level_map = [    
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    'X                                      XX                                      X',
    'X                                      XX                                      X',
    'X                                      XX                                      X',
    'X                                      XX                                      X',
    'X                                      XX                                      X',
    'X                                      XX                                      X',
    'X                                      XX                                      X',
    'X                             XXXXXXXXXXXXXXXXXXXX                             X',
    'X                                                                              X',
    'X                                                                              X',
    'X                                                                              X',
    'X                                                                              X',
    'X                                                                              X',
    'XXXXXXXXXXXXXXXXXXX                                          XXXXXXXXXXXXXXXXXXX',
    'X                                                                              X',
    'X                                                                              X',
    'X     P                                                                 T      X',
    'X                                                                              X',
    'X                                                                              X',
    'X                             XXXXXXXXXXXXXXXXXXXX                             X',
    'X                                      XX                                      X',
    'X                                      XX                                      X',
    'XXXXXXXXXXXXXXXXXXX                    XX                    XXXXXXXXXXXXXXXXXXX',
    'X                                      XX                                      X',
    'X                                      XX                                      X',
    'X                                      XX                                      X',
    'X                                      XX                                      X',
    'X                                      XX                                      X',
    'X                                      XX                                      X',
    'X                    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX                    X',
    'X                                      XX                                      X',
    'X                                      XX                                      X',
    'X                                      XX                                      X',
    'X                                      XX                                      X',
    'X                                      XX                                      X',
    'X                                      XX                                      X',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',]    
elif map == 4:
    
    level_map = ['XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    'X                                                                              X',
    'X                                                                              X',
    'X                                                                              X',
    'X                                                                              X',
    'X                                                                              X',
    'X                                                                              X',
    'X                                                                              X',
    'X          XXXXXXXXXXXXXXXXXXXXXXX            XXXXXXXXXXXXXXXXXXXXXXX          X',
    'X                      X                                X                      X',
    'X                      X                                X                      X',
    'X                      X                                X                      X',
    'X                      X                                X                      X',
    'X                      X                                X                      X',
    'X                                                                              X',
    'XXXXXXXXXXX                                                          XXXXXXXXXXX',
    'X                                                                              X',
    'X                                                                              X',
    'X     P                                                                 T      X',
    'X                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX                      X',
    'X                                                                              X',
    'X                                                                              X',
    'X                                                                              X',
    'XXXXXXXXXXX                                                          XXXXXXXXXXX',
    'X                                                                              X',
    'X                      X                                X                      X',
    'X                      X                                X                      X',
    'X                      X                                X                      X',
    'X                      X                                X                      X',
    'X                      X                                X                      X',
    'X          XXXXXXXXXXXXXXXXXXXXXXX            XXXXXXXXXXXXXXXXXXXXXXX          X',
    'X                                                                              X',
    'X                                                                              X',
    'X                                                                              X',
    'X                                                                              X',
    'X                                                                              X',
    'X                                                                              X',
    'X                                                                              X',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',]   
elif map == 5:
    #platform
    level_map = [
        'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    'X                                                                              X',
    'X                                                                              X',
    'X                                                                              X',
    'X                                                                              X',
    'X                                                                              X',
    'X                                                                              X',
    'X                                                                              X',
    'X                                                                              X',
    'X                                                                              X',
    'X                                                                              X',
    'X                                                                              X',
    'X                                                                              X',
    'X                                                                              X',
    'X                                                                              X',
    'X                                                                              X',
    'X                                                                              X',
    'X                                                                              X',
    'X                                                                              X',
    'X                                                                              X',
    'X                                                                              X',
    'X                                                                              X',
    'X                          XXXXXXXXXXXXXXXXXXXXXXXXXX                          X',
    'X                                                                              X',
    'X                                                                              X',
    'X                                                                              X',
    'X                                                                              X',
    'X                                                                              X',
    'X                                                                              X',
    'X                                                                              X',
    'X                                                                              X',
    'X                                                                              X',
    'X                                                                              X',
    'X                                                                              X',
    'X      P                                                              T        X',
    'X                                                                              X',
    'X                                                                              X',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',]


tile_size = 16
screen_width = 1280
screen_height = len(level_map)*tile_size
#print(screen_height)
#print(len(level_map))
#-------------------------------------------------------------------------------PLAYERS
player_size = 20
jump_height = -4.5

class Player(pygame.sprite.Sprite):
    def __init__(self,x,y,plr_num):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((64,64))
        self.image.fill('purple')
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        
        self.plr_num = plr_num
    
        #player movement
        self.direction = pygame.math.Vector2(0,0)
        self.gravity = 0.8
        self.jump_speed = -20
        
        self.jumping = False
        
        if plr_num == 1:
            if optionp1 == 1:
                image_to_load = pygame.image.load('1v1-game-v2/sprites/zuko.png')
                self.speed = 9
            elif optionp1 == 2:
                image_to_load = pygame.image.load('1v1-game-v2/sprites/katara.png')
                self.speed = 8.5
            elif optionp1 == 3:
                image_to_load = pygame.image.load('1v1-game-v2/sprites/aang.png')
                self.speed = 10
            elif optionp1 == 4:
                image_to_load = pygame.image.load('1v1-game-v2/sprites/toph.png')
                self.speed = 8
            elif optionp1 == 5:
                image_to_load = pygame.image.load('1v1-game-v2/sprites/sokka.png')
                self.speed = 9.5
            self.image.blit(image_to_load,(0,0))
        elif plr_num == 2:
            if optionp2 == 1:
                image_to_load = pygame.image.load('1v1-game-v2/sprites/zuko_frame2.png')
                self.speed = 9
            elif optionp2 == 2:
                image_to_load = pygame.image.load('1v1-game-v2/sprites/katara_frame2.png')
                self.speed = 8.5
            elif optionp2 == 3:
                image_to_load = pygame.image.load('1v1-game-v2/sprites/aang_frame2.png')
                self.speed = 10
            elif optionp2 == 4:
                image_to_load = pygame.image.load('1v1-game-v2/sprites/toph_frame2.png')
                self.speed = 8
            elif optionp2 == 5:
                image_to_load = pygame.image.load('1v1-game-v2/sprites/sokka_frame2.png')
                self.speed = 9.5
        self.image.blit(image_to_load,(0,0))
        self.image.set_colorkey('purple')
        
    def get_input(self):
        keys = pygame.key.get_pressed()
        
        if self.plr_num == 1:
            if keys[pygame.K_a]:
                self.direction.x = -1
                if optionp1 == 1:
                    image_to_load = pygame.image.load('1v1-game-v2/sprites/zuko_frame2.png')
                elif optionp1 == 2:
                    image_to_load = pygame.image.load('1v1-game-v2/sprites/katara_frame2.png')
                elif optionp1 == 3:
                    image_to_load = pygame.image.load('1v1-game-v2/sprites/aang_frame2.png')
                elif optionp1 == 4:
                    image_to_load = pygame.image.load('1v1-game-v2/sprites/toph_frame2.png')
                elif optionp1 == 5:
                    image_to_load = pygame.image.load('1v1-game-v2/sprites/sokka_frame2.png')
                self.image.blit(image_to_load,(0,0))
            elif keys[pygame.K_d]:
                self.direction.x = 1
                if optionp1 == 1:
                    image_to_load = pygame.image.load('1v1-game-v2/sprites/zuko.png')
                elif optionp1 == 2:
                    image_to_load = pygame.image.load('1v1-game-v2/sprites/katara.png')
                elif optionp1 == 3:
                    image_to_load = pygame.image.load('1v1-game-v2/sprites/aang.png')
                elif optionp1 == 4:
                    image_to_load = pygame.image.load('1v1-game-v2/sprites/toph.png')
                elif optionp1 == 5:
                    image_to_load = pygame.image.load('1v1-game-v2/sprites/sokka.png')
                self.image.blit(image_to_load,(0,0))
            else:
                self.direction.x = 0
                
            if keys[pygame.K_w] and not self.jumping:
                self.jumping = True
                self.jump()
                
        elif self.plr_num == 2:
            if keys[pygame.K_LEFT]:
                self.direction.x = -1
                if optionp2 == 1:
                    image_to_load = pygame.image.load('1v1-game-v2/sprites/zuko_frame2.png')
                elif optionp2 == 2:
                    image_to_load = pygame.image.load('1v1-game-v2/sprites/katara_frame2.png')
                elif optionp2 == 3:
                    image_to_load = pygame.image.load('1v1-game-v2/sprites/aang_frame2.png')
                elif optionp2 == 4:
                    image_to_load = pygame.image.load('1v1-game-v2/sprites/toph_frame2.png')
                elif optionp2 == 5:
                    image_to_load = pygame.image.load('1v1-game-v2/sprites/sokka_frame2.png')
                self.image.blit(image_to_load,(0,0))
            elif keys[pygame.K_RIGHT]:
                self.direction.x = 1
                if optionp2 == 1:
                    image_to_load = pygame.image.load('1v1-game-v2/sprites/zuko.png')
                elif optionp2 == 2:
                    image_to_load = pygame.image.load('1v1-game-v2/sprites/katara.png')
                elif optionp2 == 3:
                    image_to_load = pygame.image.load('1v1-game-v2/sprites/aang.png')
                elif optionp2 == 4:
                    image_to_load = pygame.image.load('1v1-game-v2/sprites/toph.png')
                elif optionp2 == 5:
                    image_to_load = pygame.image.load('1v1-game-v2/sprites/sokka.png')
                self.image.blit(image_to_load,(0,0))
            else:
                self.direction.x = 0
                
            if keys[pygame.K_UP] and not self.jumping:
                self.jumping = True
                self.jump()

    def apply_gravity(self):
        self.direction.y+= self.gravity
        self.rect.y += self.direction.y
         
    def jump(self):
        self.direction.y += self.jump_speed
        
    def update(self):
        self.get_input()
        
#-------------------------------------------------------------------------------LEVEL
class Level:
    def __init__(self,level_data,surface):
        self.display_surface = surface
        self.setup_level(level_data)
        pass
        
    def setup_level(self,layout):
        self.tiles = pygame.sprite.Group()
        self.players = pygame.sprite.Group()
        # self.player2 = pygame.sprite.GroupSingle()
        
        for row_index,row in enumerate(layout):
            for col_index,cell in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size
                
                if cell == 'X':
                    tile = Tile((x,y),tile_size)
                    self.tiles.add(tile)
                if cell == 'P':
                    player_sprite = Player(x, y, 1)
                    self.players.add(player_sprite)
                if cell == "T":
                    player2_sprite = Player(x,y, 2)
                    self.players.add(player2_sprite)
                    
    def horizontal_movement_collision(self):
        # player = self.players.sprites()
        for plr_sprite in self.players.sprites():
            plr_sprite.rect.x += plr_sprite.direction.x*plr_sprite.speed
        
            for sprite in self.tiles.sprites():
                if sprite.rect.colliderect(plr_sprite.rect):
                    if plr_sprite.direction.x < 0:
                        plr_sprite.rect.left = sprite.rect.right
                    elif plr_sprite.direction.x > 0:
                        plr_sprite.rect.right = sprite.rect.left
    
    def vertical_movement_collision(self):
        # player = self.players.sprites()
        for plr_sprite in self.players.sprites():
            plr_sprite.apply_gravity()
            for sprite in self.tiles.sprites():
                if sprite.rect.colliderect(plr_sprite.rect):
                    if plr_sprite.direction.y > 0:
                        plr_sprite.rect.bottom = sprite.rect.top
                        plr_sprite.direction.y = 0
                        plr_sprite.jumping = False
                    elif plr_sprite.direction.y < 0:
                        plr_sprite.rect.top = sprite.rect.bottom
                        plr_sprite.direction.y = 0               
                    
    def run(self):
        #level tiles
        self.tiles.draw(self.display_surface)
        #player
        #self.jump_detect()
        self.horizontal_movement_collision()
        self.vertical_movement_collision()
        
        self.players.update()
        self.players.draw(self.display_surface)

#-------------------------------------------------------------------------------TILES
class Tile(pygame.sprite.Sprite):
    def __init__(self,pos,size):
        super().__init__()
        self.image = pygame.Surface((size,size))
        self.image.fill('white')
        self.rect = self.image.get_rect(topleft = pos)
#-------------------------------------------------------------------------------MAIN
#python setup
pygame.init()
screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()
player = Player(2,2, 1)
player2 = Player(10,10, 2)
players = pygame.sprite.Group()
players.add(player)
players.add(player2)
level = Level(level_map,screen)


while True:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    pygame.quit()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    screen.fill("gray50")
    level.run()
    
    pygame.display.update()
    clock.tick(60)