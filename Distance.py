import math

import Player
import Customer

class Distance:

    def __init__(self, player):
        self.player = player
        self.kitchen = (15,2)

    def getDistance(self, customer, viaKitchen):
        if (viaKitchen):
            distanceToKitchen = abs(self.player.x-15) + abs(self.player.y-2)
            distanceFromKitchen = abs(customer.tilesup[0][0] - 15) + abs(customer.tilesup[0][1] - 2)
            distance = distanceToKitchen + distanceFromKitchen
        else:
            distance = abs(customer.tilesup[0][0] - self.player.x) + abs(customer.tilesup[0][1] - self.player.y)
        return distance
