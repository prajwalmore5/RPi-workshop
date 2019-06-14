import pygame
pygame.init()
####yolooooooooooooooooo#####
display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
blue=(0,0,255)
green=(0,255,0)

gameDisplay = pygame.display.set_mode((display_width,display_height))

pygame.draw.rect(gameDisplay, green,[300,400,40,40])
pygame.draw.circle(gameDisplay, red,[200,300],40)
pygame.draw.line(gameDisplay, blue,(100,100),(500,500),10)
pygame.display.update()

