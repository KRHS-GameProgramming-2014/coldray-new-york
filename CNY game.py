import pygame, sys, random
from HUD import *
from Ball import Ball
from PlayerBall import PlayerBall
from HUD import Text
from HUD import Score
from Button import Button

pygame.init()

clock = pygame.time.Clock()

width = 800 
height = 600
size = width, height

bgColor = r,g,b = 0, 255, 95
bgI = pygame.image.load("images/map1.PNG")
bgR = bgI.get_rect()

screen = pygame.display.set_mode(size)

player = PlayerBall([width/2, height/2])

balls = []
balls += [Ball("images/Ball/Doge.PNG", [4,5], [100, 125])]

title = Text([height/4, width/8], "HUD!!", 20)

run = False

startButton = Button([width/2, height-300], 
                                     "images/Buttons/Start Base.png", 
                                     "images/Buttons/Start Clicked.png")

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
		
	if len(balls) < 100:
		if random.randint(0, .25*60) == 0:
			balls += [Ball("images/Ball/Newocti.PNG",
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
	screen.blit(title.image, title.rect)
	pygame.display.flip()
	clock.tick()
		
		
		
		
		
		
		
		
		
		
		
		
		
		
