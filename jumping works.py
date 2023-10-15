import pygame, sys
import random

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
    def __init__(self,x,y, plr_num):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((64,64))
        self.image.fill('black')
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        
        self.plr_num = plr_num
    
        #player movement
        self.direction = pygame.math.Vector2(0,0)
        self.gravity = 0.8
        self.jump_speed = -1
        
        self.jumping = False
          
        if self.plr_num == 1:
            image_to_load = pygame.image.load('1v1 game v2/sprites/zuko.png')
            self.speed = 6
        elif self.plr_num == 2:
            image_to_load = pygame.image.load('1v1 game v2/sprites/katara_frame2.png')
            self.speed = 10
        self.image.blit(image_to_load,(0,0))
        self.image.set_colorkey('black')
        
    def get_input(self):
        keys = pygame.key.get_pressed()
        
        if self.plr_num == 1:
            if keys[pygame.K_a]:
                self.direction.x = -1
                image_to_load = pygame.image.load('1v1 game v2/sprites/zuko_frame2.png')
                self.image.blit(image_to_load,(0,0))
            elif keys[pygame.K_d]:
                self.direction.x = 1
                image_to_load = pygame.image.load('1v1 game v2/sprites/zuko.png')
                self.image.blit(image_to_load,(0,0))
            else:
                self.direction.x = 0
                
            if keys[pygame.K_w] and not self.jumping:
                self.jumping = True
                self.jump()
                
        elif self.plr_num == 2:
            if keys[pygame.K_LEFT]:
                self.direction.x = -1
                image_to_load = pygame.image.load('1v1 game v2/sprites/katara_frame2.png')
                self.image.blit(image_to_load,(0,0))
            elif keys[pygame.K_RIGHT]:
                self.direction.x = 1
                image_to_load = pygame.image.load('1v1 game v2/sprites/katara.png')
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