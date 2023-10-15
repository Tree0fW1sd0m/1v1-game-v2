import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))

clock = pygame.time.Clock()
running = True

player_rect = pygame.Rect(screen.get_width()/2, (screen.get_height()*.9)-100,20,20)
ground_rect = pygame.Rect(0, screen.get_height()*.90,screen.get_width(),screen.get_height()*.10)
platform_rect = pygame.Rect(0, screen.get_height()*.10,screen.get_width(),screen.get_height()*.01)
platform2_rect = pygame.Rect(0, screen.get_height()*.10,screen.get_width(),screen.get_height()*.01)

gravity = 4

dt = 0

# Stores if player is jumping or not
isjump = False
   
# Force (v) up and mass m.
v = 7
m = 1

jump_delay = 0
seconds = 0

player_pos = pygame.Vector2(screen.get_width()/2, (screen.get_height()*.9)-100)
platform_pos = pygame.Vector2(screen.get_width(), screen.get_height())
platform2_pos = pygame.Vector2(screen.get_width(), screen.get_height())

def run_game():
    global running, player_rect, ground_rect, platform_rect, platform2_rect, gravity, dt, player_pos, isjump, v, m, seconds, jump_delay 
    while running:
        keys = pygame.key.get_pressed()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                
        screen.fill("white")
        
        collide = pygame.Rect.colliderect(ground_rect, player_rect)
        collide2 = pygame.Rect.colliderect(platform_rect, player_rect)
        collide3 = pygame.Rect.colliderect(platform2_rect, player_rect)
        
        #if not collide or not collide2:
         #   player_pos.y += gravity
            #gravity = 4
        
        if collide:
            gravity = 0
            player_rect.bottom = ground_rect.top
            player_pos.y = player_rect.bottom-10
            
         
        
        if collide2:
            gravity = 4
            player_rect.bottom = platform_rect.top
            player_pos.y = player_rect.bottom-10
            #player_pos.y-10
        
           
        if collide3:
            #gravity = 0
            player_rect.bottom = platform2_rect.top
            player_pos.y = player_rect.bottom-10
            
        
        player_rect = pygame.Rect(player_pos.x-200, player_pos.y-10, 20, 20)
        platform_rect = pygame.Rect(platform_pos.x-800, platform_pos.y-125,250, 10)
        platform2_rect = pygame.Rect(platform_pos.x-500, platform_pos.y-160,100, 60)
        
        pygame.draw.rect(screen, "blue", player_rect)
        pygame.draw.rect(screen,"green",ground_rect)
        pygame.draw.rect(screen,"red",platform_rect)
        pygame.draw.rect(screen,"purple",platform2_rect)
                
        if keys[pygame.K_a]:
            player_pos.x -= 300 * dt
        if keys[pygame.K_d]:
            player_pos.x += 300 * dt
        if keys[pygame.K_s]:
            player_pos.y += 300 * dt
            
        if isjump == False:
            seconds = (pygame.time.get_ticks()-jump_delay)
            
            if seconds >= 400:
            # if w is pressed
                if keys[pygame.K_w]:
                    jump_delay = pygame.time.get_ticks()
                    # make isjump equal to True
                    isjump = True
                    
                
        if isjump :
            # calculate force (F). F = 1 / 2 * mass * velocity ^ 2.
            F =(1 / 2)*m*(v**2)
            
            # change in the y co-ordinate
            player_pos.y -= F
            #while not collide:
            #    player_pos.y -= F
            
            # decreasing velocity while going up and become negative while coming down
            v = v-1
            
            # object reached its maximum height
            if v<0:
                
                # negative sign is added to counter negative velocity
                m =-1
    
            # objected reaches its original state
            if collide or collide2 or collide3:
    
                # making isjump equal to false 
                isjump = False
    
        
                # setting original values to v and m
                v = 7
                m = 1
                    
        # flip() the display to put your work on screen
        pygame.display.flip()

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(60) / 1000
        
run_game()