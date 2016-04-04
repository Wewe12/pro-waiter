import random
from random import shuffle

class Tilemap:
    #konstruktor mapy
    def __init__(self,textures,matrix,mapwidth,mapheight):
        self.textures = textures			#lista tekstur
        self.matrix = matrix				#lista reprezentujaca mape
        self.tilesize = 23				#rozmiar pojedynczego kafelka
        self.mapwidth = mapwidth			#szerokosc mapy
        self.mapheight = mapheight			#wysokosc mapy