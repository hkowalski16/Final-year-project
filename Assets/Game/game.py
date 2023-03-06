import pygame
import sys
import os
import time
import random
from os import *
pygame.init()
pygame.font.init()
pygame.font.get_fonts()

virus_names = ["spyware", "ransomware", "malware"]

screen = pygame.display.set_mode((1280, 720))

level1Image = pygame.image.load("level_1.png")

#game class
class game:
    def __init__(self):
        self.width = 1280
        self.height = 720
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.viruses = []
        self.anti_viruses = []
        self.money = 100
        self.background = pygame.image.load("level_1.png")
        #self.clicks = [] #remove later


    def run(self):
        run = True
        fps = pygame.time.Clock()
        while run:
            fps.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                #pos = pygame.mouse.get_pos()

                #if event.type == pygame.MOUSEBUTTONDOWN:
                    #print(pos)    

            self.draw()        

    def draw(self):
        self.screen.blit(self.background, (0,0))
        #for p in self.clicks:
            #pygame.draw.circle(self.screen, (255,0,0), (p[0], p[1]), 5)
        pygame.display.update()
        

#base virus class
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

    #def move(self):

    def hit(self):
        self.health -=1
        if self.health <=0:
            return True

    def run(self):
        run = True
        fps = pygame.time.Clock()
        while run:
            fps.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                pos = pygame.mouse.get_pos()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.clicks.append(pos)
                    print(pos)

            self.draw()        


        pygame.quit()            

    def draw(self):
        self.screen.blit(self.background, (0,0))
        #for p in self.clicks:
            #pygame.draw.circle(self.win, (255,0,0), (p[1], 5, 0))
        pygame.display.update()

g = game()
g.run()