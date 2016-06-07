import pygame,sys
from pygame.locals import *
import random

import Sprite
import Player
import Tilemap

class Game():
    #konstruktor gry
    def __init__(self,tilemap,player,objectList):
        self.tilemap = tilemap                              #mapa
        self.player = player                                #gracz
        self.objectList = objectList                        #lista obiektow
        self.inventory = [ 0,0,0 ]                          #[0]mop #[1]puszka #[2]cos
        
        #rozpocznij gre
        pygame.init()
        #wyswietl okno gry
        self.DISPLAYSURF = pygame.display.set_mode((tilemap.mapwidth*tilemap.tilesize + 400,tilemap.mapheight*tilemap.tilesize))
      
    def addObject(this, sprite, width, height):
        this.objectList.append(sprite)
        for i in range(sprite.y - 1, sprite.y - 1 + height):
            for j in range (sprite.x, sprite.x + width):
                this.tilemap.matrix[i][j] = 0
    
    def addObjectOnWall(this, sprite):
        this.objectList.append(sprite)
        
    def deleteObject(this, sprite):
        this.objectList.remove(sprite)
        # for i in range(len(this.objectList)):
            # if this.objectList[i] == sprite:
                # this.objectList[i].remove
    
    #wyswietlanie i odswiezanie okna gry  
    def display(self):
        #rysowanie mapy
        for row in range(self.tilemap.mapheight):
            for column in range(self.tilemap.mapwidth):
                #rysuj w okreslonym miejscu okreslony typ kafelka/obiektu
                self.DISPLAYSURF.blit(self.tilemap.textures[self.tilemap.matrix[row][column]],(column*self.tilemap.tilesize,row*self.tilemap.tilesize))



        #rysowanie wszystkich obiektow
        for i in range(len(self.objectList)):
            icon = pygame.image.load(self.objectList[i].image).convert_alpha()
            #rysuj w okreslonym miejscu okreslony obiekt z listy
            self.DISPLAYSURF.blit(icon,(self.objectList[i].x*self.tilemap.tilesize,self.objectList[i].y*self.tilemap.tilesize))
        
        #rysowanie gracza
        icon = pygame.image.load(self.player.image).convert_alpha()
        self.DISPLAYSURF.blit(icon,(self.player.x*self.tilemap.tilesize,self.player.y*self.tilemap.tilesize))
        
        #odswiezanie widoku
        pygame.display.update()