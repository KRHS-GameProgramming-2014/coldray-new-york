import pygame, sys, random
from HUD import *
from Ball import Ball
from PlayerBall import PlayerBall
from HUD import Text
from HUD import Score
from Button import Button


pygame.init()
  
clock = pygame.time.Clock()


width = 955
height = 610
size = width, height
screen = pygame.display.set_mode(size)

bgColor = r,g,b = 100, 30, 234
bgI = pygame.image.load("images\map2.png")
bgR = bgI.get_rect()
bgImage = pygame.image.load("images/Screens/damian.png").convert()
bgRect = bgImage.get_rect()


player1 = PlayerBall(1, [width/3, height/3])
player2 = PlayerBall(2, [2*width/3, 2*height/3])

balls = []
balls += [Ball("images/Ball/crabman.png", [4,5], [100, 125])]
 
title = Text([height/4, width/8], "Hello HUD!!", 20)

run = False

startButton = Button([width/2, height-300], 
                                     "images/Button/oobi.png", 
                                     "images/Button/oobi.png")

while True:
        while not run:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT: sys.exit()
                        if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_RETURN:
                                        run = True
                        if event.type == pygame.MOUSEBUTTONDOWN:
                                startButton.click(event.pos)
                        if event.type == pygame.MOUSEBUTTONUP:
                                if startButton.release(event.pos):
                                        run = True
                                        
                bgColor = r,g,b
                screen.fill(bgColor)
                screen.blit(bgImage, bgRect)
                screen.blit(startButton.image, startButton.rect)
                pygame.display.flip()
                clock.tick(60)
        while run:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT: sys.exit()
                        if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_w:
                                        player1.go("up")
                                if event.key == pygame.K_d:
                                        player1.go("right")
                                if event.key == pygame.K_s:
                                        player1.go("down")
                                if event.key == pygame.K_a:
                                        player1.go("left")
                                        
                                if event.key == pygame.K_UP:
                                        player2.go("up")
                                if event.key == pygame.K_RIGHT:
                                        player2.go("right")
                                if event.key == pygame.K_DOWN:
                                        player2.go("down")
                                if event.key == pygame.K_LEFT:
                                        player2.go("left")
                        if event.type == pygame.KEYUP:
                                if event.key == pygame.K_w:
                                        player1.go("stop up")
                                if event.key == pygame.K_d:
                                        player1.go("stop right")
                                if event.key == pygame.K_s:
                                        player1.go("stop down")
                                if event.key == pygame.K_a:
                                        player1.go("stop left")

                                if event.key == pygame.K_UP:
                                        player2.go("stop up")
                                if event.key == pygame.K_RIGHT:
                                        player2.go("stop right")
                                if event.key == pygame.K_DOWN:
                                        player2.go("stop down")
                                if event.key == pygame.K_LEFT:
                                        player2.go("stop left")
                                        
                        
                if len(balls) < 10:
                        if random.randint(0, .25*60) == 0:
                                balls += [Ball("images/Ball/spinnything.png",
                                                  [random.randint(0,10), random.randint(0,10)],
                                                  [random.randint(100, width-100), random.randint(100, height-100)])
                                                  ]
                if len(balls) < 10:
                        if random.randint(0, .25*60) == 0:
                                balls += [Ball("images/Ball/crabman.png",
                                                  [random.randint(0,10), random.randint(0,10)],
                                                  [random.randint(100, width-100), random.randint(100, height-100)])
                                                  ]
          
  
                player1.update(width, height)
                player2.update(width, height)
                for ball in balls:
                        ball.update(width, height)
                        
    
        
                for bully in balls:
                        for victem in balls:
                                bully.collideBall(victem)
                                bully.collidePlayer(player1)
                                bully.collidePlayer(player2)
                
                for ball in balls:
                        if not ball.living:
                                balls.remove(ball)
                
                bgColor = r,g,b
                screen.fill(bgColor)
                screen.blit(bgI, bgR)
                for ball in balls:
                        screen.blit(ball.image, ball.rect)
                screen.blit(player1.image, player1.rect)
                screen.blit(player2.image, player2.rect)
                pygame.display.flip()
                clock.tick(60)
        
        
        
        
        
        
        
        
        
        
        
        
