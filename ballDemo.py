import pygame, sys, random
from Ball import Ball
from PlayerBall import PlayerBall


pygame.init()
  
clock = pygame.time.Clock()


width = 960
height = 600
size = width, height

bgColor = r,g,b = 100, 30, 234
bgI = pygame.image.load("map1.png")
bgR = bgI.get_rect()

screen = pygame.display.set_mode(size)

player = PlayerBall([width/2, height/2])

balls = []
balls += [Ball("images/Ball/ball.png", [4,5], [100, 125])]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                player.go("up")
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                player.go("right")
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                player.go("down")
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                player.go("left")
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                player.go("stop up")
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                player.go("stop right")
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                player.go("stop down")
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                player.go("stop left")
        
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
  
  
    player.update(width, height)
    for ball in balls:
        ball.update(width, height)
        
    for bully in balls:
        for victem in balls:
            bully.collideBall(victem)
            bully.collidePlayer(player)
    
    for ball in balls:
        if not ball.living:
            balls.remove(ball)
    
    bgColor = r,g,b
    screen.fill(bgColor)
    screen.blit(bgI, bgR)
    for ball in balls:
        screen.blit(ball.image, ball.rect)
    screen.blit(player.image, player.rect)
    pygame.display.flip()
    clock.tick(60)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
