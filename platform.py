import pygame
import time

class Platform(pygame.sprite.Sprite):

	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("platforms/longplat.png")
		self.rect = self.image.get_rect()
	def getImage(self):
		return self.image