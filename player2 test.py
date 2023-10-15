import pygame

player_size = 20
player2_size = 20
jump_height = -4.5
jump2_height = -4.5
class Player(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.image = pygame.Surface((64,64))
        self.image.fill('red')
        self.rect = self.image.get_rect(topleft = pos)
    
        #player movement
        self.direction = pygame.math.Vector2(0,0)
        self.speed = 8
        self.gravity = 0.8
        self.jump_speed = -1
        
        image_to_load = pygame.image.load('1v1 game v2/sprites/zuko.png')
        self.image.blit(image_to_load,(0,0))
        self.image.set_colorkey('red')
        
        
class Player2(pygame.sprite.Sprite):
    def __init__(self2,pos):
        super().__init__()
        self2.image = pygame.Surface((64,64))
        self2.image.fill('red')
        self2.rect = self2.image.get_rect(topleft = pos)
    
        #player movement
        self2.direction = pygame.math.Vector2(0,0)
        self2.speed = 8
        self2.gravity = 0.8
        self2.jump_speed = -1
        
        image_to_load = pygame.image.load('1v1 game v2/sprites/zuko.png')
        self2.image.blit(image_to_load,(0,0))
        self2.image.set_colorkey('red')
        
            
        
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
            
    def get_input2(self2):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LEFT]:
            self2.direction.x = -1
            image_to_load = pygame.image.load('1v1 game v2/sprites/zuko_frame2.png')
            self2.image.blit(image_to_load,(0,0))
        elif keys[pygame.K_RIGHT]:
            self2.direction.x = 1
            image_to_load = pygame.image.load('1v1 game v2/sprites/zuko.png')
            self2.image.blit(image_to_load,(0,0))
        else:
            self2.direction.x = 0
            
        if keys[pygame.K_UP]:
            self2.jump()

            
                
            
    def apply_gravity(self):
        self.direction.y+= self.gravity
        self.rect.y += self.direction.y
         
    def jump(self):
        self.direction.y += jump_height
            
    def update(self):
        self.get_input()
        
    def apply_gravity(self2):
        self2.direction.y+= self2.gravity
        self2.rect.y += self2.direction.y
         
    def jump(self2):
        self2.direction.y += jump_height
            
    def update(self2):
        self2.get_input()
