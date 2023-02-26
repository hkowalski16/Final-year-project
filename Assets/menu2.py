import pygame
from pygame.locals import *
import sys
import pygame_menu
from pygame_menu import *
import os
pygame.init()
pygame.font.init()
pygame.font.get_fonts()

"""PATH = os.path.join(os.path.dirname(pygame_menu.__file__),
                    'resources', 'images', 'pygame_menu.png')"""

#screen dimensions
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

#drawing the main menu
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Hacker simulator")
mainmenu = pygame_menu.Menu('Hacker simulator',  1280, 720, theme=pygame_menu.themes.THEME_DARK,)

#Level select sub-menu
def level_select():
    mainmenu._open(level)

#level select menu + buttons
level = pygame_menu.Menu('Pick a level', 1280, 720,theme=pygame_menu.themes.THEME_DARK)    

gameisplaying = False

level1button = level.add.button('Level 1', font_color = (0, 235, 21))
level2button = level.add.button('Level 2', font_color = (0, 235, 21))
level3button = level.add.button('Level 3', font_color = (0, 235, 21))

#Instructions sub-menu
def instructions_page():
    mainmenu._open(instructions)

HELP = "Press level select to pick a level, " \
    "this is still a WIP"

instructions = pygame_menu.Menu('Instructions', 1280,720, theme=pygame_menu.themes.THEME_DARK)
instructions.add.label(HELP, max_char=-1,font_color = (0, 235, 21), font_size=30)

def options_page():
    mainmenu._open(options)

options = pygame_menu.Menu('Options', 1280, 720, theme=pygame_menu.themes.THEME_DARK)
options.add.selector('Audio:', [('On', 1), ('Off', 2)], font_color = (0, 235, 21))

#buttons
level_select_menu = mainmenu.add.button('Level select',  level_select, font_color = (0, 235, 21))
instructions_menu = mainmenu.add.button('Instructions', instructions_page, font_color = (0, 235, 21))
options_menu = mainmenu.add.button('Options', options_page, font_color = (0, 235, 21))
exit_button = mainmenu.add.button('Quit', pygame_menu.events.EXIT, font_color = (0, 235, 21))

#Maps

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()
 
    if mainmenu.is_enabled():
        mainmenu.update(events)
        mainmenu.draw(screen)
 
    pygame.display.update()

while gameisplaying:
    screen.blit(level1)
    pygame.display.flip(level)


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


