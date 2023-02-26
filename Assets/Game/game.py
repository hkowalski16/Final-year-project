import pygame
import sys
import os
from os import *
pygame.init()
pygame.font.init()
pygame.font.get_fonts()

class game:
    def __init__(self):
        self.width = 1280
        self.height = 720
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.viruses = []
        self.anti_viruses = []
        self.money = 100
        self.background = pygame.image.load(os.path.join("Game", "level_1.png"))
        

class virus: 
    images = []

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.health = 1
        self.path = []
        self.image = None

    def draw(self, screen):
        self.virus_type +=1
        self.image = self.images[self.virus_type]
        screen.blit(self.image, (self.x, self.y))
        self.move()
        

    def collide (self,x, y):
        if x <= self.x + self.width and x >= self.x:
            if y <= self.y + self.height and y >= self.y:
                return True
        return False

    def move(self):

    def hit(self):
        self.health -=1
        if self.health <=0:
            return True
    




#setting screen dimensions
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


#loading in the assets
level1 = pygame.image.load('level_1.png')
level1Path = r'C:\Users\Harry\Documents\Computer science\Final year project\Assets\Game'

#drawing window
def draw():
    screen.fill([0,0,0])
    screen.blit(level1,[0,0])



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        
    draw()
    pygame.display.update()

