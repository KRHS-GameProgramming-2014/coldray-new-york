import pygame, sys, random
from Ball import Ball
from PlayerBall import PlayerBall
from Wall import Wall


pygame.init()
  
clock = pygame.time.Clock()


width = 955
height = 610
size = width, height

bgColor = r,g,b = 100, 30, 234
bgI = pygame.image.load("map1.png")
bgR = bgI.get_rect()

walls = [Wall([13, 12], [931, 28]),
         Wall([13, 12], [26, 593]),
         Wall([21, 254], [90, 271]),
         Wall([163, 255], [577, 268]),
         Wall([270, 256], [285, 576]),
         Wall([562, 262], [576, 349]),
         Wall([23, 157], [254, 173]),
         Wall([317, 157], [752, 175]),
         Wall([739, 157], [755, 351]),
         Wall([512, 28], [529, 158]),
         Wall([913, 14], [931, 592]),
         Wall([560, 416], [576, 577]),
         Wall([739, 415], [755, 575])]
         
    

screen = pygame.display.set_mode(size)

player1 = PlayerBall([width/3, height/3])
player2 = PlayerBall([2*width/3, 2*height/3])

balls = []
balls += [Ball("images/Ball/crabman.png", [4,5], [100, 125])]

while True:
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
                
        
    if len(balls) < 5:
        if random.randint(0, .25*60) == 0:
            balls += [Ball("images/Ball/spinnything.png",
                      [random.randint(0,10), random.randint(0,10)],
                      [random.randint(100, width-100), random.randint(100, height-100)])
                      ]
    if len(balls) < 5:
        if random.randint(0, .25*60) == 0:
            balls += [Ball("images/Ball/crabman.png",
                      [random.randint(0,10), random.randint(0,10)],
                      [random.randint(100, width-100), random.randint(100, height-100)])
                      ]
  
  
    player1.update(width, height)
    player2.update(width, height)
    for ball in balls:
        ball.update(width, height)
        
    for wall in walls:
        player1.collideWall(wall)
        player2.collideWall(wall)
     #   for ball in ball:
      #      ball.collideWall(wall)
        
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
    for wall in walls:
        screen.blit(wall.image, wall.rect)
    screen.blit(player1.image, player1.rect)
    screen.blit(player2.image, player2.rect)
    pygame.display.flip()
    clock.tick(60)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
