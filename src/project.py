import pygame
import os
from random import choice
from random import randrange
def main():
     pygame.init()
     os.environ['SDL_VIDEO_CENTERED'] = '1'#this will center the screen
     width = 800
     height = 600
     resolution = (width, height)

     font_height = 35

     Katakana = ['ｦ', 'ｱ', 'ｳ', 'ｴ', 'ｵ', 'ｶ', 'ｷ', 'ｹ', 'ｺ', 'ｻ', 'ｼ', 'ｽ', 
               'ｾ', 'ｿ', 'ﾀ', 'ﾂ', 'ﾃ', 'ﾅ', 'ﾆ', 'ﾇ', 'ﾈ',
               'ﾊ', 'ﾋ', 'ﾎ', 'ﾏ', 'ﾐ', 'ﾑ', 'ﾒ', 'ﾓ', 'ﾔ', 'ﾕ', 'ﾗ', 'ﾘ', 'ﾜ', '日']

     trail = randrange(30, 40, 5) 
     #will use the trial to change the aplphas of the katakana using a new display changing the alphas
     font = pygame.font.Font('font/HinaMincho-Regular.ttf', font_height)
     green_symbols = [font.render(char, True, (0, 255, 0)) for char in Katakana] 

     screen = pygame.display.set_mode(resolution)
     clock = pygame.time.Clock()
     show_surface = pygame.Surface(resolution)#will use this to show the surface of my resolution.
     show_surface.set_alpha(trail)

     class Symbol:
          #to display symbol class.
          def __init__(self, x, y):#x and y coordinatea
               self.x = x
               self.y = y
               self.speed = 25 #how fast it moves on the y coordinate.
               self.value = choice(green_symbols)
          def draw(self):
               self.value = choice(green_symbols)
               self.y = self.y + self.speed if self.y < height else -font_height * randrange(1, 10) #This is so when the symbol falls to the bottom of the screen it will appear back to the top at a random point on the x coordinate. 
               screen.blit(self.value, (self.x, self.y)) #blink at defindes coordinates


     symbols = [Symbol(x, randrange(-height, 0))for x in range(0, width, font_height)] 
     #This will generate symbols for window width at random
               
          
          

     running = True
     while running: 
          screen.blit(show_surface, (0, 0))
          show_surface.fill(pygame.Color('black'))
          [symbol.draw() for symbol in symbols]

          pygame.display.update()

          clock.tick(60)
     



     for event in pygame.event.get():
               if event.type == pygame.QUIT:
                    running = False 


if __name__ == "__main__":
    main()













