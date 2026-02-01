
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
speed = 500



player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
apple_coord = random_coord(screen_size)


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("grey")
    font = pygame.font.Font(None, 32)
    ppos = font.render(f"x: {int(player_pos.x)} y: {int(player_pos.y)}", True, (10,10,10))
    #write texts
    screen.blit(ppos, (10,10))  
    #draw objects
    pygame.draw.rect(screen, "red", (player_pos.x, player_pos.y,10,10))
    pygame.draw.circle(screen, "blue", apple_coord, 5)
    
    #movement player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        dir = "up"
    if keys[pygame.K_s]:
        dir = "down"
    if keys[pygame.K_a]:
        dir = "left"
    if keys[pygame.K_d]:
        dir = "right"
    player_pos = move_step(dir,player_pos, (screen.get_height(), screen.get_height()), speed, dt)
    
    #eat/respawn apple
    
    
    
   
   
   
   
    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()