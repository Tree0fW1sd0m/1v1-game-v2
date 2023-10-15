import pygame, random

class Player(pygame.sprite.Sprite):
    def __init__(self,col,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((64,64))
        self.image.fill(col)
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

class Playertwo(pygame.sprite.Sprite):
    def __init__(self,col,x,y):
        super().__init__()
        self.image = pygame.Surface((64,64))
        self.image.fill(col)
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        
player = Player("red",100,100)
player2 = Playertwo("green",0,0)
players = pygame.sprite.Group()
players.add(player)
players.add(player2)
print(players)
