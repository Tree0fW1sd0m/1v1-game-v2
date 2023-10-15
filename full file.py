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
    def __init__(self,pos):
        super().__init__()
        self.image = pygame.Surface((64,64))
        self.image.fill('red')
        self.rect = self.image.get_rect(topleft = pos)
    
        #player movement
        self.direction = pygame.math.Vector2(0,0)
        self.speed = 1
        self.gravity = 0.8
        self.jump_speed = -1
        
        image_to_load = pygame.image.load('1v1 game v2/sprites/zuko.png')
        self.image.blit(image_to_load,(0,0))
        self.image.set_colorkey('red')
        
            
        
    def get_input(self):
        keys = pygame.key.get_pressed()
        
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
            
        if keys[pygame.K_w]:
            self.jump()

            
                
            
    def apply_gravity(self):
        self.direction.y+= self.gravity
        self.rect.y += self.direction.y
         
    def jump(self):
        self.direction.y += jump_height
          


            
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
        self.player = pygame.sprite.GroupSingle()
        self.player2 = pygame.sprite.GroupSingle()
        
        for row_index,row in enumerate(layout):
            for col_index,cell in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size
                if cell == 'X':
                    tile = Tile((x,y),tile_size)
                    self.tiles.add(tile)
                if cell == 'P':
                    player_sprite = Player((x,y))
                    self.player.add(player_sprite)
                if cell == "T":
                    player2_sprite = Player((x,y))
                    self.player.add(player2_sprite)
                    
    def horizontal_movement_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x*player.speed
        
        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left
    
    def vertical_movement_collision(self):
        player = self.player.sprite
        player.apply_gravity()
        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0


    def horizontal_movement_collision2(self2):
        player = self2.player.sprite
        player.rect.x += player.direction.x*player.speed
        
        for sprite in self2.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left
    
    def vertical_movement_collision2(self2):
        player = self2.player.sprite
        player.apply_gravity()
        for sprite in self2.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
                    
                    
                    
                    
    def run(self):
        #level tiles
        self.tiles.draw(self.display_surface)
        #player
        self.player.update()
        self.player2.update()
        #self.jump_detect()
        self.horizontal_movement_collision()
        self.vertical_movement_collision()
        self.player.draw(self.display_surface)
        self.horizontal_movement_collision2()
        self.vertical_movement_collision2()
        self.player2.draw(self.display_surface)
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
level = Level(level_map,screen)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    screen.fill("black")
    level.run()
    
    pygame.display.update()
    clock.tick(60)