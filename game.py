import pygame
from pygame.locals import *
from player import Player
from platform import Platform
BLACK = (0,0,0,)
WHITE = (255,255,255)
BLUE =  (0,0,255)
RED = (255,0,0)
GREEN = (0,255,0)
WIDTH = 1600
HEIGH = 900

def main():
    pygame.init()
    
    
    width, height = 1600, 900
    screen = pygame.display.set_mode((width, height),pygame.FULLSCREEN)
  
    player = Player()
    plat0 = Platform()
    player.setX(800)
    player.setY(387)
    while 1:
        
        screen.fill(0)
    
        
        player.update()
        screen.blit(player.getImage(), (player.getX(),player.getY()))
        screen.blit(plat0.getImage(),(20,450))  

        

        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    player.setXSpeed(-1)
                    
                if event.key == pygame.K_d:
                    player.setXSpeed(1)

                if event.key == pygame.K_k:
                    player.setJumping(True)
                    player.wdown = True
                     

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a and player.getXSpeed() < 0:
                    player.setXSpeed(0)
                    player.facingLeft = True
                if event.key == pygame.K_d and player.getXSpeed() > 0:
                    player.setXSpeed(0)
                    player.facingLeft == False
                if event.key == pygame.K_k:
                    
                    player.wdown = False





main()
