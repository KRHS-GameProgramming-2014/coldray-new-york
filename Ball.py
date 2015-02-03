import pygame, math

class Ball():
	def __init__(self, image, speed = [0,0], pos = [0,0]):
		self.image = pygame.image.load(image)
		self.rect = self.image.get_rect()
		self.speedx = speed[0]
		self.speedy = speed[1]
		self.speed = [self.speedx, self.speedy]
		self.place(pos)
		self.didBounceX = False
		self.didBounceY = False
		self.radius = (int(self.rect.height/2.0 + self.rect.width/2.0)/2) - 1
		self.living = True
		
	def place(self, pos):
		self.rect.center = pos
		
	def update(self, width, height):
		self.didBounceX = False
		self.didBounceY = False
		self.move()
		self.collideEdge(width, height)
		
	def move(self):
		self.speed = [self.speedx, self.speedy]
		self.rect = self.rect.move(self.speed)
		
	def collideEdge(self, width, height):
		if not self.didBounceX:
			#print "trying to hit Wall"
			if self.rect.left < 0 or self.rect.right > width:
				self.speedx = -self.speedx
				self.didBounceX = True
				#print "hit xWall"
		if not self.didBounceY:
			if self.rect.top < 0 or self.rect.bottom > height:
				self.speedy = -self.speedy
				self.didBounceY = True
				#print "hit xWall"
		
	def collideBall(self, other):
		if self != other:
			if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
				if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
					if (self.radius + other.radius) > self.distance(other.rect.center):
						if not self.didBounceX:
							self.speedx = -self.speedx
							self.didBouncex = True
						if not self.didBounceY:
							self.speedy = -self.speedy
							self.didBounceY = True
							#print "hit Ball"
							
	def collidePlayer(self, other):
		if self != other:
			if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
				if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
					if (self.radius + other.radius) > self.distance(other.rect.center):
						self.living = False
	
	def distance(self, pt):
		x1 = self.rect.center[0]
		y1 = self.rect.center[1]
		x2 = pt[0]
		y2 = pt[1]
		return math.sqrt(((x2-x1)**2) + ((y2-y1)**2))
        
        
        def collideWall(self, wall):
            if self.rect.right > wall.rect.left and self.rect.left < wall.rect.right:
                if self.rect.bottom > wall.rect.top and self.rect.top < wall.rect.bottom:
                    if not self.didBounceX and self.speedx != 0:
                        self.speedx = -self.speedx*1
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
                        
                    
                    


            
            
            
            
            
            
            
            
		
		
		
		
