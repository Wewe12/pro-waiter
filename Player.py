import random
from random import shuffle
import time

import Tilemap
import Sprite

class Player(Sprite.Sprite):

    # object's constructor overloading

    def __init__(self,x,y,texture_down,texture_up,texture_left,texture_right,tilemap):
        super(Player,self).__init__(x,y,texture_down)
        self.texture_down = texture_down
        self.texture_up = texture_up
        self.texture_left = texture_left
        self.texture_right = texture_right
        self.tilemap = tilemap


    def getCoordinates(self):
        return (self.x, self.y)

    def moveAlgorithm(self, directions):
        path = []
        for i in range(len(directions) - 1):
            if directions[i][0] < directions[i + 1][0]:
                path.append('right')
            elif directions[i][0] > directions[i + 1][0]:
                path.append('left')
            elif directions[i][1] < directions[i + 1][1]:
                path.append('down')
            elif directions[i][1] > directions[i + 1][1]:
                path.append('up')
        return path

    def setCoordinates(self, x, y):
        self.x = x
        self.y = y

    # moving player function

    def move(self,direction):
        # to the left
        if direction == 'left':
            if self.collision(self.tilemap, direction):
                self.x -= 1
            # player's texture change
            self.image = self.texture_left
        # to the right
        elif direction == 'right':
            if self.collision(self.tilemap, direction):
                self.x += 1
                # player's texture change
            self.image = self.texture_right
        # up
        elif direction == 'up':
            if self.collision(self.tilemap, direction):
                self.y -= 1;
            # player's texture change
            self.image = self.texture_up
        # down
        elif direction == 'down':
            if self.collision(self.tilemap, direction):
                self.y += 1
            # player's texture change
            self.image = self.texture_down

    # detecting possible collisions function
    # prevents moving player outside the map and enetering the tile already occupied

    def collision(self,tilemap,direction):
    
        # todo: uwzglednic rozne typy colliderow (nie tylko 0) np. check if >= 10
    
        # to the left
        if direction == 'left':
            if self.x <= 1 or tilemap.matrix[self.y][self.x-1] == 0 or tilemap.matrix[self.y][self.x-1] == 2 :
                # target tile occupied
                return False
        # to the right
        elif direction == 'right':
            if self.x >= tilemap.mapwidth - 2 or tilemap.matrix[self.y][self.x+1] == 0 or tilemap.matrix[self.y][self.x+1] == 2:
                # target tile occupied
                return False
        # up
        elif direction == 'up':
            if self.y <= 3 or tilemap.matrix[self.y-1][self.x] == 0 or tilemap.matrix[self.y-1][self.x] == 2:
                # target tile occupied
                return False
        # down
        elif direction == 'down':
            if self.y >= tilemap.mapheight - 3 or tilemap.matrix[self.y+1][self.x] == 0 or tilemap.matrix[self.y+1][self.x] == 2:
                # target tile occupied
                return False

        # target tile unoccupied
        return True
