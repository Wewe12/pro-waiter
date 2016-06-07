import random
from random import shuffle
import Tilemap
import Sprite
import time


class Player(Sprite.Sprite):
    # przeladowanie konstruktora obiektu
    def __init__(self, x, y, texture_down, texture_up, texture_left, texture_right, tilemap):
        super(Player, self).__init__(x, y, texture_down)
        self.texture_down = texture_down
        self.texture_up = texture_up
        self.texture_left = texture_left
        self.texture_right = texture_right
        self.tilemap = tilemap

    def getCoordinates(self):
        return (self.x, self.y)

    def moveAlgorithm(self, directions):
        print directions
        for direction in directions:
            self.x = direction[0]
            self.y = direction[1]


    def move(self, direction):
        # w lewo
        if direction == 'left':
            if self.collision(self.tilemap, direction):
                self.x -= 1
            # zmiana tekstury gracza
            self.image = self.texture_left
        # w prawo
        elif direction == 'right':
            if self.collision(self.tilemap, direction):
                self.x += 1
            # zmiana tekstury gracza
            self.image = self.texture_right
        # w gore
        elif direction == 'up':
            if self.collision(self.tilemap, direction):
                self.y -= 1;
            # zmiana tekstury gracza
            self.image = self.texture_up
        # w dol
        elif direction == 'down':
            if self.collision(self.tilemap, direction):
                self.y += 1
            # zmiana tekstury gracza
            self.image = self.texture_down

    # funkcja wykrywajaca ewentualne kolizje
    # uniemozliwia wyjscia postaci gracza poza mape i wejscia na kafelek zajety przez inny obiekt
    def collision(self, tilemap, direction):

        # todo: uwzglednic rozne typy colliderow (nie tylko 0) np. check if >= 10


        # w lewo
        if direction == 'left':
            if self.x <= 1 or tilemap.matrix[self.y][self.x - 1] == 0 or tilemap.matrix[self.y][self.x - 1] == 2:
                # docelowy kafelek zajety
                return False
        # w prawo
        elif direction == 'right':
            if self.x >= tilemap.mapwidth - 2 or tilemap.matrix[self.y][self.x + 1] == 0 or tilemap.matrix[self.y][
                        self.x + 1] == 2:
                # docelowy kafelek zajety
                return False
        # w gore
        elif direction == 'up':
            if self.y <= 3 or tilemap.matrix[self.y - 1][self.x] == 0 or tilemap.matrix[self.y - 1][self.x] == 2:
                # docelowy kafelek zajety
                return False
        # w dol
        elif direction == 'down':
            if self.y >= tilemap.mapheight - 3 or tilemap.matrix[self.y + 1][self.x] == 0 or tilemap.matrix[self.y + 1][
                self.x] == 2:
                # docelowy kafelek zajety
                return False

        # docelowy kafelek jest wolny
        return True

    def lookaround(self, tilemap, direction):
        # rozgladanie wszedzie
        if direction == 'everywhere':
            around = [tilemap.matrix[self.y][self.x - 1], tilemap.matrix[self.y][self.x + 1],
                      tilemap.matrix[self.y - 1][self.x], tilemap.matrix[self.y + 1][self.x],
                      tilemap.matrix[self.y - 1][self.x - 1], tilemap.matrix[self.y + 1][self.x - 1],
                      tilemap.matrix[self.y - 1][self.x + 1], tilemap.matrix[self.y + 1][self.x + 1]]
        # rozgladanie w lewo
        elif direction == 'left':
            around = [tilemap.matrix[self.y][self.x - 1], tilemap.matrix[self.y + 1][self.x - 1],
                      tilemap.matrix[self.y - 1][self.x - 1]]
        # rozgladanie w prawo
        elif direction == 'right':
            around = [tilemap.matrix[self.y][self.x + 1], tilemap.matrix[self.y + 1][self.x + 1],
                      tilemap.matrix[self.y - 1][self.x + 1]]
        # rozgladanie w gore
        elif direction == 'up':
            around = [tilemap.matrix[self.y - 1][self.x], tilemap.matrix[self.y - 1][self.x + 1],
                      tilemap.matrix[self.y - 1][self.x - 1]]
        # rozgladanie w dol
        elif direction == 'down':
            around = [tilemap.matrix[self.y + 1][self.x], tilemap.matrix[self.y + 1][self.x + 1],
                      tilemap.matrix[self.y + 1][self.x - 1]]

        objectsFound = []
        for i in around:
            if i != 0:
                if i == 11:
                    objectsFound.append('plame')
                elif i == 12:
                    objectsFound.append('kurz')
                elif i == 13:
                    objectsFound.append('puszke')
                elif i == 14:
                    objectsFound.append('kosz')
                elif i == 15:
                    objectsFound.append('mop')
        return objectsFound
