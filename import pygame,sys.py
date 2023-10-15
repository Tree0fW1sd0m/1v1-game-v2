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
optionp1 = 1
optionp2 = 1
game_beginp1 = False
game_beginp2 = False

while game_beginp1 == False and game_beginp2 == False:
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
            
            
            
#-------------------------------------------------------------------------------SETTINGS
level_map = [
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
'X                                      X',
'X                                      X',
'X                                      X',
'X                                      X',
'X                                      X',
'X  P                                T  X',
'X          XXXXXXXXXXXXXXXXX           X',
'X                                      X',
'X                                      X',
'X                                      X',
'X                                      X',
'X                                      X',
'XXXXXXXXXXXXXXXX       XXXXXXXXXXXXXXXXX',
'X                                      X',
'X                                      X',
'X                                      X',
'X                                      X',
'X                                      X',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',]
    
tile_size = 32
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
        self.image.fill('black')
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
                image_to_load = pygame.image.load('1v1 game v2/sprites/zuko.png')
                self.speed = 8
            elif optionp1 == 2:
                image_to_load = pygame.image.load('1v1 game v2/sprites/katara.png')
                self.speed = 7
            elif optionp1 == 3:
                image_to_load = pygame.image.load('1v1 game v2/sprites/aang.png')
                self.speed = 10
            elif optionp1 == 4:
                image_to_load = pygame.image.load('1v1 game v2/sprites/toph.png')
                self.speed = 6
            elif optionp1 == 5:
                image_to_load = pygame.image.load('1v1 game v2/sprites/sokka.png')
                self.speed = 9
            self.image.blit(image_to_load,(0,0))
        elif plr_num == 2:
            if optionp2 == 1:
                image_to_load = pygame.image.load('1v1 game v2/sprites/zuko_frame2.png')
                self.speed = 8
            elif optionp2 == 2:
                image_to_load = pygame.image.load('1v1 game v2/sprites/katara_frame2.png')
                self.speed = 7
            elif optionp2 == 3:
                image_to_load = pygame.image.load('1v1 game v2/sprites/aang_frame2.png')
                self.speed = 10
            elif optionp2 == 4:
                image_to_load = pygame.image.load('1v1 game v2/sprites/toph_frame2.png')
                self.speed = 6
            elif optionp2 == 5:
                image_to_load = pygame.image.load('1v1 game v2/sprites/sokka_frame2.png')
                self.speed = 9
            self.image.blit(image_to_load,(0,0))
        self.image.set_colorkey('black')
        
    def get_input(self):
        keys = pygame.key.get_pressed()
        
        if self.plr_num == 1:
            if keys[pygame.K_a]:
                self.direction.x = -1
                if optionp1 == 1:
                    image_to_load = pygame.image.load('1v1 game v2/sprites/zuko_frame2.png')
                elif optionp1 == 2:
                    image_to_load = pygame.image.load('1v1 game v2/sprites/katara_frame2.png')
                elif optionp1 == 3:
                    image_to_load = pygame.image.load('1v1 game v2/sprites/aang_frame2.png')
                elif optionp1 == 4:
                    image_to_load = pygame.image.load('1v1 game v2/sprites/toph_frame2.png')
                elif optionp1 == 5:
                    image_to_load = pygame.image.load('1v1 game v2/sprites/sokka_frame2.png')
                self.image.blit(image_to_load,(0,0))
            elif keys[pygame.K_d]:
                self.direction.x = 1
                if optionp1 == 1:
                    image_to_load = pygame.image.load('1v1 game v2/sprites/zuko.png')
                elif optionp1 == 2:
                    image_to_load = pygame.image.load('1v1 game v2/sprites/katara.png')
                elif optionp1 == 3:
                    image_to_load = pygame.image.load('1v1 game v2/sprites/aang.png')
                elif optionp1 == 4:
                    image_to_load = pygame.image.load('1v1 game v2/sprites/toph.png')
                elif optionp1 == 5:
                    image_to_load = pygame.image.load('1v1 game v2/sprites/sokka.png')
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
                    image_to_load = pygame.image.load('1v1 game v2/sprites/zuko_frame2.png')
                elif optionp2 == 2:
                    image_to_load = pygame.image.load('1v1 game v2/sprites/katara_frame2.png')
                elif optionp2 == 3:
                    image_to_load = pygame.image.load('1v1 game v2/sprites/aang_frame2.png')
                elif optionp2 == 4:
                    image_to_load = pygame.image.load('1v1 game v2/sprites/toph_frame2.png')
                elif optionp2 == 5:
                    image_to_load = pygame.image.load('1v1 game v2/sprites/sokka_frame2.png')
                self.image.blit(image_to_load,(0,0))
            elif keys[pygame.K_RIGHT]:
                self.direction.x = 1
                if optionp2 == 1:
                    image_to_load = pygame.image.load('1v1 game v2/sprites/zuko.png')
                elif optionp2 == 2:
                    image_to_load = pygame.image.load('1v1 game v2/sprites/katara.png')
                elif optionp2 == 3:
                    image_to_load = pygame.image.load('1v1 game v2/sprites/aang.png')
                elif optionp2 == 4:
                    image_to_load = pygame.image.load('1v1 game v2/sprites/toph.png')
                elif optionp2 == 5:
                    image_to_load = pygame.image.load('1v1 game v2/sprites/sokka.png')
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
            
    screen.fill("black")
    level.run()
    
    pygame.display.update()
    clock.tick(60)