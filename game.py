import pygame,os
import sys
fps = 30
fpscontroller = pygame.time.Clock()
pygame.display.set_caption('Hill Climb Racing')
# pygame.display.set_caption(title, icontitle=None)
width = 700
height = 500
game_window = pygame.display.set_mode((width,height))

keepPlaying = True

pygame.init()
red = pygame.Color(255,0,0)

while True:
    game_window.fill(red)
    fpscontroller.tick(fps)
    pygame.display.update()
