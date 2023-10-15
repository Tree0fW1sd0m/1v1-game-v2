#import pygame, sys 

level_map = [
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
'X                                      X',
'X                                      X',
'X                                      X',
'X                                      X',
'X                                      X',
'X  P                                   X',
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