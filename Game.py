import pygame,sys
from pygame.locals import *
import random

import Sprite
import Player
import Tilemap
import Customer
import Kitchen
import Number
import Colors

class Game():

    # game constructor

    def __init__(self,tilemap,player):
        self.tilemap = tilemap  # map
        self.player = player  # agent
        self.customers = [] # list of customers
        self.tableList = [] # list of tables
        self.numberList = [] # list of table numbers
        self.objectList = [] # list of objects other than tables

        # declaration of tables and other objects

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

        # declarations of customers and their table numbers;
        # up and down refers to tiles that waiter must stand od
        # to be able to serve a customer

        for i in range(len(self.tableList)):
            spr = self.tableList[i]
            up = [(spr.x, spr.y - 2),(spr.x + 1, spr.y - 2)]
            down = [(spr.x, spr.y + 1),(spr.x + 1, spr.y + 1)]
            self.customers.append(Customer.Customer(i+1,down,up))
            self.numberList.append(Number.Number(spr.x+1,spr.y,"textures/Black" + str(i+1) + ".png","textures/Orange" + str(i+1) + ".png","textures/Red" + str(i+1) + ".png","textures/Green" + str(i+1) + ".png"))

        # declaration of numbers' colors controller
        self.colors = Colors.Colors(self.customers, self.numberList)

        # declaration of kitchen activities controller
        self.kitchen = Kitchen.Kitchen(len(self.customers))

        # calling function that supports collision preventing
        # depends on object's size

        # tables

        for element in self.tableList:
            self.preventCollisions(element,2,2)

        # other objects
        
        for element in self.objectList:
            if (element.image == 'textures/chairLt.png' or element.image == 'textures/chairRt.png'):
                self.preventCollisions(element,1,2)
            elif (element.image == 'textures/door.png'):
                pass
            else:
                self.preventCollisions(element,1,1)

        # font settings                
        pygame.font.init()
        self.font = pygame.font.Font(None, 30)

        # initial text
        self.message = self.font.render("Klienci czekaja na obsluge.", True, (255,255,255))
        self.hint = self.font.render("Nacisnij spacje, aby otrzymac wskazowke.", True, (255,255,255))

        # hints for user enable
        self.hintDisplay = True

        # let the game begin
        pygame.init()

        # display the game window
        self.DISPLAYSURF = pygame.display.set_mode((tilemap.mapwidth*tilemap.tilesize + 450,tilemap.mapheight*tilemap.tilesize))

    
    # function that supports collision preventing
    # takes into consideration object's size
    def preventCollisions(self, sprite, width, height):
        for i in range(sprite.y - 1, sprite.y - 1 + height):
            for j in range (sprite.x, sprite.x + width):
                self.tilemap.matrix[i][j] = 0

    # checking if it's the time to finish meal preparing
    def timeEvent(self,time,kitchen):
        timeList = kitchen.orderFinishTimes
        if (len(timeList) > 0):
            if (timeList[0][0] == time):
                message = kitchen.makeMealReady(self.customers[timeList[0][1]],time)
                kitchen.removeTimeEvent()
                return message

    # choosing the table to serve
    # TEMPORARY!!!
    # improving in progress

    def getDecision(self):
        # if some meal is ready, go and serve it
        ready = self.kitchen.anyMealReady()
        if (ready > 0):
            return ready
        else:
            # if there's no ready meal, serve random customer who
            # ordered a drink or haven't placed the order yet
            remaining = []
            for i in range(len(self.kitchen.customerStates)):
                if (self.kitchen.customerStates[i] == 0 or self.kitchen.customerStates[i] == 1):
                    remaining.append(i+1)
            if (len(remaining) > 0):
                index = random.randint(0, len(remaining) - 1)
                return remaining[index]
            # if everybody has placed the order and received ordered
            # drinks, do nothing but wait for meals
            else:
                return 0


    # shows and updates game window
 
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

        # draws all table numbers
        for element in self.numberList:
            icon = pygame.image.load(element.image).convert_alpha()
            # draws specific object from the list at specific place
            self.DISPLAYSURF.blit(icon,(element.x*self.tilemap.tilesize,element.y*self.tilemap.tilesize))        

        # draws all sprites other than tables
        for element in self.objectList:
            icon = pygame.image.load(element.image).convert_alpha()
            # draws specific object from the list at specific place
            self.DISPLAYSURF.blit(icon,(element.x*self.tilemap.tilesize,element.y*self.tilemap.tilesize))
        
        # some time format settings

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

        # text showing

        # checks if there's a message about new meal just prepared        
        message = self.timeEvent(time,self.kitchen)
        if (message != None):
            self.message = self.font.render(message, True, (255,255,255))

        # shows the game clock
        self.DISPLAYSURF.blit(time_output, [790,0])
        # shows logs
        self.DISPLAYSURF.blit(self.message, [790,50])
        # shows hints for user if enabled
        if (self.hintDisplay):
            self.DISPLAYSURF.blit(self.hint, [790,100])

        # updates the game window
        pygame.display.update()            

    
    # event handling

    def handle_events(self,time):
        for event in pygame.event.get():
            # game aborting
            if event.type == QUIT:
                exit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_x:
                    exit()
                    sys.exit()
                # player moving
                if event.key == K_UP:
                    self.player.move('up')
                if event.key == K_DOWN:
                    self.player.move('down')
                if event.key == K_RIGHT:
                    self.player.move('right')
                if event.key == K_LEFT:
                    self.player.move('left')
                # generating hints for player (where to go)
                if event.key == K_SPACE:
                    self.currentTable = self.getDecision()
                    if (self.currentTable > 0):
                        self.hint = self.font.render("Idz do stolika nr " + str(self.currentTable) + ".", True, (255,255,255))
                    else:
                        self.hint = self.font.render("Poczekaj na przygotowanie posilku.", True, (255,255,255))
                # table serving
                if event.key == K_RETURN:
                    message = self.customers[self.currentTable - 1].customerAction(time, self.kitchen, self.player, self.colors)
                    if (message != "action impossible"):
                        if (self.colors.getServed() == len(self.customers)):  # whoa, mission accomplished
                            message = "Wszyscy klienci obsluzeni!"
                            self.hintDisplay = False
                        else:  # you're standing on the wrong tile or customer already received the order
                            self.hint = self.font.render("Nacisnij spacje, aby otrzymac wskazowke.", True, (255,255,255))
                        self.message = self.font.render(message, True, (255,255,255))
