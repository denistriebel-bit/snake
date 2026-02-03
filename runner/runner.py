import pygame
from sys import exit

#system variables
pygame.init() #necesarry
screen = pygame.display.set_mode((800, 400)) #define window, width and height in tuple
pygame.display.set_caption("Runner") #set caption of window
clock = pygame.time.Clock()

#variables
sky_surface = pygame.image.load('runner/graphics/sky.png')

while True:
    #manage exit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() #is opposit to init
            exit() #imported from sys to end program correctly
    
    #drawing
    screen.blit(sky_surface,(200,100))
    #updating
    
    pygame.display.update() # update the window with drawn elements, is necessary
    clock.tick(60) #while loop will run 60x in 1 second