
# Example file showing a circle moving on screen
import pygame
from tools import move_step, random_coord
# pygame setup
pygame.init()
screen_size = 640
screen = pygame.display.set_mode((screen_size, screen_size))
clock = pygame.time.Clock()
running = True

dt = 0
speed = 300
score = 0
tcoord = []
dir = "up"



player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
apple_coord = random_coord(screen_size)
ppos = (int(player_pos.x), int(player_pos.y))


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("grey")
    font = pygame.font.Font(None, 32)
    ppos_info = font.render(f"x: {int(player_pos.x)} y: {int(player_pos.y)} score: {score}", True, (10,10,10))
    #write texts
    screen.blit(ppos_info, (10,10))  
    #draw objects
    
    head = pygame.Rect(0,0,10,10)
    head.center = ppos
    pygame.draw.rect(screen, "red", head)
    
    for i in range(score):
        tail = pygame.Rect(0,0,10,10)
        tail.center = tcoord[i]
        pygame.draw.rect(screen, "green", tail)
    
    pygame.draw.circle(screen, "blue", apple_coord, 5)
    
    #movement player
    keys = pygame.key.get_pressed()
     
    if keys[pygame.K_w] and dir != "down" and ppos[0] != mem_pos[0]:
        dir = "up"
    if keys[pygame.K_s] and dir != "up" and ppos[0] != mem_pos[0]:
        dir = "down"
    if keys[pygame.K_a] and dir != "rigt" and ppos[1] != mem_pos[1]:
        dir = "left"
    if keys[pygame.K_d] and dir != "left" and ppos[1] != mem_pos[1]:
        dir = "right"
    mem_pos = ppos
    player_pos = move_step(dir,player_pos, (screen.get_height(), screen.get_height()), speed, dt)
    
    #tail mem
    ppos = (player_pos.x, player_pos.y)
    if ppos not in tcoord:
        tcoord.append(ppos)
    if len(tcoord) > score+1:
        tcoord.pop(0)
    
    #eat/respawn apple
    if ppos == apple_coord :
        score +=1        
        apple_coord = random_coord(screen_size)
        while apple_coord in tcoord:
            apple_coord = random_coord(screen_size) #dont spawn inside tail
        
    #detect collision, game over
    if ppos in tcoord and tcoord.index(ppos) != len(tcoord)-1:
        break
        

    pygame.display.flip()
    dt = clock.tick(30) / 1000

pygame.quit()