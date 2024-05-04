import pygame
import os
from random import choice
from random import randrange

pygame.init()
os.environ['SDL_VIDEO_CENTERED'] = '1'#this will center the screen
resolution = (800, 600)

font_height = 35

Katakana = ['ｦ', 'ｱ', 'ｳ', 'ｴ', 'ｵ', 'ｶ', 'ｷ', 'ｹ', 'ｺ', 'ｻ', 'ｼ', 'ｽ', 
            'ｾ', 'ｿ', 'ﾀ', 'ﾂ', 'ﾃ', 'ﾅ', 'ﾆ', 'ﾇ', 'ﾈ',
          'ﾊ', 'ﾋ', 'ﾎ', 'ﾏ', 'ﾐ', 'ﾑ', 'ﾒ', 'ﾓ', 'ﾔ', 'ﾕ', 'ﾗ', 'ﾘ', 'ﾜ', '日']
font = pygame.font.Font('font/ms mincho.ttf', font_height)
green_symbols = [font.render(char, True, (0, 255, 0)) for char in Katakana] #will make the katakana green.

screen = pygame.display.set_mode(resolution)
clock = pygame.time.Clock()
show_surface = pygame.Surface(resolution)#will use this to show the surface of my resolution.

class Symbol:
       

running = True
while running: 
     show_surface.fill(pygame.Color(0, 0, 0 ))
     screen.blit(show_surface, (0, 0))

     pygame.display.update()

     clock.tick(60)
    



for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 
















