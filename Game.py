import pygame,sys
from pygame.locals import *
import random

import Sprite
import Player
import Tilemap

class Game():

    # game constructor

    def __init__(self,tilemap,player):
        self.tilemap = tilemap  # map
        self.player = player  # agent
        self.objectList = []  # list of objects
        
        # let the game begin
        pygame.init()

        # display the game window
        self.DISPLAYSURF = pygame.display.set_mode((tilemap.mapwidth*tilemap.tilesize + 400,tilemap.mapheight*tilemap.tilesize))
    
    # adds object to the tilemap, considers the object's size
  
    def addObject(this, sprite, width, height):
        this.objectList.append(sprite)
        for i in range(sprite.y - 1, sprite.y - 1 + height):
            for j in range (sprite.x, sprite.x + width):
                this.tilemap.matrix[i][j] = 0
    
    # adds object to the tilemap, considers that object should take the wall's place

    def addObjectOnWall(this, sprite):
        this.objectList.append(sprite)
    
    # removes object from the map
    
    def deleteObject(this, sprite):
        this.objectList.remove(sprite)
    
    # shows and updates game window
  
    def display(self, text):
        # clears the window (necessary to update the text part)
        self.DISPLAYSURF.fill((0,0,0))
        
        # draws the tilemap
        for row in range(self.tilemap.mapheight):
            for column in range(self.tilemap.mapwidth):
                # draws specific type of tile/sprite at specific place
                self.DISPLAYSURF.blit(self.tilemap.textures[self.tilemap.matrix[row][column]],(column*self.tilemap.tilesize,row*self.tilemap.tilesize))

        # draws all sprites
        for i in range(len(self.objectList)):
            icon = pygame.image.load(self.objectList[i].image).convert_alpha()
            # draws specific object from the list at specific place
            self.DISPLAYSURF.blit(icon,(self.objectList[i].x*self.tilemap.tilesize,self.objectList[i].y*self.tilemap.tilesize))
        
        # draws the player
        icon = pygame.image.load(self.player.image).convert_alpha()
        self.DISPLAYSURF.blit(icon,(self.player.x*self.tilemap.tilesize,self.player.y*self.tilemap.tilesize))

        # shows the game clock
        self.DISPLAYSURF.blit(text, [790,0])
        
        # updates the game window
        pygame.display.update()
