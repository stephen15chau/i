import pygame
import time
class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.wdown = False
        self.jumping = False
        self.xSpeed = 0
        self.ySpeed = 0
        self.yAccel = .06
        self.xPos = 0
        self.yPos = 0
        self.facingLeft = False
        self.walk0 = pygame.image.load("wa;l/walk0.png")
        self.walk1 = pygame.image.load("wa;l/walk1.png")
        self.walk2 = pygame.image.load("wa;l/walk2.png")
        self.walk3 = pygame.image.load("wa;l/walk3.png")
        self.walk4 = pygame.image.load("wa;l/walk4.png")

        self.walk5 = pygame.transform.flip(self.walk0,True,False)
        self.walk6 = pygame.transform.flip(self.walk1,True,False)
        self.walk7 = pygame.transform.flip(self.walk2,True,False)
        self.walk8 = pygame.transform.flip(self.walk3,True,False)
        self.walk9 = pygame.transform.flip(self.walk4,True,False)

        self.jump1 = pygame.transform.flip(pygame.image.load("wa;l/jump.png"),True,False)
        self.jump2 = pygame.transform.flip(pygame.image.load("wa;l/jump0.png"),True,False)

        self.walkRightFrames = [self.walk5,self.walk6,self.walk7,self.walk8,self.walk9]
        self.walkLeftFrames = [self.walk0,self.walk1,self.walk2,self.walk3,self.walk4]
        self.image = pygame.image.load("wa;l/walk0.png")
        transColor = self.image.get_at((0,0))
        self.rect = self.image.get_rect()
        self.millis = int(round(time.time() * 1000))
        self.image.set_colorkey(transColor)
    def getImage(self):

    	return self.image
    def update(self):
    	pygame.sprite.Sprite.update(self)
    	self.t = int(round(time.time() * 1000))
    	
    	#direction on the ground
    	if self.xSpeed == 1 and abs(self.yPos-450) <= 63:
    		self.image = self.walkLeftFrames[((self.t-self.millis)/110)%5]
    	if self.xSpeed == -1 and abs(self.yPos-450) <= 63:
    		self.image = self.walkRightFrames[((self.t-self.millis)/110)%5]
    	
    	#direction midair
    	if self.jumping == True:
    		if self.xSpeed < 0:
    			self.image = self.jump2
    		if self.xSpeed > 0:
    			self.image = pygame.image.load("wa;l/jump0.png")
    	if self.jumping == False and abs(self.yPos - 450) > 63:
    		if self.xSpeed < 0:
    			self.image = self.jump1
    		if self.xSpeed > 0:
    			self.image = pygame.image.load("wa;l/jump.png")
    	
    	#when you hit the jump key
    	if self.jumping == True and self.ySpeed >= 0 and abs(self.yPos-450) <= 63:
    		if self.xSpeed < 0 or self.facingLeft == True:
    			self.image = self.jump2
    		if self.xSpeed > 0 or self.facingLeft == False:
    			self.image = pygame.image.load("wa;l/jump0.png")
    		self.ySpeed = -2.6
    		self.tm = int(round(time.time() * 1000))

    	#when you fall down
    	if self.ySpeed > 0 and self.jumping == True and abs(self.yPos - 450) > 63:
    		self.jumping = False
    		if self.xSpeed < 0 or self.facingLeft == True:
    			self.image = self.jump1
    		if self.xSpeed > 0 or self.facingLeft == False:
    			self.image = pygame.image.load("wa;l/jump.png")

    	if abs(self.yPos-450) <= 63 and self.jumping == False:
    		self.ySpeed = 0
    		
    		if(self.facingLeft == False and self.xSpeed == 0 and self.ySpeed == 0):
    			self.image = pygame.image.load("wa;l/walk0.png")
    		if self.facingLeft == True and self.xSpeed == 0 and self.ySpeed == 0:
    			self.image = self.walk5
    	
    	self.xPos += self.xSpeed
    	self.yPos += self.ySpeed
    	if abs(self.yPos-450) > 63:
    		if self.wdown == True:
    			
    			self.ySpeed += self.yAccel/2.0
    		if self.wdown == False:
    			
    			self.ySpeed += self.yAccel	


    	
    	

    

    def getX(self):
   	    return self.xPos
    
    def getY(self):
    	return self.yPos
    
    def setX(self, x):
    	self.xPos = x
    
    def setY(self, y):
    	self.yPos = y
	
    def getXSpeed(self):
    	return self.xSpeed

    def getYSpeed(self):
    	return self.ySpeed

    def setXSpeed(self, xs):
    	self.xSpeed = xs 

    def setYSpeed(self, ys):
    	self.ySpeed = ys 
        
    def isJumping(self):
    	return self.jumping

    def setJumping(self,j):
    	self.jumping = j
        
