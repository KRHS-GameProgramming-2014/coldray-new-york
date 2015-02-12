import pygame
from Ball import Ball


class PlayerBall(Ball):
    def __init__(self, pos):
        Ball.__init__(self, "images/Player/BG1.png", [0,0], pos)
        self.upImages = [pygame.image.load("images/Player/BG1.PNG"),
                         pygame.image.load("images/Player/BG2.PNG"),
                         pygame.image.load("images/Player/BG3.PNG")]
                      
        self.downImages = [pygame.image.load("images/Player/mcp1down.PNG"),
                           pygame.image.load("images/Player/mcp2down.PNG"),
                           pygame.image.load("images/Player/mcp3down.PNG")]
                         
        self.leftImages = [pygame.image.load("images/Player/mcp1left.PNG"),
                           pygame.image.load("images/Player/mcp2left.PNG"),
                           pygame.image.load("images/Player/mcp3left.PNG")]
                           
        self.rightImages = [pygame.image.load("images/Player/mcp1right.PNG"),
                            pygame.image.load("images/Player/mcp2right.PNG"),
                            pygame.image.load("images/Player/mcp3right.PNG")]
                            
        self.upPunchImages = [pygame.image.load("images/Player/punchUP.PNG")]
        self.rightPunchImages = [pygame.image.load("images/Player/punchRight.PNG")]
        self.leftPunchImages = [pygame.image.load("images/Player/punchLeft.PNG")]
        self.downPunchImages = [pygame.image.load("images/Player/punchDown.PNG")]
                   
        self.facing = "up"
        self.changed = False
        self.images = self.upImages
        self.frame = 0
        self.maxFrame = len(self.images) - 1
        self.waitCount = 0
        self.maxWait = 60*.25
        self.image = self.images[self.frame]
        self.rect = self.image.get_rect(center = self.rect.center)
        self.maxSpeed = 5
        self.punching = False
        self.punchTime = 0
        self.maxPunchTime = 1*60
            
    def update(self, width, height):
        Ball.update(self, width, height)
        
        if self.punchTime > 0:
            if self.punchTime < self.maxPunchTime:
                self.punchTime += 1
                self.changed = True
            else:
                self.punchTime = 0
                self.punching = False
                self.changed = True
        
        self.animate()
        self.changed = False
        
    def collideEdge(self, width, height):
        if not self.didBounceX:
            print "trying to hit Wall"
            if self.rect.left < 0 or self.rect.right > width:
                self.speedx = 0
                self.didBounceX = True
                print "hit xWall"
        if not self.didBounceY:
            if self.rect.top < 0 or self.rect.bottom > height:
                self.speedy = 0
                self.didBounceY = True
                print "hit xWall"
    
    def collideWall(self, wall):
        if self.rect.right > wall.rect.left and self.rect.left < wall.rect.right:
            if self.rect.bottom > wall.rect.top and self.rect.top < wall.rect.bottom:
                if not self.didBounceX and self.speedx != 0:
                    self.speedx = -self.speedx*2
                    self.move()
                    self.speedx = 0
                    print "x"
                    self.didBouncex = True
                if not self.didBounceY and self.speedy != 0:
                    self.speedy = -self.speedy*2
                    self.move()
                    self.speedy = 0
                    print "y"
                    self.didBounceY = True
                    print "hit Ball"
    
    def animate(self):
        if self.waitCount < self.maxWait:
            self.waitCount += 2
        else:
            self.waitCount = 0
            self.changed = True
            if self.frame < self.maxFrame:
                self.frame += 1
            else:
                self.frame = 0
        
        if self.changed:    
            if self.punching:
                self.maxFrame = len(self.punchUpImages)-1
                if self.facing == "up":
                    self.images = self.upPunchImages
                elif self.facing == "down":
                    self.images = self.downPunchImages
                elif self.facing == "right":
                    self.images = self.rightPunchImages
                elif self.facing == "left":
                    self.images = self.leftPunchImages

            else:
                self.maxFrame = len(self.upImages)-1
                if self.facing == "up":
                    self.images = self.upImages
                elif self.facing == "down":
                    self.images = self.downImages
                elif self.facing == "right":
                    self.images = self.rightImages
                elif self.facing == "left":
                    self.images = self.leftImages   
                
            if self.frame > self.maxFrame:
                self.frame = 0
            print self.frame, self.maxFrame, len(self.images)
            self.image = self.images[self.frame]
            self.rect = self.image.get_rect(center = self.rect.center)

    def punch(self):
       self.punching = True
       self.punchTime = 1
    
    def go(self, direction):
        if direction == "up":
            self.facing = "up"
            self.changed = True
            self.speedy = -self.maxSpeed
        elif direction == "stop up":
            self.speedy = 0
        elif direction == "down":
            self.facing = "down"
            self.changed = True
            self.speedy = self.maxSpeed
        elif direction == "stop down":
            self.speedy = 0
            
        if direction == "right":
            self.facing = "right"
            self.changed = True
            self.speedx = self.maxSpeed
        elif direction == "stop right":
            self.speedx = 0
        elif direction == "left":
            self.facing = "left"
            self.changed = True
            self.speedx = -self.maxSpeed
        elif direction == "stop left":
            self.speedx = 0


