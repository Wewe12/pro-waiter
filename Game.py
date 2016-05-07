import pygame,sys
from pygame.locals import *
import random

import Sprite
import Player
import Tilemap
import Customer
import Kitchen

class Game():

    # game constructor

    def __init__(self,tilemap,player):
        self.tilemap = tilemap  # map
        self.player = player  # agent
        self.customers = [] # list of customers
        self.tableList = [] # list of tables
        self.objectList = [] # list of objects other than tables

        # tables

        self.tableList.append(Sprite.Sprite(3,6,'textures/tableSmall.png'))
        self.tableList.append(Sprite.Sprite(12,6,'textures/tableSmall.png'))
        self.tableList.append(Sprite.Sprite(3,12,'textures/tableSmall.png'))
        self.tableList.append(Sprite.Sprite(12,12,'textures/tableSmall.png'))
        self.tableList.append(Sprite.Sprite(22,6,'textures/tableSmall.png'))
        self.tableList.append(Sprite.Sprite(29,6,'textures/tableSmall.png'))
        self.tableList.append(Sprite.Sprite(22,12,'textures/tableSmall.png'))
        self.tableList.append(Sprite.Sprite(29,12,'textures/tableSmall.png')) 

        # chairs

        self.objectList.append(Sprite.Sprite(2,6,'textures/chairRt.png'))
        self.objectList.append(Sprite.Sprite(5,6,'textures/chairLt.png'))
        self.objectList.append(Sprite.Sprite(2,12,'textures/chairRt.png'))
        self.objectList.append(Sprite.Sprite(5,12,'textures/chairLt.png'))
        self.objectList.append(Sprite.Sprite(11,6,'textures/chairRt.png'))
        self.objectList.append(Sprite.Sprite(14,6,'textures/chairLt.png'))
        self.objectList.append(Sprite.Sprite(11,12,'textures/chairRt.png'))
        self.objectList.append(Sprite.Sprite(14,12,'textures/chairLt.png'))
        self.objectList.append(Sprite.Sprite(21,6,'textures/chairRt.png'))
        self.objectList.append(Sprite.Sprite(24,6,'textures/chairLt.png'))
        self.objectList.append(Sprite.Sprite(21,12,'textures/chairRt.png'))
        self.objectList.append(Sprite.Sprite(24,12,'textures/chairLt.png'))
        self.objectList.append(Sprite.Sprite(28,6,'textures/chairRt.png'))
        self.objectList.append(Sprite.Sprite(31,6,'textures/chairLt.png'))
        self.objectList.append(Sprite.Sprite(28,12,'textures/chairRt.png'))
        self.objectList.append(Sprite.Sprite(31,12,'textures/chairLt.png'))

        # plants

        self.objectList.append(Sprite.Sprite(18,6,'textures/flower2.png'))
        self.objectList.append(Sprite.Sprite(18,9,'textures/flower2.png'))
        self.objectList.append(Sprite.Sprite(18,12,'textures/flower2.png'))
        self.objectList.append(Sprite.Sprite(18,15,'textures/flower2.png'))

        # door

        self.objectList.append(Sprite.Sprite(15,2,'textures/door.png'))

        for i in range(len(self.tableList)):
            spr = self.tableList[i]
            up = [(spr.x, spr.y - 2),(spr.x + 1, spr.y - 2)]
            down = [(spr.x, spr.y + 1),(spr.x + 1, spr.y + 1)]
            self.customers.append(Customer.Customer(i+1,down,up))

        for element in self.tableList:
            self.preventCollisions(element,2,2)
        
        for element in self.objectList:
            if (element.image == 'textures/chairLt.png' or element.image == 'textures/chairRt.png'):
                self.preventCollisions(element,1,2)
            elif (element.image == 'textures/door.png'):
                pass
            else:
                self.preventCollisions(element,1,1)
                
        # let the game begin
        pygame.init()

        # display the game window
        self.DISPLAYSURF = pygame.display.set_mode((tilemap.mapwidth*tilemap.tilesize + 450,tilemap.mapheight*tilemap.tilesize))

        # pygame rectangle object - for text clearing
        self.rect = pygame.Rect
        
        self.kitchen = Kitchen.Kitchen(len(self.customers))

        pygame.font.init()
        self.font = pygame.font.Font(None, 30)

        self.message = self.font.render("Klienci czekaja na obsluge.", True, (255,255,255))
        self.hint = self.font.render("Nacisnij spacje, aby otrzymac wskazowke.", True, (255,255,255))
    
    # adds object to the tilemap, considers the object's size
  
    def preventCollisions(self, sprite, width, height):
        for i in range(sprite.y - 1, sprite.y - 1 + height):
            for j in range (sprite.x, sprite.x + width):
                self.tilemap.matrix[i][j] = 0
    
    # shows and updates game window

    def timeEvent(self,time,kitchen):
        timeList = kitchen.orderFinishTimes
        if (len(timeList) > 0):
            if (timeList[0][0] == time):
                message = kitchen.makeMealReady(self.customers[timeList[0][1]],time)
                kitchen.removeTimeEvent()
                return message
 
    def display(self, time):
        # clears the text window (necessary to update)
        self.DISPLAYSURF.fill((0,0,0))
        
        # draws the tilemap
        for row in range(self.tilemap.mapheight):
            for column in range(self.tilemap.mapwidth):
                # draws specific type of tile/sprite at specific place
                self.DISPLAYSURF.blit(self.tilemap.textures[self.tilemap.matrix[row][column]],(column*self.tilemap.tilesize,row*self.tilemap.tilesize))

        # draws all tables
        for element in self.tableList:
            icon = pygame.image.load(element.image).convert_alpha()
            # draws specific object from the list at specific place
            self.DISPLAYSURF.blit(icon,(element.x*self.tilemap.tilesize,element.y*self.tilemap.tilesize))

        # draws all sprites other than tables
        for element in self.objectList:
            icon = pygame.image.load(element.image).convert_alpha()
            # draws specific object from the list at specific place
            self.DISPLAYSURF.blit(icon,(element.x*self.tilemap.tilesize,element.y*self.tilemap.tilesize))
        
        # draws the player
        icon = pygame.image.load(self.player.image).convert_alpha()
        self.DISPLAYSURF.blit(icon,(self.player.x*self.tilemap.tilesize,self.player.y*self.tilemap.tilesize))

        # divide by 60 to get total minutes
        minutes = time // 60
 
        # use modulus (remainder) to get seconds
        seconds = time % 60

        # use python string formatting to format in leading zeros
        output_string = "{0:02}:{1:02}".format(minutes, seconds)
 
        # prepare to blit to the screen
        time_output = self.font.render(output_string, True, (255,255,255))

        message = self.timeEvent(time,self.kitchen)
        if (message != None):
            self.message = self.font.render(message, True, (255,255,255))

        # shows the game clock
        self.DISPLAYSURF.blit(time_output, [790,0])
        self.DISPLAYSURF.blit(self.message, [790,50])
        self.DISPLAYSURF.blit(self.hint, [790,100])

        # updates the game window
        pygame.display.update()

    def getDecision(self):
        if (self.kitchen.anyMealReady() > 0):
            self.currentTable = self.kitchen.anyMealReady() + 1
        else:
            table = random.randint(1,len(self.tableList))
            return table

    def handle_events(self,time):
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_x:
                    exit()
                    sys.exit()
                if event.key == K_UP:
                    self.player.move('up')
                if event.key == K_DOWN:
                    self.player.move('down')
                if event.key == K_RIGHT:
                    self.player.move('right')
                if event.key == K_LEFT:
                    self.player.move('left')
                if event.key == K_SPACE:
                    self.currentTable = self.getDecision()
                    self.hint = self.font.render("Idz do stolika nr " + str(self.currentTable) + ".", True, (255,255,255))
                if event.key == K_RETURN:
                    message = self.customers[self.currentTable - 1].customerAction(time, self.kitchen, self.player)
                    if (message != "action impossible"):
                        self.message = self.font.render(message, True, (255,255,255))
                if event.key == K_KP_ENTER:
                    message = self.kitchen.makeMealReady(self.customers[self.currentTable - 1], time)
                    self.message = self.font.render(message, True, (255,255,255))
