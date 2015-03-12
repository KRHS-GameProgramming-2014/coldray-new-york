#code from Kevin, Jacob, Phillip
#https://code.google.com/p/butterfly-game1/

import pygame,math,sys,random

class HealthBar():
    def __init__(self, position):
        self.surfaces = []
        self.surfaces += [pygame.image.load("0health/Health/0%.png")]
        self.surfaces += [pygame.image.load("10health/Health/10%.png")]
        self.surfaces += [pygame.image.load("25health/Health/25%.png")]
        self.surfaces += [pygame.image.load("40health/Health/40%.png")]
        self.surfaces += [pygame.image.load("55health/Health/55%.png")]
        self.surfaces += [pygame.image.load("70health/Health/70%.png")]
        self.surfaces += [pygame.image.load("85health/Health/85%.png")]
        self.surfaces += [pygame.image.load("100health/Health/100%1.png")]
        self.maxFrame = len(self.surfaces)-1
#        self.surface = pygame.transform.scale(self.faces,(100,25))
        self.frame = self.maxFrame
        self.surface = self.surfaces[self.frame]
        self.rect = self.surface.get_rect()
        self.rect.center = position
        #if pygame.mixer:
        #    self.healthSound = pygame.mixer.Sound("health.wav")
        
       
    def  __str__(self):
        return "I'm a Health Bar " + str(self.rect.center) + str(self.speed) + str(self.living)
     
    def health_bar(self):
        pass
            
    def update(self, life, maxLife):
        percentLife = float(life)/float(maxLife)
        if percentLife > .95:
            self.frame = 19
            print percentLife
        elif percentLife > .90:
            self.frame = 18
            print percentLife
        elif percentLife > .85:
            self.frame = 17
            print percentLife
        elif percentLife > .80:
            self.frame = 16
            print percentLife
        elif percentLife > .75:
            self.frame = 15
            print percentLife
        elif percentLife > .70:
            self.frame = 14
            print percentLife
        elif percentLife > .65:
            self.frame = 13
            print percentLife
        elif percentLife > .60:
            self.frame = 12
            print percentLife
        elif percentLife > .50:
            self.frame = 11
            print percentLife
        elif percentLife > .45:
            self.frame = 10
            print percentLife
        elif percentLife > .40:
            self.frame = 9
            print percentLife
        elif percentLife > .35:
            self.frame = 8
            print percentLife
        elif percentLife > .30:
            self.frame = 7
            print percentLife
        elif percentLife > .25:
            self.frame = 6
            print percentLife
        elif percentLife > .20:
            self.frame = 5
            print percentLife
        elif percentLife > .15:
            self.frame = 4
            print percentLife
        elif percentLife > .10:
            self.frame = 3
            print percentLife
        elif percentLife > .5:
            self.frame = 2
            print percentLife
        elif percentLife > .1:
            self.frame = 1
            print percentLife
        else:
            self.frame = 0
            print percentLife
            self.living = False
        self.surface = self.surfaces[self.frame]