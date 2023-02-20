import pygame
from pygame.locals import *
import sys
import pygame_menu
from pygame_menu import themes
pygame.init()

#screen dimensions
hackerTheme = pygame.menu.themes.Theme(color_opaque = (0,0,0),
title_shadow = False,
title_background_color = (0,0,0)
font = pygame_menu.font.FONT_MUNRO)


SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Hacker simulator")
mainmenu = pygame_menu.Menu('Hacker simulator', 1280, 720, theme=pygame_menu.themes.THEME_DARK)
instructions_menu = mainmenu.add.button('Instructions')
level_select_menu = mainmenu.add.button('Level select')
options_menu = mainmenu.add.button('Options')

mainmenu.mainloop(screen)

#font
TEXT_COL = (75,139,59)
font = pygame.font.SysFont("ocr a extended", 40) 

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

instructionsImage = pygame.image.load('instructions.png')
optionsImage = pygame.image.load('options menu.png')

def instructionsmenu(x,y):
    screen.blit(instructionsImage, (x,y))

def optionsmenu(x,y):
    screen.blit(optionsImage, (x,y))


#game loop
run = True
while run:
    mainmenu(0,0)

    pygame.quit()