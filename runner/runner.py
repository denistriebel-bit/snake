import pygame
from sys import exit
from random import randint, choice

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        player_walk_1 = pygame.image.load('runner/graphics/player/player_walk_1.png').convert_alpha()
        player_walk_2 = pygame.image.load('runner/graphics/player/player_walk_2.png').convert_alpha()
        self.player_walk = [player_walk_1, player_walk_2]
        self.player_index = 0
        self.player_jump = pygame.image.load('runner/graphics/player/jump.png').convert_alpha()
        
        self.jump_sound = pygame.mixer.Sound('runner/audio/jump.mp3')
        self.jump_sound.set_volume(0.5)
        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom = (80,300))
        self.gravity = 0
    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.gravity = -20
            self.jump_sound.play()
    def apply_gravity(self):
        self.gravity +=1
        self.rect.y += self.gravity
        if self.rect.bottom > 300: self.rect.bottom = 300
    def player_animation(self):
        if self.rect.bottom < 300:
            self.image = self.player_jump
        else:
            self.player_index +=0.1
            if self.player_index > 2 : self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]
            
    def update(self):
        self.player_input()
        self.apply_gravity()
        self.player_animation()

class Obstacle(pygame.sprite.Sprite):
    def __init__(self,type):
        super().__init__()
        
        if type == 'fly':
            fly_frame1 = pygame.image.load('runner/graphics/fly/Fly1.png').convert_alpha()
            fly_frame2 = pygame.image.load('runner/graphics/fly/Fly2.png').convert_alpha()
            self.frames = [fly_frame1,fly_frame2]
            y_pos = 210
        else:
            snail_frame1 = pygame.image.load('runner/graphics/snail/snail1.png').convert_alpha() #make transparent properly
            snail_frame2 = pygame.image.load('runner/graphics/snail/snail2.png').convert_alpha()
            self.frames = [snail_frame1,snail_frame2]
            y_pos = 300
        
        self.anim_index = 0    
        self.image = self.frames[self.anim_index]
        self.rect = self.image.get_rect(midbottom = (randint(900,1100),y_pos))
    
    def animation(self):
        if self.rect.bottom == 300:
            self.anim_index += 0.1 
        else:
            self.anim_index +=0.2
        if self.anim_index > 2 : self.anim_index = 0
        self.image = self.frames[int(self.anim_index)]
    def update(self):
        self.animation()
        if self.rect.bottom == 300:
            self.rect.x -= 6
        else:
            self.rect.x -= 8
        self.destroy()
    def destroy(self):
        if self.rect.x <= -100:
            self.kill()
        
        
        
def display_score():
    time = int((pygame.time.get_ticks() - start_time) / 1000)
    score_surf = test_font.render(f"Score: {time}", False, (64,64,64))
    score_rect = score_surf.get_rect(center = (400, 50))
    screen.blit(score_surf,score_rect)
    return time

def obstacle_movement(obs_lst):
    if obs_lst: #check if is not empty
        for rect in obs_lst:
            rect.x -= 5
            if rect.bottom == 300:       
                screen.blit(snail_surf,rect)
            else:
                screen.blit(fly_surf,rect)
        obs_lst = [obs for obs in obs_lst if obs.x > -100]
        return obs_lst
    else:
        return []

def collision_detection (player,obs):
    if obs :
        for rect in obs:
            if player.colliderect(rect):
                return False
    return True
def collision_sprite():
    if pygame.sprite.spritecollide(player.sprite, obs_group, False): #boolean if we want delete from obs gorup after collision
        obs_group.empty()
        return False
    else:
        return True


    
#system variables
pygame.init() #necesarry

screen = pygame.display.set_mode((800, 400)) #define window, width and height in tuple
pygame.display.set_caption(f"runner") #set caption of window
clock = pygame.time.Clock()
mouse_pos = (0,0)
game_active = False
start_time = 0
score = 0
bg_music = pygame.mixer.Sound("runner/audio/music.wav")
bg_music.set_volume(0.1)
bg_music.play(loops = -1)

player = pygame.sprite.GroupSingle()
player.add(Player())

obs_group = pygame.sprite.Group()


#texts
test_font = pygame.font.Font("runner/font/Pixeltype.ttf", 50) #1, need define font, size

sky_surface = pygame.image.load('runner/graphics/sky.png').convert() #converts image to more easy for py
ground_surface = pygame.image.load('runner/graphics/ground.png').convert()

 
#intro screen
player_stand = pygame.image.load('runner/graphics/player/player_stand.png').convert_alpha() 
player_stand = pygame.transform.scale2x(player_stand)
player_stand_rect = player_stand.get_rect(center =(400,200))

mtext_surf = test_font.render(("PRESS SPACE TO START"),False,("#2a2b2c"))
mtext_rect = mtext_surf.get_rect(center =(400, 350))

mtitle_surf = test_font.render(("BITRUNNER!"),False,("#2a2b2c"))
mtitle_rect = mtitle_surf.get_rect(center =(400, 50))

#timer
obstacle_timer = pygame.USEREVENT + 1 
pygame.time.set_timer(obstacle_timer,1500)
snail_anim_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_anim_timer,500)
fly_anim_timer = pygame.USEREVENT +3
pygame.time.set_timer(fly_anim_timer,200)


while True:
    #manage exit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() #is opposit to init
            exit() #imported from sys to end program correctly
        if game_active:   
            if event.type == pygame.MOUSEBUTTONDOWN:
                ...
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_active = True 
                    start_time = pygame.time.get_ticks()
        if game_active:
            if event.type == obstacle_timer:
                obs_group.add(Obstacle(choice(['fly', 'snail', 'snail',])))
                
    
    if game_active:            
        screen.blit(sky_surface,(0,0))
        screen.blit(ground_surface,(0,300))

        score = display_score()
        
        player.draw(screen)  
        player.update()
        
        obs_group.draw(screen)
        obs_group.update()   
        
        game_active = collision_sprite()
        
    else:
        screen.fill((94,129,162))
        screen.blit(player_stand,player_stand_rect)
        
        score_msg = test_font.render(f'Your score:{score}',False,("#2a2b2c"))
        score_msg_rect = score_msg.get_rect(center = (400, 350))
        obstacle_rect_lst = []
        
        player_grav = 0
        
        if score > 0 :
            screen.blit(score_msg, score_msg_rect)
        else:    
            screen.blit(mtext_surf,mtext_rect)
        screen.blit (mtitle_surf,mtitle_rect)
    

    
    pygame.display.update() # update the window with drawn elements, is necessary
    clock.tick(60) #while loop will run 60x in 1 second
    
    
    # https://youtu.be/AY9MnQ4x3zk?t=11591